import numpy
import cv2
import copy

class ImageContainer:
    def __init__(self,path=None):
        if path != None: #if path is defined, import the image
            self.path = path
            self.data = cv2.imread(path)
    path = None
    data = []

    def show(self): #show the image and wait for anykey
        cv2.imshow(self.path, self.data)
        cv2.waitKey(0)

def IC_to_monochrome(input_IC): #create monochromatic copy of an image
    output_IC=copy.deepcopy(input_IC) #create copy of an image
    output_IC.path=None #delete a path of a copy
    pos_y = 0
    for row in output_IC.data:
        pos_x = 0
        for pixel in row:
            output_IC.data[pos_y][pos_x] = pixel[0]*0.36+pixel[1]*0.53+pixel[2]*0.11 #monochromatic transformation
            pos_x+=1
        pos_y+=1
    return output_IC #return a monochromatic copy