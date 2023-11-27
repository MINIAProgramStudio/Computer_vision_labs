import cv2
import image_handler as IH
import convolution_filters_presets as CFP
import numpy

while True:
    print("Please select a picture to filter.")
    Image = IH.ImageContainer(input("Relative path: >>>")) #import the image
    print("Select filter:")
    print("1 -- Move 10 20")
    print("2 -- Inversion")
    print("3 -- Gauss' 11x11")
    print("4 -- Diagonal 7x7")
    print("5 -- Sharpening")
    print("6 -- Sobel's vertical")
    print("7 -- Borderlines")
    print("8 -- My filter")
    selection = input(">>>")
    match selection:
        case "1": Image_filtered = CFP.Right_10_Down_20.apply(Image)
        case "2": Image_filtered = CFP.Inversion.apply(Image)
        case "3": Image_filtered = CFP.Gauss_11_Filter.apply(Image)
        case "4": Image_filtered = CFP.Moving_diagonal_7.apply(Image)
        case "5": Image_filtered = CFP.Sharpening_3.apply(Image)
        case "6": Image_filtered = CFP.Sobels_Vertical.apply(Image)
        case "7": Image_filtered = CFP.Borderlines.apply(Image)
        case "8": Image_filtered = CFP.iFilter.apply(Image)
        case _: continue
    print("Filter applied. Please wait a moment while picture is loading to your definitively beautiful screen")
    Image_filtered.show()#show filtered image
    print("Do you want to save the result? (Y/N)")
    if input(">>>").lower() in ["y","n","yes","no"]:
        Image_filtered.path = input("Relative path: >>>")
        Image_filtered.save()
    cv2.destroyAllWindows()
    print("--------------")