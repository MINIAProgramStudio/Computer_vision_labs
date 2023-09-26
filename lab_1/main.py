import numpy
import cv2
import image_handler as IH

Watermelon = IH.ImageContainer("img\watermelon.jpg") #import the image
Watermelon_monochrome = IH.IC_to_monochrome(Watermelon) #monochromatic copy of the image
Watermelon_binary = IH.monochrome_to_binary(Watermelon_monochrome) #binary mask of the image
Watermelon_monochrome.show() #show monochromatic image
Watermelon_binary.show() #show binary mask
Watermelon.show() #show that original image is untouched
