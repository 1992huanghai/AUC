# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 17:57:56 2015

@author: huanghai
"""
import random
from matplotlib import pyplot   
from sklearn.metrics import roc_auc_score  
from sklearn.metrics import roc_curve   
def auc(x,score): 
    FPR=[]
    TPR=[]  
    auc=0.0 
    FPR0=0
    TPR0=0
    FPR.append(FPR0)
    TPR.append(TPR0)
    for i in range(1000):
        threshold = 1-float(i)/1000
        FP=0
        TP=0
        N=0
        P=0
        for j in range(len(x)):
            if x[j]==0:
                N=N+1
            else :
                P=P+1
            if score[j]>threshold and x[j]==0:
                FP=FP+1
            elif score[j]>threshold and x[j]==1:
                TP=TP+1
        FPR1=float(FP)/N
        TPR1=float(TP)/P
        FPR.append(FPR1)
        TPR.append(TPR1)
        auc=auc+0.5*(FPR1-FPR0)*(TPR1+TPR0)
        FPR0=FPR1
        TPR0=TPR1
    auc=auc+0.5*(1-FPR0)*(1+TPR0)
    FPR.append(1)
    TPR.append(1)
    pyplot.plot(FPR,TPR)
    return auc


x=[]
score=[]
for i in range(1000):
    x.append(0)
    score.append(random.gauss(0.8,0.5))
for i in range(1000):
    x.append(1)
    score.append(random.gauss(0.2,0.5))    
print "auc值"+str(auc(x,score))+"  scikit auc值"+str(roc_auc_score(x,score))
fpr,tpr,thresholds=roc_curve(x,score)
pyplot.figure()
pyplot.plot(fpr,tpr)
    




