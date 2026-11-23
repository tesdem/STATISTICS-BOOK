"""MASTER_V9 reproducible teaching demonstrations.
Created as a replacement-ready teaching package, not copied from the existing GitHub notebooks.
Each chapter run returns computed metrics and a plot, with a fixed local random generator.
Methods illustrate concepts under explicit synthetic assumptions; not independently validated research.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]

def run_lab(chapter, title, variant='main', seed=20261123):
    tag=str(chapter).upper().replace(' ','_')
    rng=np.random.default_rng(seed+sum(map(ord, tag+variant)))
    fig,ax=plt.subplots(figsize=(7,4)); metrics={'chapter':tag, 'variant':variant,'seed':seed,'evidence_class':'SYNTHETIC_TEACHING_SIMULATION','limitations':'Results depend on the stated simulated data-generating assumptions; not external validation.'}
    x=None; y=None; units='arbitrary units'
    def hist(v, caption='Simulated observations'):
        ax.hist(v,bins=25,color='#4d86aa',alpha=.85,edgecolor='white');ax.set(xlabel=caption,ylabel='Count')
    def line(xx, yy, label='Scenario'):ax.plot(xx,yy,marker='o',markersize=3,label=label);ax.set(xlabel='Scenario or sample index',ylabel='Model output')
    c=tag
    if c in ['1','5','15','16']:
        pop=rng.normal(50,12,20000); ns=[30,60,120,240,480,960]
        estimates=np.array([[rng.choice(pop,n,replace=False).mean() for _ in range(250)] for n in ns]); err=np.std(estimates,axis=1)
        line(ns,err,'Monte Carlo SE'); ax.set(xlabel='Sample size',ylabel='SD of sample mean estimates');metrics.update(population_mean=float(pop.mean()),se_at_n30=float(err[0]),se_at_n960=float(err[-1]))
    elif c in ['2','32','42','47','48']:
        p=rng.beta(2,7,500); costs=np.linspace(0,1,60); loss=np.array([np.mean(p*(1-t)**2 + 0.35*(1-p)*t**2 + 0.05*t) for t in costs]);line(costs,loss);ax.set(xlabel='Action threshold (illustrative)',ylabel='Mean assumed loss');metrics.update(minimum_loss=float(loss.min()),threshold=float(costs[np.argmin(loss)]))
    elif c in ['3','14']:
        latent=rng.normal(size=1000); obs=latent+rng.normal(0,.5,1000); repeat=latent+rng.normal(0,.5,1000);ax.scatter(obs,repeat,s=6,alpha=.2);ax.set(xlabel='Measurement A',ylabel='Measurement B');metrics['repeat_measure_correlation']=float(np.corrcoef(obs,repeat)[0,1])
    elif c in ['4','10','11','37','45']:
        truth=rng.binomial(1,.35,2000); scores=np.clip(.35+(.22 if c in ['37','45'] else .10)*(truth-.35)+rng.normal(0,.23,2000),0,1);bins=np.linspace(0,1,11);means=[truth[(scores>=a)&(scores<b)].mean() if ((scores>=a)&(scores<b)).sum() else np.nan for a,b in zip(bins[:-1],bins[1:])];ax.plot((bins[:-1]+bins[1:])/2,means,'o-');ax.plot([0,1],[0,1],'--',color='grey');ax.set(xlabel='Model score',ylabel='Observed fraction');metrics['brier_score']=float(np.mean((scores-truth)**2))
    elif c in ['6','9','40','43']:
        t=np.arange(30);logits=-1+.06*t; counts=rng.poisson(np.exp(logits)*80);line(t,counts);ax.set(xlabel='Time period',ylabel='Observed event count');metrics['first_period_count']=int(counts[0]);metrics['last_period_count']=int(counts[-1])
    elif c in ['7','12','18','20']:
        samples=rng.poisson(3.2,2000) if c in ['18','20'] else rng.normal(size=2000);hist(samples,'Simulated random variable');metrics.update(sample_mean=float(samples.mean()),sample_variance=float(samples.var(ddof=1)))
    elif c in ['8','33','44']:
        n=np.unique(np.logspace(2,4,12).astype(int));errors=np.array([abs(rng.normal(0,1,int(q)).mean()) for q in n]);line(n,errors);ax.set(xscale='log',xlabel='Monte Carlo replicates',ylabel='Absolute integration error');metrics['error_at_max_iterations']=float(errors[-1])
    elif c in ['13','26']:
        x=rng.normal(size=1000);missing=rng.random(1000)<1/(1+np.exp(-(x-1)));cc=x[~missing];hist(cc,'Available values (selection depends on value)');metrics.update(true_full_mean=float(x.mean()),complete_case_mean=float(cc.mean()),missing_rate=float(missing.mean()))
    elif c in ['17','23']:
        sig=np.linspace(0,.8,40);se=np.sqrt(2/100);power=stats.norm.cdf(-1.96-sig/se)+1-stats.norm.cdf(1.96-sig/se);line(sig,power);ax.set(xlabel='Effect size (SD units)',ylabel='Approximate two-sided test power');metrics.update(power_at_zero=float(power[0]),max_power=float(power[-1]))
    elif c=='19':
        raw=rng.normal(15,5,1000);z=(raw-raw.mean())/raw.std(ddof=0);hist(z,'Z-standardised values');metrics.update(z_mean=float(z.mean()),z_sd=float(z.std(ddof=0)))
    elif c=='21':
        ps=np.linspace(.01,.99,100);H=-ps*np.log2(ps)-(1-ps)*np.log2(1-ps);line(ps,H);ax.set(xlabel='Bernoulli event probability',ylabel='Binary entropy (bits)');metrics['maximum_entropy_bits']=float(H.max())
    elif c in ['22','24']:
        pop=rng.binomial(1,.62,400);phat=pop.mean();se=np.sqrt(phat*(1-phat)/len(pop));hist(rng.normal(phat,se,1500),'Asymptotic estimate distribution');metrics.update(phat=float(phat),wald_95_low=float(phat-1.96*se),wald_95_high=float(phat+1.96*se))
    elif c=='22A':
        n=np.array([20,40,80,160,320,640]);variances=[];bias=[]
        for m in n:
            draws=rng.normal(2,3,(300,int(m)));mean_est=draws.mean(axis=1);variances.append(float(mean_est.var(ddof=1)));bias.append(float(mean_est.mean()-2))
        line(n,variances,'Empirical variance');ax.plot(n,9/n,'--',label='Theory: sigma²/n');ax.legend();ax.set(xlabel='Sample size',ylabel='Variance of sample mean');metrics.update(theoretical_cramer_rao_n640=9/640,simulated_variance_n640=variances[-1],bias_n640=bias[-1])
    elif c in ['25','39']:
        est=rng.normal(.2,.2,20);weights=np.repeat(1/20,20);pooled=np.sum(weights*est);ax.errorbar(np.arange(20),est,yerr=.3,fmt='o',markersize=3);ax.axhline(pooled,ls='--');ax.set(xlabel='Study index',ylabel='Estimated effect ± illustrative interval');metrics['unweighted_pooled_effect']=float(pooled)
    elif c in ['27','29','34']:
        x=rng.normal(size=800);y=2+1.5*x+rng.normal(0,1.2,800);b=np.polyfit(x,y,1);ax.scatter(x,y,s=5,alpha=.25);ax.plot(np.sort(x),np.polyval(b,np.sort(x)),color='#ac6344');ax.set(xlabel='Predictor',ylabel='Outcome');metrics.update(slope=float(b[0]),intercept=float(b[1]),r_squared=float(np.corrcoef(x,y)[0,1]**2))
    elif c=='27A':
        v=rng.normal(size=(500,3));v[:,1]=.85*v[:,0]+.25*v[:,1];v[:,2]=.4*v[:,0]+.6*v[:,2];cov=np.cov(v,rowvar=False);eig,evec=np.linalg.eigh(cov);order=np.argsort(eig)[::-1];projection=v@evec[:,order];ax.scatter(projection[:,0],projection[:,1],s=7,alpha=.3);ax.set(xlabel='First principal component',ylabel='Second principal component');metrics.update(variance_explained_pc1=float(eig[order[0]]/eig.sum()),covariance_matrix=cov.round(4).tolist())
    elif c=='28':
        u=rng.normal(size=1600);t=(u+rng.normal(size=1600)>.3).astype(int);y=2*t+1.6*u+rng.normal(size=1600);naive=y[t==1].mean()-y[t==0].mean();# u observed in this instructional case
        x=np.column_stack((np.ones(len(u)),t,u));adj=np.linalg.lstsq(x,y,rcond=None)[0][1];ax.bar(['Unadjusted','Adjusted'],[naive,adj]);ax.axhline(2,ls='--',color='black');ax.set(ylabel='Treatment association/effect');metrics.update(naive_association=float(naive),adjusted_effect=float(adj),true_simulated_effect=2.0)
    elif c=='30':
        t=np.arange(100);y=np.zeros(100);eps=rng.normal(size=100)
        for i in range(1,len(y)): y[i]=.7*y[i-1]+eps[i]
        line(t,y);ax.set(xlabel='Time',ylabel='AR(1) simulated value');metrics['lag1_correlation']=float(np.corrcoef(y[:-1],y[1:])[0,1])
    elif c=='31':
        x=np.arange(100);y=2+.08*x+rng.normal(0,1,100);fit=np.polyfit(x[:80],y[:80],1);line(x[80:],y[80:],'Holdout actual');ax.plot(x[80:],np.polyval(fit,x[80:]),label='Linear forecast');ax.legend();metrics['holdout_mae']=float(np.mean(np.abs(np.polyval(fit,x[80:])-y[80:])))
    elif c=='32A':
        if variant=='reversal':
            eps=np.linspace(0,1,50);gap=.25-0.6*eps;line(eps,gap);ax.axhline(0,color='grey',ls='--');ax.set(xlabel='Contamination radius',ylabel='Expected loss difference');metrics['decision_reversal_epsilon']=float(.25/.6)
        elif variant=='coupled':
            budget=np.linspace(0,1,50);worst=.16-.31*budget;line(budget,worst);ax.axhline(0,color='grey',ls='--');ax.set(xlabel='Joint uncertainty budget',ylabel='Worst-case decision gap');metrics['illustrative_reversal_budget']=float(.16/.31)
        else:
            from scipy.optimize import linprog
            cvec=np.array([.6,.8,.25,.95]);resource=np.array([2.,3.,1.,4.]);budget=5.;sol=linprog(-cvec,A_ub=[resource],b_ub=[budget],bounds=[(0,1)]*len(cvec),method='highs');assert sol.success;ax.bar(np.arange(4),sol.x);ax.set(xlabel='Action',ylabel='Selected fractional allocation');metrics['optimized_gain']=float(cvec@sol.x)
    elif c=='35':
        x=rng.normal(size=700);y=(x>0).astype(int);simple=(x>.25).astype(int);ax.hist(x[y==0],alpha=.55,label='Class 0');ax.hist(x[y==1],alpha=.55,label='Class 1');ax.legend();metrics['rule_accuracy']=float((simple==y).mean())
    elif c=='36':
        query=rng.normal(size=20);docs=rng.normal(size=(150,20));docs[0]=query+.04*rng.normal(size=20);score=(docs@query)/(np.linalg.norm(docs,axis=1)*np.linalg.norm(query));ax.bar(np.arange(10),np.sort(score)[::-1][:10]);ax.set(xlabel='Ranked document',ylabel='Cosine retrieval score');metrics['highest_similarity']=float(score.max())
    elif c=='38':
        groups=rng.integers(0,2,2000);risk=rng.random(2000)+.13*groups;sel=risk>.5;rate=[sel[groups==g].mean() for g in (0,1)];ax.bar(['Group 0','Group 1'],rate);ax.set(ylabel='Selection proportion',ylim=(0,1));metrics['selection_rate_difference']=float(rate[1]-rate[0])
    elif c=='41':
        x=rng.normal(20,2,100);x[80:]+=3;line(np.arange(100),x);ax.axhline(20+3*2,ls='--');ax.axhline(20-3*2,ls='--');ax.set(xlabel='Production period',ylabel='Measurement');metrics['mean_after_shift']=float(x[80:].mean())
    elif c in ['46']:
        x=rng.standard_t(df=3,size=3000);ax.hist(x[(x>-10)&(x<10)],bins=45);ax.set(xlabel='Heavy-tailed variable',ylabel='Count');metrics['sample_excess_kurtosis']=float(stats.kurtosis(x))
    else:
        x=rng.normal(size=500);hist(x);metrics['mean']=float(x.mean())
    ax.set_title(f'Chapter {chapter}: {title[:58]}',fontsize=10)
    fig.tight_layout()
    out=ROOT/'outputs'/'figures'/f'chapter_{tag.lower()}_{variant}.png';fig.savefig(out,dpi=120);plt.close(fig)
    metrics['figure_path']=str(out.relative_to(ROOT))
    mp=ROOT/'outputs'/'metrics'/f'chapter_{tag.lower()}_{variant}.json';mp.write_text(json.dumps(metrics,indent=2,allow_nan=False))
    print('Chapter',chapter,'variant',variant,'results:',json.dumps({k:v for k,v in metrics.items() if k not in ('limitations','figure_path','evidence_class')},indent=2))
    return metrics
