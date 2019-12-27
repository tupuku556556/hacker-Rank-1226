#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input())
arr = input() 
l = list(map(int,arr.split(' '))) 
l.sort()
res = [] 
for i in l: 
    if i not in res: 
        res.append(i)
print(res[-2])


# In[ ]:




