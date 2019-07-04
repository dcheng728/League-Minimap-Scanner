# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 18:10:42 2019

@author: dchen
"""

from PIL import ImageGrab
from PIL import Image
import cv2
import numpy as np
import Processing
import tensorflow as tf
import time

#Shapes of the League of Legends Minimap, adjust to fit your screen
width = 275
height = 275
"""
define the box to crop the minimap
        (x1,y1)
             ________________________
            |                        |
            |                        |
            |                        |
            |                        |
            |        Minimap         |
            |                        |
            |                        |
            |                        |
            |                        |
            |________________________|
                                   (x2,y2)
"""    
x1 = 1645
y1 = 805
x2 = 1920
y2 = 1080

fps = 10

model_path = "model/v 1.0.0.h5"

class_names = ['ashe','blitzcrank','brand','caitlyn','cassiopeia','darius','drmundo','ezreal','fiddlestick',
               'garen','graves','jax','karthus','kayle','malphite','nasus','nidalee','renekton','ryze','shen',
               'sivir','soraka','tristana','trundle','udyr','vladimir','warwick','wukong','ziggs','zilean','zyra']




def getimg():
    image = ImageGrab.grab((1645,805,1920,1080))
    image_array = np.array(image)
    image_bgr = cv2.cvtColor(image_array,cv2.COLOR_RGB2BGR)
    #processed = photo2vid.process(image_bgr)
    #resized = cv2.resize(processed, (width,height)) 
    return image_bgr



def main():
    scanner = Processing.League_Scanner(model_path)
    img = getimg()
    while True:
        img = getimg()
        img = Processing.process(img,scanner)
        cv2.imshow("",img)
        cv2.waitKey(int(1000/fps))


if __name__ == '__main__':
    main()

    
    
    
    
    
    
    
    
    
    
    