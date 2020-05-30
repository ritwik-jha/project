values = open('newaccuracy.txt').read().split('\n')



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
                           

accuracy=[]                       
for i in range(len(x)-1):
    accuracy.append(x[i][0])


