#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"C:\Users\Milanjyoti\Desktop\cars.csv")


# In[3]:


data


# In[4]:


data.head(5)


# In[7]:


data.shape


# In[8]:


data.isnull()


# In[17]:


data.isnull().sum()


# In[20]:


data.fillna(data.mean(),inplace= True)


# In[21]:


data.isnull().sum()


# In[23]:


make_counts = data["Make"].value_counts()


# In[24]:


make_counts


# In[25]:


asia_europe_df = data[(data["Origin"]=="Asia") | (data["Origin"]=="Europe")]


# In[27]:


asia_europe_df


# In[28]:


#increase all values  of "MPG_City" column by 3
data["MPG_City"] +=3


# In[29]:


data[data["Weight"]<= 4000]


# In[30]:


data


# In[34]:


data["Cylinders"].fillna(data["Cylinders"].mean(),inplace = True)


# In[ ]:




