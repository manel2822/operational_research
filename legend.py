import pandas as pd
import matplotlib.pyplot as plt
data=[['A','B','7:00:00','7:30:00'],['A','C','8:00:00','8:30:00'], 
      ['X','B','7:30:00','8:30:00'],['X','C','7:30:00','8:00:00'],
      ['P','Q','7:30:00','8:30:00'],['P','C','9:00:00','9:30:00']]
df=pd.DataFrame(data,columns=['L','M','stime','etime'])
start_time=[]
end_time=[]
for i,row in df.iterrows():
   a=row['stime'].split(':')
   b=row['etime'].split(':')
   start_hrs=int(a[0])+(int(a[1])/60)+(int(a[2])/3600)
   end_hrs=int(b[0])+(int(b[1])/60)+(int(b[2])/3600)
   start_time.append(start_hrs)
   end_time.append(end_hrs)
df['start']=start_time
df['end']=end_time
df['diff']=df['end']-df['start']
color = {"B":"turquoise", "C":"crimson","Q":"orange"}
fig,ax=plt.subplots(figsize=(6,3))   
w=[]
lbl_pool = []
for i, task in enumerate(df.groupby("L")):
   w.append(task[0])
   for lbl, grp in task[1].groupby("M"):
      data = grp[["start", "diff"]]
      if lbl in lbl_pool:
          prefix = '_'
      else:
          lbl_pool.append(lbl)
          prefix=''
      ax.broken_barh(data.values, (i-0.4,0.8), color=color[lbl], label=prefix+lbl+"hi")

plt.legend()

plt.show()      