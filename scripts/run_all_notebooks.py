from pathlib import Path
import sys, os, csv, time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import nbformat
from nbclient import NotebookClient
paths=sorted((ROOT/'notebooks').glob('chapter_*/*.ipynb'))
report=[]
for path in paths:
    t=time.time()
    try:
        nb=nbformat.read(path,as_version=4)
        NotebookClient(nb,timeout=180,kernel_name='python3',resources={'metadata':{'path':str(ROOT if '42a' not in path.parent.name else path.parent)}}).execute()
        status='PASS'; detail=''
    except Exception as exc:
        status='FAIL'; detail=f'{type(exc).__name__}: {str(exc)[:220]}'
    report.append([str(path.relative_to(ROOT)),status,round(time.time()-t,2),detail]);print(status, path.name, detail,flush=True)
with open(ROOT/'docs/execution_report.csv','w',newline='') as f:
    writer=csv.writer(f);writer.writerow(['notebook','status','seconds','error']);writer.writerows(report)
print('PASS',sum(r[1]=='PASS' for r in report),'/',len(report))
if any(r[1]!='PASS' for r in report):sys.exit(1)
