// AUTHOR: Vanshika
// Python3 Concept: Breast Cancer Detection System
// GITHUB: https://github.com/Vanshika-11

//Add your python3 concept below

# In[1]:


import pandas as pd
import numpy as np

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler


# In[2]:


data=load_breast_cancer()


# In[3]:


data


# In[4]:


data.keys()


# In[5]:


data['DESCR']


# In[6]:


print(data['DESCR'])

#569 tumors each having 30 attributes


# In[7]:


print(data['frame'])


# In[8]:


print(data['target_names'])


# In[9]:


print(data['target'])

# 0=malignant  (cancerous)
# 1=benign     (non - cancerous)


# In[10]:


print(data['data'])


# In[11]:


print(data['data'][0])      #values of first tumor


# In[12]:


data['data'].shape


# 569 tumors each having 30 features.
# Each tumor has a target , either 0 or 1. Means if any tumor has target=0,it is malignant and if any tumor has target=1,it is benign


# In[13]:


print(data['feature_names'])
print(len(data['feature_names']))


# In[14]:


j = 0
for i in data['feature_names']:
  print(i,":",data['data'][568][j])
  j+=1

#values and features of 568th tumor


# In[15]:


feature=data['data']
feature

#attributes of each tumor


# In[16]:


label=data['target']
label

# target or label =  malignant or benign


# In[17]:


feature.shape


# In[18]:


label.shape


# In[19]:


print(data['DESCR'])

# here if we observe that min and max values are very much varied, some have small range and some have a very wide range 

# As for area attribute, range is very high , but if we look for  concave points , range is very small

# So we need to rearrange all the values in a particular range, so that every row is having only a particular range


# In[20]:


# Standardising the data

scale = StandardScaler()

feature = scale.fit_transform(feature)
print(feature)


# In[21]:


# Comparing before and after standardisation
# For first tumor

j = 0
for i in data['feature_names']:
  print(i,":",data['data'][568][j])
  j+=1

    
print('------------------------AFTER-----------------------------------------')

j = 0
for i in data['feature_names']:
  print(i,":",feature[0][j])
  j+=1

    


# In[22]:


# We will pass these features to the neural network and will get '0' or '1' as output


# In[23]:


print(feature[568])
print(data['target_names'][label[568]],label[568])


# In[24]:


df= pd.DataFrame(feature,columns=data['feature_names'])


# In[25]:


df


# In[26]:



df_features= pd.DataFrame(feature , columns = data['feature_names'])
df_label = pd.DataFrame(label , columns = ['label'])
df = pd.concat([df_features, df_label], axis=1)

df


# In[27]:



#500 Training
X_train = feature[:500]
y_train = label[:500]

#35 Validation
X_val = feature[500:535]
y_val = label[500:535]

#34 Testing
X_test = feature[535:]
y_test = label[535:]


# In[28]:


# neural network

from keras.models import Sequential
from keras.layers import Dense


# In[49]:


model=Sequential()

model.add(Dense(15, activation='relu',input_dim=30))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])


# In[53]:


model.fit(X_train,y_train,batch_size=1,epochs=5,validation_data=(X_val,y_val))


# In[54]:


model.evaluate(X_test,y_test)


# In[55]:


#Predictions
sample=X_test[0]


# In[56]:


sample


# In[58]:


sample.shape


# In[62]:


import numpy as np

sample=np.reshape(sample, (1,30))
sample.shape


# In[68]:


model.predict(sample)[0][0]


# In[69]:


if model.predict(sample)[0][0]>0.5:
    print("Benign")
else:
    print("Malignant")


# In[76]:


print("-------------Predicted vs actual value---------------")
for i in range(100):
    sample=X_test[i]
    sample=np.reshape(sample, (1,30))
    
    if model.predict(sample)[0][0]>0.5:
        print("-Benign")
    else:
        print("-Malignant")
        
    if y_test[i]==0:
        print("*Malignant")
    else:
        print("*Benign")
        
    print("----------------------------")


# In[ ]:


#df=df.sample(frac=1) to shuffle the dataset

