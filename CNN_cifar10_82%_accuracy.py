# -*- coding: utf-8 -*-
"""CNN_cifar10_82%_accuracy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iUyol-OcfyiQScsUydIuUFP1K3e8Q3CK
"""

from tensorflow import keras
from keras.layers import Input, Dense, Dropout,Conv2D, MaxPooling2D, Flatten
from tensorflow.keras import  datasets
from matplotlib import pyplot as plt

(x_train, y_train), (x_test, y_test) = datasets.cifar10.load_data()

x_train.shape

x_test.shape

#Convert the labels into one-hot codes.
num_classes = 10
y_test1=y_test
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
print(y_train[0])

#Normalize image pixel values.
x_train = x_train/255
x_test = x_test/255

model = keras.Sequential()
    # The first two layers with 32 filters of window size 3x3
model.add(Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(32,32,3)))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

     


model.summary()

model.compile(optimizer='Adam',loss="categorical_crossentropy",metrics=['accuracy']) 
#model.compile(optimizer=keras.optimizers.Adam(),loss="categorical_crossentropy",metrics=['accuracy']) 
results= model.fit(x_train,y_train,epochs=50,batch_size=128,shuffle='true',validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test)

y_pred=model.predict(x_test)
y_pred.shape

import numpy as np
from numpy import argmax
y_pred1=argmax(y_pred,axis=1)

print(y_pred[10])

print(y_pred1[10])

from sklearn.metrics import accuracy_score,  confusion_matrix
print(confusion_matrix(y_test1,y_pred1))
accuracy_score(y_test1,y_pred1)*100

plt.imshow(x_test[502],cmap="gray")

print(y_test1[502])
print(y_pred[502])
print(y_pred1[502])

plt.plot(results.history['accuracy'], label='accuracy')
plt.plot(results.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
#plt.ylim([0.5, 1])
plt.legend(loc='lower right')

plt.plot(results.history['loss'])
plt.title('Training losses')
plt.xlabel('epoch')
plt.ylabel('Training losses')

import matplotlib.pyplot as plt
plt.plot(results.history['accuracy'])
plt.ylabel('Training  accuracy')
plt.xlabel('epoch')

import matplotlib.pyplot as plt
plt.plot(results.history['val_accuracy'])
plt.ylabel(' Validation accuracy')
plt.xlabel('epoch')