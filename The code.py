#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[ ]:


import sympy
from sympy import sympify


# In[2]:


def F(x):
    # this for passing matmatical function as variables from user
    return eval("lambda x:" + input("Please input a function in numpy notation! \n For example: np.sin(x), np.cos(x)...etc  "))


# In[3]:


def integration():
    x = 1 #just fot intiliaziation
    f = F(x)
  
    print("input a,b,n")
    a=float(input())
    b=float(input())
    n=int(input())
    h = (b - a) / n
# divide adaptive trapezoidal rule to 3 parts to make the opreation easier.
    first = f(a) + f(b)
    sum = 0
    for i in range(1, n):
     sum = sum + f(a + (i * h))
    second = 2 * sum
    third = h * 0.5 * (first + second)
    return third


# In[4]:


def composite_trapziodal():
    
#this method to compute the integral of the functions given using composite trapezoidal rule from.

 condtion=True
 while(condtion):
    area= integration()
    

    print("the integral of the functions  using composite trapezoidal is ",area)
    print("do you want to integrate another function ? yes or no")
    answer=input()
    if answer == "yes":
        condtion=True
    else:
        condtion=False 



# In[ ]:


composite_trapziodal()


# In[ ]:





# In[5]:


tol=np.sqrt(np.finfo(float).eps) # the machine epilson program will stop if it arrive to it. 
level=0
def adaptive_trapezoidal(f,left,right,area,maxlevel):
    global tol
    global level
    mid=(left+right)/2
    leftarea=0.5*(f(left)+f(mid))*(mid-left)
    rightarea=0.5*(f(mid)+f(right))*(right-mid)
   
    if abs( ( area-(leftarea+rightarea) ) / 3 ) <= tol:
        area=(leftarea+rightarea)
        return area
    
    
        
    elif(level>= maxlevel):
        print("arrived to max level",level)
        return (leftarea+rightarea)
        
    
    else:
        level=level+1
        leftarea=adaptive_trapezoidal(f,left,mid,leftarea,maxlevel)
        rightarea=adaptive_trapezoidal(f,mid,right,rightarea,maxlevel)
        area=leftarea+rightarea
        
    return area


# In[6]:


def user_input():
 condtion=True
 while(condtion):
    global level
    level=0
    x = 1 #just fot intiliaziation
    f = F(x)
    print("input a and b")
    a=float(input())
    b=float(input())
    n=1
    h = (b - a) / n
    first = f(a) + f(b)
    sum = 0
    for i in range(1, n):
        sum = sum + f(a + (i * h))
    second = 2 * sum
    area = h * 0.5 * (first + second)
    finallarea=adaptive_trapezoidal(f,a,b,area,1000)
    print("Final area :",finallarea)
    print("number of N is : ", level)
    print("do you want to integrate another function ? yes or no")
    answer=input()
    if answer == "yes":
        condtion=True
    else:
        condtion=False 
   
    
    


# In[ ]:


user_input()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


print


# In[ ]:




