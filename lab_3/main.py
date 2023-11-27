import cv2
import image_handler as IH
import morfological_presets as MP
import convolution_filters_presets as CFP
import numpy

while True:
    print("Please select a picture to filter.")
    Image = IH.ImageContainer(input("Relative path: >>>")) #import the image
    print("Please wait: image is being preprocessed")
    Image_monochrome = IH.IC_to_monochrome(Image)
    Image_binary = IH.monochrome_to_binary(Image_monochrome)
    while True:
        print("Close the binary image to proceed")
        Image_binary.show()
        cv2.destroyAllWindows()
        print("True pixels must be white")
        print("Do you want to invert the image? (Y/N)")
        if input(">>>").lower() in ["y", "yes"]:
            Image_binary = CFP.Inversion.apply(Image_binary)
        else:
            break
    print("Please select operation:")
    print("0 -- Nothing")
    print("1 -- Erosion")
    print("2 -- Dilation")
    print("3 -- Closing")
    print("4 -- Opening")
    print("5 -- Borderlines")
    match input(">>>"):
        case "0": Image_filtered = MP.test.apply(Image_binary)
        case "1": Image_filtered = MP.Erosion.apply(Image_binary)
        case "2": Image_filtered = MP.Dilation.apply(Image_binary)
        case "3": Image_filtered = MP.Erosion.apply(MP.Dilation.apply(Image_binary))
        case "4": Image_filtered = MP.Dilation.apply(MP.Erosion.apply(Image_binary))
        case "5":
            Image_filtered = MP.Dilation.apply(Image_binary)
            Image_filtered.data = Image_filtered.data - MP.Erosion.apply(Image_binary).data
        case _:Image_filtered = MP.test.apply(Image_binary)
    print("Filter applied. Close the picture to proceed")
    Image_filtered.show()#show filtered image
    print("Do you want to save the result? (Y/N)")
    if input(">>>").lower() in ["y","yes"]:
        Image_filtered.path = input("Relative path: >>>")
        Image_filtered.save()
    cv2.destroyAllWindows()
    print("--------------")