from pathlib import Path
import json, nbformat
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'docs/notebook_manifest.json').read_text())
assert len(m)==54,f'Expected 54 notebooks, got {len(m)}'
for x in m:
    p=root/x['path'];assert p.exists(),x['path'];nbformat.validate(nbformat.read(p,as_version=4))
print('Manifest and notebook structure verified:',len(m),'files')
