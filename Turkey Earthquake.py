#!/usr/bin/env python
# coding: utf-8

# In[167]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[168]:


df = pd.read_csv(r"C:\\Users\\doguy\\Desktop\\TurkeyEarth\\TurkeyEarthquake.csv", encoding= 'unicode_escape',escapechar="\\",engine="python",sep=';')


# In[169]:


df=df.drop(index=21)


# In[170]:


df.head(25)


# In[171]:


df["Mag."] = [str(x.strip('(Ms)')) if type(x) == str else x for x in df["Mag."]]
df["Mag."] = [str(x.strip('(Mw)')) if type(x) == str else x for x in df["Mag."]]


# In[172]:


df['Casualty'] = df['Casualty'].astype(int)


# In[173]:


plt.figure(figsize = (8  , 10)) 

light = df.loc[df.Casualty < 125].count()[0]
light_medium = df.loc[(df.Casualty >= 125) & (df.Casualty < 150)].count()[0]
medium = df.loc[(df.Casualty >=150) & (df.Casualty < 175)].count()[0]           
medium_heavy = df.loc[(df.Casualty >= 175 ) & (df.Casualty < 200)].count()[0]
heavy = df.loc[df.Casualty > 200].count()[0] 

labels = ['Under 125' , '125 - 150' , '150 , 175' , '175 - 200' , 'Over 200']
plt.style.use('ggplot')
explode = [.1,0,0,0,.1]
weights = [light , light_medium , medium , medium_heavy , heavy]
plt.title("Casualty")

plt.pie(weights , labels = labels , autopct = '%.1f %%' , explode = explode )


# In[174]:


df = df.dropna()


# In[175]:


plt.figure(figsize = (15  , 7)) 

xpoints = df.Date
ypoints = df.Casualty
plt.plot(xpoints, ypoints)
plt.xlabel('Date')
plt.ylabel('Casualty')
plt.show()


# In[220]:


plt.figure(figsize = (8  , 10)) 
blogs = df["Fault Mechanism"]
posts = df["Casualty"]

# Creating a simple bar chart
plt.bar(blogs, posts)

plt.title('Fault Mechanism - Casualty')
plt.xlabel('Fault Mechanism', fontsize=15)
plt.ylabel('Casualty', fontsize=15)
plt.show()


# In[178]:


df = df.drop(["Date","Time","Location"], axis = 1)


# In[182]:


df.dtypes


# In[ ]:


df["Long."] = df["Long."].str.replace(',','.').astype(float)
df["Mag."] = df["Mag."].str.replace(',','.').astype(float)
df["Fault Mechanism"] = [str(x.strip('-slip')) if type(x) == str else x for x in df["Fault Mechanism"]]


# In[188]:


final = Set.drop(["Fault Mechanism","Norma","Reverse","Strike"] , axis = 1)


# In[211]:


final.head(15)


# In[218]:


from sklearn.linear_model import LogisticRegression
reg = LogisticRegression(max_iter = 10000)

X = final.drop('Casualty', axis = 1)
y = final['Casualty']

reg.fit(X , y)
pred = reg.predict([[38,28.40,6.5,4]]) #🗸
score = reg.score(X , y) # %1.0 🗸
print("Succces Rate {}".format(score))
print("Casualty {}".format(pred))


# In[219]:


X.info()


# In[ ]:




