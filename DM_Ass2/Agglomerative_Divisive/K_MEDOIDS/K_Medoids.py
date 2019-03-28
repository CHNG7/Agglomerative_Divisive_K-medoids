import numpy as np 
import matplotlib.pyplot as plt
from copy import deepcopy
from IPython import embed
import time


# coding: utf-8

# In[11]:


import numpy as np
import pandas as pd
import random
from collections import defaultdict


# In[12]:


# df = pd.read_csv('Symmetric.csv',header=None) #importing the distance matrix of the data set
# df.head()
df=df.reset_index()
df1 = df['index']
df = np.array(df)
df1 = np.zeros([311,2])
df=np.delete(df,0,axis=1)
# df


# In[13]:


k=3                                       #Number of clusters
l=list()
i=0
while i<k:
    d=random.randint(0,311)               #taking random value between 0 and 311
    if d in l:
        continue
    else:
        i+=1
        l.append(random.randint(0,311))    #Making sure the numbers do not repeat
# l                                         #Choosing initial centroids


# In[14]:


def minsum(l):                           #defining function returning the value in l from which sum of squares of dist is least 
    a=list()
    for i in range(len(l)):
        sum1=0
        for j in range(len(l)):
            sum1+=df[l[i]][l[j]]
        a.append(sum1)
    return l[a.index(min(a))]    
k9=20                                    #Gives the number of updations of the centroid of the clusters
f3=list()
for o in range(k9):
    d1=list()
    f1=list()
    f2=list()
    data = defaultdict(list)             
    minimum = df.max().max()
    for i in range(df[0].size):
        if i not in l:                   #Not including the initial centroids that are in l
            a2=list()                    
            b3=0
            for k in range(len(l)):
                a2.append(df[i][l[k]])
                b3=a2.index(min(a2))
            data[b3].append(i)           #assigns the least distance points from their respective points in l to them again
    for i in range(len(l)):
        data[i].append(l[i])             #adding back the values in l to each cluster which was removed earlier
    for p in range(len(l)):
        f1.append(data[p])               #adding each of the k clusters whole as a list to the list f1 
        f2.append(minsum(data[p]))
    f3.append(f1)                        #appending list of clusters after each iteration
    l=f2                                 #updating the new centroids
#     print(l)


# In[17]:


df5 = pd.DataFrame(f3[-1]).T                             #returns the last value(list) of f3 which is the final set of k clusters 


# In[18]:


df5


# In[6]:


f3[1]


# In[7]:


l
