import image_handler as IH

test = IH.Morfological_Operation([[True]],(0,0))

Erosion = IH.Morfological_Operation([
    [True, True, True],
    [True, True, True],
    [True, True, True]
], (1,1), fit = True)

Dilation = IH.Morfological_Operation([
    [True, True, True],
    [True, True, True],
    [True, True, True]
], (1,1))
