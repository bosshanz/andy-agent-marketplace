#!/usr/bin/env python3
"""Offline catalog and bundled-source integrity checks; does not run skills."""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def check():
    market = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text())
    lock = json.loads((ROOT / 'sources.lock.json').read_text())['plugins']
    assert re.fullmatch(r'[a-z0-9-]+', market['name']), 'Invalid marketplace name'
    names = [p['name'] for p in market['plugins']]
    assert len(set(names)) == len(names), 'Duplicate plugin names'
    assert set(names) == set(lock), 'Catalog and lock disagree'
    for entry in market['plugins']:
        name = entry['name']
        source = entry['source']
        pinned = lock[name]
        assert re.fullmatch(r'[0-9a-f]{40}', pinned['sha']), f'{name}: require full SHA'
        assert entry['policy'] == {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'}
        assert entry['category'] and (ROOT / 'catalog' / (name + '.md')).is_file()
        if source['source'] == 'url':
            assert source['sha'] == pinned['sha'] and source['url'] == pinned['repository']
            assert source['url'].startswith('https://github.com/')
        elif source['source'] == 'local':
            assert source['path'] == './plugins/' + name
            plugin = ROOT / 'plugins' / name
            manifest = json.loads((plugin / '.codex-plugin/plugin.json').read_text())
            assert manifest['name'] == name and manifest['version'] == pinned['version']
            assert manifest['skills'] == './skills/'
            assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])
            skills = {p.parent.name for p in (plugin / 'skills').glob('*/SKILL.md')}
            assert skills == set(pinned['skills']), f'{name}: missing or extra skills'
            actual = {str(p.relative_to(ROOT)) for p in (plugin / 'skills').rglob('*') if p.is_file()}
            expected = {p for p in pinned['files'] if '/skills/' in p}
            assert actual == expected, f'{name}: unexpected or missing bundled files'
            for rel, digest in pinned['files'].items():
                path = (ROOT / rel).resolve()
                assert path.is_relative_to(plugin.resolve()), 'Unsafe lock path'
                assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, f'Content changed: {rel}'
        else:
            raise AssertionError('Unsupported source: ' + source['source'])
    print(f'PASS: {len(names)} entries; fixed source SHAs; bundled files match recorded hashes.')

if __name__ == '__main__':
    check()
