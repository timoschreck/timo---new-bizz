from pathlib import Path
import hashlib, json, re

root = Path(__file__).resolve().parents[1]
config = json.loads((root / 'config/site.json').read_text())
assert config['finalName'] is None
assert all(not c['enabled'] and c['target'] is None for c in config['contacts'].values())
for image in json.loads((root / 'assets/images/manifest.json').read_text())['images']:
    for field, digest in [('original', 'sha256_original'), ('web', 'sha256_web')]:
        data = (root / image[field]).read_bytes()
        assert hashlib.sha256(data).hexdigest() == image[digest], image[field]
for file in json.loads((root / 'vendor/dir4b/PROVENANCE.json').read_text())['files']:
    data = (root / file['destination']).read_bytes()
    git_digest = hashlib.sha1(f'blob {len(data)}\0'.encode() + data).hexdigest()
    assert git_digest == file['git_blob_sha'], file['destination']
html = (root / 'index.html').read_text()
for path in re.findall(r'(?:src|href)="([^"]+)"', html):
    if path.startswith('#'):
        assert f'id="{path[1:]}"' in html, path
    else:
        assert (root / path).is_file(), path
assert html.count('<section ') == 4
assert '<form' not in html
assert '690' not in html
print('PASS: configuration, 4 sections, image hashes, unchanged CI sources and local paths')
