# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 19:33:27 2019

@author: Davidson Cheng
"""

import os
import cv2
import numpy as np
import tensorflow as tf


#Class names for each supporting champion, their placement in this list coorresponds to the output of the CNN
class_names = ['ashe','blitzcrank','brand','caitlyn','cassiopeia','darius','drmundo','ezreal','fiddlestick',
               'garen','graves','jax','karthus','kayle','malphite','nasus','nidalee','renekton','ryze','shen',
               'sivir','soraka','tristana','trundle','udyr','vladimir','warwick','wukong','ziggs','zilean','zyra']


    
# Class to initialize the Tensorflow Keras Sequential model  
# format:   XXXX = League_Scanner(path_of_model)
class League_Scanner:
    def __init__(self,path):
        self.path = path
        self.model = tf.keras.models.load_model(path)

    def predict(self,imagelist):
        prediction = self.model.predict(imagelist)
        print(prediction.shape)
        output = [np.argmax(prediction[n]) for n in range(prediction.shape[0])]
        return output

# Main function to process the image, called by function in liveidentify.py
def process(image,league_scanner):
    
    """
    An image of minimap ---> a numpy array of champions image with dimension 24*24
    """
    champion_list = []
    coords = []
    b,g,r = cv2.split(image)
    inranger = cv2.inRange(r,120,255)
    inrangeg = cv2.inRange(g,120,255)
    inrangeb = cv2.inRange(b,120,255)
    induction = inranger - inrangeg - inrangeb

    circles = cv2.HoughCircles(induction,cv2.HOUGH_GRADIENT,1,10,param1 = 30,param2 =15,minRadius = 9, maxRadius = 30)
    if(circles is not None):
        for n in range(circles.shape[1]):
            x = int(circles[0][n][0])
            y = int(circles[0][n][1])
            coords.append([x,y])
            radius = int(circles[0][n][2])
            cropped = image[y-radius:y+radius,x-radius:x+radius].copy()
            to_append = cv2.resize(cropped,(24,24))
            champion_list.append(to_append)
            cv2.rectangle(image,(x-radius,y-radius),(x+radius,y+radius),(255,255,255),1)
        champion_list = np.stack(champion_list,axis = 0,)
        champion_list = champion_list.reshape((champion_list.shape[0], 24, 24, 3))
        champion_list_text = league_scanner.predict(champion_list)
        for n in range(len(champion_list_text)):
            cv2.putText(image,class_names[champion_list_text[n]],(coords[n][0]-12,coords[n][1]-12), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),1)
    else:
        image = image
    return image



