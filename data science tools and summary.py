#!/usr/bin/env python
# coding: utf-8

# In[5]:


#In this notebook, Data Science Tools and Ecosystem are summarized.


# In[6]:


datasciencelanguages=["1.c-language","2.rlanguae","3.sql"]
print(datasciencelanguages)


# In[7]:


dslibraries=["scrapy","beautifulsoup","numpy","scipy"]
print(dslibraries)


# In[8]:


pip install tabulate


# In[9]:


# import module
from tabulate import tabulate

# assign data
mydata = [
	["tablue"],
	["matlab"],
	["apache spark"],
	["msexcel"]
]

# create header
head = ["dstools"]

# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))


# In[10]:


#Below are a few examples of evaluating arithmetic expressions in Python


# In[11]:


#This a simple arithmetic expression to mutiply then add integers.
(3*4)+5


# In[12]:


total_minutes = 200

# Get hours with floor division
hours = total_minutes // 60

# Get additional minutes with modulus
minutes = total_minutes % 60

# Create time as a string
time = "{}:{}".format(hours, minutes)

print(time)


# In[13]:


objectives = ["tools for datascinece", "arthematic operations", "table of tools"]
print(objectives)


# In[ ]:




