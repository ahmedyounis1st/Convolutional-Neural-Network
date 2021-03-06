# -*- coding: utf-8 -*-
"""CNN_flatten_layer_mnist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K1aQokr3nSq1G6gR3ai9g1tjsxhTydp_
"""

from tensorflow import keras
from keras.layers import Input, Dense, Dropout,Conv2D, MaxPooling2D, Flatten
from tensorflow.keras import  datasets
from matplotlib import pyplot as plt

(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()

#Normalize image pixel values.
x_train = x_train/255
x_test = x_test/255

model=keras.Sequential() #Create a network sequence.

model.add(Input(shape=(28,28,1)))
model.add(Flatten())
model.add(Dense(120,activation = 'tanh'))
model.add(Dense(84,activation = 'tanh'))
model.add(Dense(10,activation = 'softmax'))

model.summary()

#model.compile(optimizer='Adam',loss="categorical_crossentropy",metrics=['accuracy']) 
model.compile(optimizer='Adam',loss="sparse_categorical_crossentropy",metrics=['accuracy']) 
results= model.fit(x_train,y_train,epochs=10,batch_size=128,validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test)

y_pred=model.predict(x_test)
y_pred.shape

import numpy as np
from numpy import argmax
y_pred1=argmax(y_pred,axis=1)

from sklearn.metrics import accuracy_score,  confusion_matrix
print(confusion_matrix(y_test,y_pred1))

accuracy_score(y_test,y_pred1)*100

x_test_final=x_test.reshape(-1, 28,28)
plt.imshow(x_test_final[0],cmap="gray")
print(y_pred[0])
print(y_pred1[0])

plt.plot(results.history['accuracy'], label='accuracy')
plt.plot(results.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
#plt.ylim([0.5, 1])
plt.legend(loc='lower right')