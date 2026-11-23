"""Fast engine-level test of all reconstructed notebook models; not a Jupyter kernel test."""
from pathlib import Path
import sys, json, csv, time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from scripts.lab_engine import run_lab
manifest=json.loads((ROOT/'docs/notebook_manifest.json').read_text())
rows=[]
for entry in manifest:
    if entry['chapter']=='42A':
        rows.append((entry['path'],'NOT_TESTED_BY_FAST_RUN','Observed RAND notebook requires full kernel execution'))
        continue
    try:
        res=run_lab(entry['chapter'],entry['chapter'],variant=entry['variant'])
        rows.append((entry['path'],'PASS',res['figure_path']))
    except Exception as exc:
        rows.append((entry['path'],'FAIL',repr(exc)))
with open(ROOT/'docs/fast_execution_report.csv','w',newline='') as f:
    w=csv.writer(f);w.writerow(['notebook','status','detail']);w.writerows(rows)
print('Successful engine calculations:',sum(x[1]=='PASS' for x in rows),'of',len(rows)-1)
if any(x[1]=='FAIL' for x in rows):sys.exit(1)
