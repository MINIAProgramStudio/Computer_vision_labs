import numpy
import cv2
import image_handler as IH

while True:
    Image = IH.ImageContainer(input("relative path: ")) #import the image
    print("Please wait. Operations may take a while")
    Image_monochrome = IH.IC_to_monochrome(Image) #monochromatic copy of the image
    Image_binary = IH.monochrome_to_binary(Image_monochrome) #binary mask of the image
    Image_mask = IH.mask_cut(Image_binary,Image, negative=True) #cutting out the mask

    Image_monochrome.show() #show monochromatic image
    Image_binary.show() #show binary mask
    Image_mask.show() #sow cut image
    Image.show() #show that original image is untouched

    if input("Do you wish to save masked picture? (Y/N) ") in ["Yes","yes","Y","y"]:
        Image_mask.path = input("input path: ")
        Image_mask.save()