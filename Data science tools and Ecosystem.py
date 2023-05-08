#!/usr/bin/env python
# coding: utf-8

# In[5]:


#In this notebook, Data Science Tools and Ecosystem are summarized.


# In[17]:


a="Some popular Data science Languages are"
print(a)
datasciencelanguages=["1.c-language","2.rlanguae","3.sql","4.scala","5.java script","6.php","7.Go"]
list(map(print,datasciencelanguages))


# In[18]:


a="Some Of the Popular Data Science Libraries are:"
print(a)
dslibraries=["pandas","seaborn","numpy","scipy","keras","Tensor flow"]
list(map(print,dslibraries))


# In[8]:


pip install tabulate


# In[19]:


a="Data science tools"
print(a)
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


# In[22]:


a="objectives"
print(a)
objectives = ["1.Add comments to code cell", "2.Create markdown cells", "3.How to use tools","4.An ordered and unordered list","5.format markdown cell with heading styles"]
list(map(print,objectives))


# In[28]:


a="AUTHORS"
authors="sathya prakash"
print(a)
print(authors)


# In[ ]:




