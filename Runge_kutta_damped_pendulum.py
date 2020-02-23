#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt


# In[153]:


import math
l=1
h=0.01
m=1
b=0.1
theta_0=math.pi/6

def theta_time(w):
    return w
def w_time(theta,w):
    return -(9.81/l)*math.sin(theta)-(b/(m*l))*w


# In[154]:


time = np.zeros((2000,1))
theta = np.zeros((2000,1))
w=np.zeros((2000,1))
theta[0][0]=math.pi/6
theta


# In[155]:


for i in range(1,2000):
    k11=h*w[i-1][0]
    k12=h*w_time(theta[i-1][0],w[i-1][0])
    k21=h*w[i-1][0]+0.5*k12*h
    k22=h*w_time(0.5*k11+theta[i-1][0],w[i-1][0]+0.5*k12)
    k31=h*w[i-1][0]+0.5*k22*h
    k32=h*w_time(0.5*k21+theta[i-1][0],w[i-1][0]+0.5*k22)
    k41=h*w[i-1][0]+k32*h
    k42=h*w_time(theta[i-1][0]+k31,w[i-1][0]+0.5*k32)
    theta[i][0]=theta[i-1][0]+(1/6)*(k11+2*k21+2*k31+k41)
    w[i][0]=w[i-1][0]+(1/6)*(k12+2*k22+2*k32+k42)
    time[i]=time[i-1]+h


# In[156]:


plt.scatter(time,theta)


# In[ ]:





# In[ ]:




