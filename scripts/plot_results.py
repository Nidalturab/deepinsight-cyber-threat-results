"""Redraw published values only; no model training or experimental replication."""
from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.spines.top':False,'axes.spines.right':False,'axes.spines.left':False,'axes.spines.bottom':False,'svg.fonttype':'none','pdf.fonttype':42})
COLORS=['#186779','#D58039']
def plot(source,field,name,title,subtitle):
 with (ROOT/'data'/source).open() as f: rows=list(csv.DictReader(f))
 fig,axs=plt.subplots(1,2,figsize=(14,8))
 fig.subplots_adjust(left=.07,right=.975,top=.65,bottom=.23,wspace=.22)
 fig.text(.07,.93,'DEEPINSIGHT  /  CYBER-THREAT DETECTION',fontsize=11,color=COLORS[0],weight='bold')
 fig.text(.07,.865,title,fontsize=24,weight='bold',color='#192C3A')
 fig.text(.07,.813,subtitle,fontsize=12,color='#52616B')
 fig.legend(handles=[Patch(color=c,label=l) for c,l in zip(COLORS,['Tabular data + DNN','DeepInsight images + CNN'])],loc='upper left',bbox_to_anchor=(.062,.785),ncol=2,frameon=False)
 for ax,ds in zip(axs,['NSL-KDD','CICMalDroid20']):
  selected=[r for r in rows if r['dataset']==ds]; x=list(range(len(selected)))
  for j,key in enumerate(['tabular_dnn','deepinsight_cnn']):
   vals=[float(r[key]) for r in selected]
   assert all(0<=v<=1 for v in vals)
   bars=ax.bar([n+(-.19 if j==0 else .19) for n in x],vals,.35,color=COLORS[j],zorder=3)
   ax.bar_label(bars,labels=[f'{v:.2f}' for v in vals],padding=4,fontsize=10)
  ax.set_title(ds,loc='left',fontweight='bold',fontsize=15,pad=18)
  labels=[r[field].replace('Overall accuracy','Overall\naccuracy').replace('SMSMalware','SMS\nmalware') for r in selected]
  ax.set_xticks(x,labels);ax.set_ylim(0,1.05);ax.set_yticks([0,.2,.4,.6,.8,1]);ax.set_ylabel('F1 score' if field=='class' else 'Score (0–1)');ax.grid(axis='y',color='#E4E9ED',zorder=0);ax.tick_params(length=0,pad=8)
 fig.text(.07,.133,'Published values, not rerun experiments. No uncertainty estimates reported.',fontsize=11,color='#334A59')
 fig.text(.07,.099,'Pipeline comparison: representation and model architecture both differ.',fontsize=11,color='#334A59')
 source_label='Table 4' if field=='metric' else 'Figure 1 numeric labels'
 fig.text(.07,.047,f'Source: AL-Essa et al. (2026), {source_label}, p. 1235. DOI: 10.11591/eei.v15i2.9649  |  Redrawn from source (CC BY-SA).',fontsize=9,color='#52616B')
 out=ROOT/'figures';out.mkdir(exist_ok=True)
 for ext in ['png','pdf','svg']:fig.savefig(out/f'{name}.{ext}',dpi=300,facecolor='white')
 plt.close(fig)
plot('aggregate_results.csv','metric','Results_Comparison','Image conversion did not improve aggregate scores','Reported results on two five-class cybersecurity datasets; all six aggregate comparisons favor the tabular pipeline.')
plot('per_class_results.csv','class','Per_Class_F1','Class-level effects vary across the datasets','The image pipeline improves SMSMalware and Riskware F1 in CICMalDroid20, while aggregate scores remain lower.')
print('Generated six figure files from published-result CSVs.')
