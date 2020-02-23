#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np
import matplotlib.pyplot as plt
from random import seed
from random import random
import math


# In[79]:


def H(n):
    norm = 0    
    sum = 0
    maxSamples=10000
    seed(1)
    for i in range(0,maxSamples):
        for k in range(0,n):
            norm=norm+math.pow(random(),2)
        if(norm<1):
            sum = sum + 1
        norm=0
    I=sum/maxSamples
    seed(1)    
    return math.pow(2,n)*I


# In[81]:


Volume=np.zeros((20,1))
dimension=np.zeros((20,1))
for i in range(2,22):
    Volume[i-2][0]=H(i)
    dimension[i-2][0]=i


# In[82]:


plt.scatter(dimension,Volume)


# In[ ]:





# In[ ]:




