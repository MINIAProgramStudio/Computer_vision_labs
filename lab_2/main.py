import cv2
import image_handler as IH
import numpy

while True:
    Image = IH.ImageContainer(input("Relative path: ")) #import the image
    Filter = IH.Convolution_filter([
        [1, 2, 4, 8, 16, 32, 16, 8, 4, 2, 1],
        [2, 4, 8, 16, 32, 64, 32, 8, 4, 2, 1],
        [4, 8, 16, 32, 64, 128, 64, 32, 16, 8, 4],
        [8, 16, 32, 64, 128, 256, 128, 64, 32, 16, 8],
        [16, 32, 64, 128, 256, 512, 256, 128, 64, 32, 16],
        [8, 16, 32, 64, 128, 256, 128, 64, 32, 16, 8],
        [4, 8, 16, 32, 64, 128, 64, 32, 8, 4],
        [2, 4, 8, 16, 32, 64, 32, 8, 4, 2, 1],
        [1, 2, 4, 8, 16, 32, 16, 8, 4, 2, 1]
    ])
    Image_filtered = Filter.apply(Image)
    Image_filtered.standardize()
    Image_filtered.show()#show filtered image
    #cv2.destroyAllWindows()