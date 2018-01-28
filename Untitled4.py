
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_boston


# In[6]:


boston = load_boston()


# In[7]:


boston


# In[14]:


df_x= pd.DataFrame(boston.data,columns = boston.feature_names)


# In[15]:


df_y= pd.DataFrame(boston.target)


# In[16]:


reg = linear_model.LinearRegression()


# In[17]:


df_x.describe()


# In[19]:


x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)


# In[20]:


x_train.head()


# In[21]:


y_train.head()


# In[22]:


reg.fit(x_train,y_train)


# In[24]:


a= reg.predict(x_test)


# In[25]:


a


# In[26]:


a[0]


# In[28]:


y_test


# In[29]:


np.mean((a-y_test)**2)

