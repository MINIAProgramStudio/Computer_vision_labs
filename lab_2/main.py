import cv2
import image_handler as IH

while True:
    Image = IH.ImageContainer(input("Relative path: ")) #import the image
    Image_monochrome = IH.IC_to_monochrome(Image) #monochromatic copy of the image
    Filter = IH.Convolution_filter([
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ])
    Image_filtered = Filter.apply(Image_monochrome)
    Image_monochrome.show() #show monochromatic image
    Image_filtered.show() #show filtered image

    cv2.destroyAllWindows()