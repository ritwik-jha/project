#!/usr/bin/env python
# coding: utf-8

# In[1]:


fil = open('filter.txt').read().split('\n')

kernel = open('kernel_size.txt').read().split('\n')

lr = open('lr.txt').read().split('\n')

maxpool = open('maxpool.txt').read().split('\n')

unit1 = open('unit1.txt').read().split('\n')

unit2 = open('unit2.txt').read().split('\n')

unit3 = open('unit3.txt').read().split('\n')


# In[9]:


from keras.models import Sequential
from keras.layers import Dense , Conv2D , Flatten , MaxPooling2D
from keras.optimizers import adam





from keras.datasets import mnist


dataset = mnist.load_data()


train , test = dataset


X_train , y_train = train


X_test , y_test = test


X_test.shape


X_train=X_train.reshape(60000,28,28,1)
X_test=X_test.reshape(10000,28,28,1)


from keras.utils import np_utils

y_train=np_utils.to_categorical(y_train)
y_test=np_utils.to_categorical(y_test)

x = []

for a in range(len(fil)-1):
    for b in range(len(kernel)-1):
        for c in range(len(lr)-1):
            for d in range(len(maxpool)-1):
                for e in range(len(unit1)-1):
                    for f in range(len(unit2)-1):
                        for g in range(len(unit3)-1):
                            
                            model = Sequential()

                            model.add(Conv2D(filters=int(fil[a]),
                            kernel_size=eval(kernel[b]),
                            activation='relu',
                            input_shape=(28,28,1)))


                            model.add(MaxPooling2D(pool_size=eval(maxpool[d])))


                            model.add(Flatten())


                            model.add(Dense(units=int(unit1[e]),activation='relu'))


                            model.add(Dense(units=int(unit2[f]),
                                            activation='relu'))


                            model.add(Dense(units=int(unit3[g]),
                                            activation='relu'))


                            model.add(Dense(units=10,
                                           activation='softmax'))


                            model.compile(optimizer='adam',
                                         loss='categorical_crossentropy',
                                         metrics = ['accuracy'])


                            model.fit(X_train , y_train,
                                     epochs=2,
                                     validation_data=(X_test,y_test))

                            score=model.evaluate(X_train , y_train)


                            accuracy=score[1]
                            x.append(list(accuracy*100 , 'filter= '+fil[a] , 'kernel_size= '+kernel[b], 
                                          'pool_size= '+maxpool[d] ,
                                  'neuron_no.1= '+unit1[e],'neuron_no.2= '+unit2[f]
                                 ,'neuron_no.3= '+ unit3[g]))


                            

with open('newaccuracy.txt' , 'w') as f:
    for items in x:
        f.write("%s\n"%items)
        



# In[ ]:




