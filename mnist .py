#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras.models import Sequential


# In[2]:


from keras.layers import Dense , Conv2D , Flatten , MaxPooling2D


# In[3]:


from keras.optimizers import adam


# In[4]:


model = Sequential()


# In[5]:


from keras.datasets import mnist


# In[6]:


dataset = mnist.load_data()


# In[7]:


train , test = dataset


# In[8]:


X_train , y_train = train


# In[9]:


X_test , y_test = test


# In[10]:


X_test.shape


# In[11]:


X_train=X_train.reshape(60000,28,28,1)
X_test=X_test.reshape(10000,28,28,1)


# In[12]:


from keras.utils import np_utils


# In[13]:


y_train=np_utils.to_categorical(y_train)
y_test=np_utils.to_categorical(y_test)


# In[14]:


model.add(Conv2D(filters=10,
                kernel_size=(3,3),
                activation='relu',
                input_shape=(28,28,1)))


# In[15]:


model.add(MaxPooling2D(pool_size=(2,2)))


# In[16]:


model.add(Flatten())


# In[20]:


model.add(Dense(units=64,activation='relu'))


# In[21]:


model.add(Dense(units=32,
               activation='relu'))


# In[22]:


model.add(Dense(units=16,
               activation='relu'))


# In[23]:


model.add(Dense(units=10,
               activation='softmax'))


# In[25]:


model.compile(optimizer='adam',
             loss='categorical_crossentropy',
             metrics = ['accuracy'])


# In[26]:


model.fit(X_train , y_train,
         epochs=20,
         validation_data=(X_test,y_test))


# In[32]:


score=model.evaluate(X_train , y_train)


# In[33]:


accuracy=score[1]


# In[ 34]:

print(accuracy)




