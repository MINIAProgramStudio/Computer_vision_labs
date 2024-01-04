import image_handler as IH
import convolution_filters_presets as CFP

while True:
    print("Image path")
    le_image = IH.ImageContainer(input("<<<"))
    le_image.show()

    le_image_sp = IH.sp_noise(le_image)
    le_image_sp.show()

    le_image_sp_box = CFP.BoxAverage.apply(le_image_sp)
    le_image_sp_box.show()

    le_image_sp_median = IH.median_filter(le_image_sp)
    le_image_sp_median.show()

    le_image_nn = IH.norm_noise(le_image,var=50)
    le_image_nn.show()

    le_image_nn_box = CFP.BoxAverage.apply(le_image_nn)
    le_image_nn_box.show()

    le_image_nn_median = IH.median_filter(le_image_nn)
    le_image_nn_median.show()