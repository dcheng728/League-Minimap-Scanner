# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:33:00 2019

@author: dchen
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import numpy as np
#from tensorflow.keras import datasets, layers, models
from tensorflow import keras

class_names = ['ashe','blitzcrank','brand','caitlyn','cassiopeia','darius','drmundo','ezreal','fiddlestick',
               'garen','graves','jax','karthus','kayle','malphite','nasus','nidalee','renekton','ryze','shen',
               'sivir','soraka','tristana','trundle','udyr','vladimir','warwick','wukong','ziggs','zilean','zyra']


"""
train_images = np.load("numpy_saves/3dtrain_images_2424.npy")
train_labels = np.load("numpy_saves/3dtrain_labels_2424.npy")
test_images = np.load("numpy_saves/3dtest_images_2424.npy")
test_labels = np.load("numpy_saves/3dtest_labels_2424.npy")






#i = train_images[0]

assert not np.any(np.isnan(train_images))
assert not np.any(np.isnan(test_images))

# Normalize pixel values to be between 0 and 1
train_images, test_images = train_images / 255.0, test_images / 255.0

i = train_images[0]

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(24, 24,3)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(32,kernel_regularizer=keras.regularizers.l2(0.001), activation='relu'))
model.add(keras.layers.Dense(31, activation='softmax'))


model.summary()

model.compile(optimizer= "Adam",
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])





history = model.fit(train_images, train_labels, epochs=20)




test_loss, test_acc = model.evaluate(test_images, test_labels)

print(test_acc)
print(history)

model.save('model/my_model.h5')
"""