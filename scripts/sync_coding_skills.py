#!/usr/bin/env python3
"""Update the bundled plugin from an explicit commit in a local upstream clone."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from verify import ROOT, check


def main():
    if len(sys.argv) != 3 or not re.fullmatch(r'[0-9a-f]{40}', sys.argv[2]):
        raise SystemExit('Usage: python3 scripts/sync_coding_skills.py LOCAL_UPSTREAM FULL_COMMIT_SHA')
    check()  # Refuse to overwrite modified or incomplete managed files.
    repo, sha = sys.argv[1:]
    def git(*args):
        return subprocess.check_output(['git', '-C', repo, *args])
    assert git('rev-parse', sha + '^{commit}').decode().strip() == sha
    pkg = json.loads(git('show', sha + ':package.json'))
    assert pkg['name'] == 'my-coding-skills'
    paths = git('ls-tree', '-r', '--name-only', sha).decode().splitlines()
    skills = sorted(p.split('/')[0] for p in paths if p.count('/') == 1 and p.endswith('/SKILL.md'))
    assert skills, 'No skills found'
    plugin = ROOT / 'plugins/my-coding-skills'
    # Resolve and fetch all source bytes before changing the existing package.
    payload = {}
    for rel in paths:
        if rel.split('/')[0] in skills:
            dest = plugin / 'skills' / rel
        elif rel in ('LICENSE', 'README.md', 'README.en.md'):
            dest = plugin / rel
        else:
            continue
        assert dest.resolve().is_relative_to(plugin.resolve()), 'Unsafe source path'
        mode = git('ls-tree', sha, '--', rel).decode().split()[0]
        assert mode in ('100644', '100755'), 'Only regular files can be packaged'
        payload[str(dest.relative_to(ROOT))] = (git('show', sha + ':' + rel), mode)
    lock_path = ROOT / 'sources.lock.json'
    lock = json.loads(lock_path.read_text())
    previous = lock['plugins']['my-coding-skills']
    for rel in set(previous['files']) - set(payload):
        (ROOT / rel).unlink()
    for rel, (data, mode) in payload.items():
        dest = ROOT / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        dest.chmod(0o755 if mode == '100755' else 0o644)
    previous.update(sha=sha, version=pkg['version'], skills=skills,
                    files={rel: hashlib.sha256(data).hexdigest() for rel, (data, _) in payload.items()})
    manifest_path = plugin / '.codex-plugin/plugin.json'
    manifest = json.loads(manifest_path.read_text())
    manifest['version'] = pkg['version']
    for path, value in [(lock_path, lock), (manifest_path, manifest)]:
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')
    check()
    print('Review git diff, update README/catalog version notes, and try the changed skills before release.')

if __name__ == '__main__':
    main()
