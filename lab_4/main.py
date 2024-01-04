import image_handler as IH
import convolution_filters_presets as CFP

while True:
    print("Image path")
    le_image = IH.ImageContainer(input("<<<"))
    le_image.show()

    le_image_sp = IH.sp_noise(le_image)
    le_image_sp.show()
    le_image_sp.path = "output/sp.png"
    le_image_sp.save()

<<<<<<< Updated upstream
    le_image_nn = IH.norm_noise(le_image,var=50)
    le_image_nn.show()
=======
    le_image_sp_box = CFP.BoxAverage.apply(le_image_sp)
    le_image_sp_box.show()
    le_image_sp_box.path = "output/sp_box.png"
    le_image_sp_box.save()

    le_image_sp_median = IH.median_filter(le_image_sp)
    le_image_sp_median.show()
    le_image_sp_median.path = "output/sp_median.png"
    le_image_sp_median.save()

    le_image_sp_w_median = IH.w_median_filter(le_image_sp)
    le_image_sp_w_median.show()
    le_image_sp_w_median.path = "output/sp_w_median.png"
    le_image_sp_w_median.save()

    le_image_sp_box = CFP.BoxAverage.apply(le_image_sp)
    le_image_sp_box.show()

    le_image_sp_median = IH.median_filter(le_image_sp)
    le_image_sp_median.show()

    le_image_nn = IH.norm_noise(le_image,var=50)
    le_image_nn.show()
<<<<<<< HEAD
    le_image_nn.path = "output/nn.png"
    le_image_nn.save()

    le_image_nn_box = CFP.BoxAverage.apply(le_image_nn)
    le_image_nn_box.show()
    le_image_nn_box.path = "output/nn_box.png"
    le_image_nn_box.save()

    le_image_nn_median = IH.median_filter(le_image_nn)
    le_image_nn_median.show()
    le_image_nn_median.path = "output/nn_median.png"
    le_image_nn_median.save()

    le_image_nn_w_median = IH.w_median_filter(le_image_nn)
    le_image_nn_w_median.show()
    le_image_nn_w_median.path = "output/nn_w_median.png"
    le_image_nn_w_median.save()
>>>>>>> Stashed changes
=======

    le_image_nn_box = CFP.BoxAverage.apply(le_image_nn)
    le_image_nn_box.show()

    le_image_nn_median = IH.median_filter(le_image_nn)
    le_image_nn_median.show()
>>>>>>> 23ab6a33ca573b9087b8d07e01388d7322f54993
