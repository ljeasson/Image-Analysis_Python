# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 10:51:41 2017
@author: ljeas

Spirit Animal User ID: creativeBison
Date: 3/23/17
Challenge 3

Sources:
    Python: Working with Pixels
    http://www.csc.villanova.edu/~map/1040/lab12/lab12.pdf
    
    Basic Image Analysis
    https://john.cs.olemiss.edu/~jones/doku.php?id=csci343_image_analysis
    
    Calculating Standard Deviation Step by Step
    https://www.khanacademy.org/math/probability/data-distributions-a1/summarizing-spread-distributions/a/calculating-standard-deviation-step-by-step
"""
#Imports
from __future__ import division
from PIL import Image
import matplotlib.pyplot as mplot
import numpy as np
import os

def standard_deviation(list):
    #Imports image directory
    images = os.listdir("rebelmrkt")
    
    #Creates standard deviation list and image count variable
    std = []
    img_count = 0
    
    #Standard Deviation calculation
    for i in range(0,len(images)):
        if "jpg" in images[i]:
            img = Image.open("rebelmrkt/"+images[i])
            img = np.float32(img)
            img_count += 1
            
            try:
                std += (img - np.mean(list)) ** 2
            except:
                std = (img - np.mean(list)) ** 2
            
    std = (std / img_count) ** 0.5
    
    #Image Conversion
    std = std.clip(0,255)
    std = np.uint8(std)      
          
    return std

def Average_Image(threshold):
    #Imports image directory
    images = os.listdir("rebelmrkt")

    #Creates average image list and file count variable
    avg_image = []
    file_count = 0
    
    #Average Image
    for i in range(0,len(images)):
        if "jpg" in images[i]:
            img = Image.open("rebelmrkt/"+images[i])
            img = np.float32(img)
            file_count += 1
            
            try:
                avg_image += img
            except:
                avg_image=img
            
    avg_image /= file_count

    std = standard_deviation(avg_image)
    
    #Change pixel color to red if standard deviation is greater than threshold
    for row in range(0, len(avg_image)):
        for column in range(0, len(avg_image[row])):
           red = std[row][column][0]
           green = std[row][column][1] 
           blue = std[row][column][2]
           
           color_sum = float(red) + float(green) + float(blue)
           #color_avg = int(color_sum / 3)
           
           if color_sum > float(threshold):
               avg_image[row][column][0] = 255.0
               avg_image[row][column][1] = 0.0
               avg_image[row][column][2] = 0.0
 
    
    #Image Conversion
    avg_image = avg_image.clip(0,255)
    avg_image = np.uint8(avg_image)
    
    #Plot
    mplot.imshow(avg_image)
    mplot.show()
    
    print("DONE")
        
##############################################################################

#Prompt user input
print("Enter an Image Threshold (0-255)")
threshold = input()

while int(threshold) < 0 or int(threshold) > 255:
    print("Invalid Threshold")
    threshold = input()
    
Average_Image(threshold)
