import cv2
import image_handler as IH
import convolution_filters_presets as CFP
import numpy

while True:
    Image = IH.ImageContainer(input("Relative path: ")) #import the image

    Image_filtered = CFP.iFilter.apply(Image)
    Image_borders = CFP.Borderlines.apply(Image)
    Image_filtered.show()#show filtered image
    Image_borders.show()
    #cv2.destroyAllWindows()