import image_handler as IH
import convolution_filters_presets as CFP

le_image = IH.ImageContainer("input/1.png")
IH.sp_noise(le_image).show()