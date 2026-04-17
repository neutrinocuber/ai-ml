import numpy as np
import matplotlib.pyplot as plt
l10=[-8.0,-7.5,-7.0,-2.0,-1.4,-0.8,8.5,9.2,10.0]
bdgp=[0.0,0.0,0.1,0.7,1.0,1.3,4.8,5.4,6.1]
tp=[0.0,0.0,0.0,0.5,0.5,0.5,1.0,1.0,1.0]
d=[]
l10norm=[0,0,0,0,0,0,0,0,0]
bdgpnorm=[0,0,0,0,0,0,0,0,0]
for i in range(len(l10)):
  l10norm[i]=(l10[i]-min(l10))/(max(l10)-min(l10))
  bdgpnorm[i]=(bdgp[i]-min(bdgp))/(max(bdgp)-min(bdgp))
l10sam=-1.2
bdgpsam=1.1
l10samnorm=(l10sam-min(l10))/(max(l10)-min(l10))
bdgpsamnorm=(bdgpsam-min(bdgp))/(max(bdgp)-min(bdgp))
for i in range(len(l10)):
  d.append(((l10norm[i]-l10samnorm)**2+(bdgpnorm[i]-bdgpsamnorm)**2)**0.5)
k=[0,0,0,0,0]
for i in range(len(k)):
  for j in range(0,len(d)):
    if d[k[i]]>d[j]:
      if i==0:
        k[i]=j
      else:
        if d[k[i-1]]<=d[j] and k[i-1]!=j:
          k[i]=j
cc=0
cs=0
ci=0
for i in range(len(k)):
  if tp[k[i]]==0.0:
    cc=cc+1
  if tp[k[i]]==1.0:
    ci=ci+1
  if tp[k[i]]==0.5:
    cs=cs+1
if cc>ci and cc>cs:
  print('sam is conductor')
  tpsam=0.0
elif ci>cc and ci>cs:
  print('sam is insulator')
  tpsam=1.0
elif cs>cc and cs>ci:
  print('sam is semiconductor')
  tpsam=0.5
else:
  if tp[k[0]]==0.0:
    print('sam is conductor')
    tpsam=0.0
  elif tp[k[0]]==0.5:
    print('sam is semiconductor')
    tpsam=0.5
  else:
    print('sam is insulator')
    tpsam=1.0
print(d)
for i in range(len(k)):
  print(l10[k[i]],bdgp[k[i]])
plt.scatter(l10,bdgp)
plt.scatter(l10sam,bdgpsam)
plt.show()
plt.scatter(l10,tp)
plt.scatter(l10sam,tpsam)
plt.show()
plt.scatter(bdgp,tp)
plt.scatter(bdgpsam,tpsam)
plt.show()
