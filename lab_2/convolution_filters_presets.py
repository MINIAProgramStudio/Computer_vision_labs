import image_handler as IH

Right_10_Down_20 = IH.Convolution_filter([[1] + [0] * 18] + [[0] * 10] * 58)

Inversion = IH.Convolution_filter([[-1]])

Gauss_11_Filter = IH.Convolution_filter([[2.210400105835432e-12, 1.989738765536754e-10, 6.5891098500480135e-09,
                                          8.027179095462168e-08, 3.5975320817778996e-07, 5.931327665253336e-07,
                                          3.5975320817778996e-07, 8.027179095462168e-08, 6.5891098500480135e-09,
                                          1.989738765536754e-10, 2.210400105835432e-12],
                                         [1.989738765536754e-10, 1.7911057571106018e-08, 5.931327665253336e-07,
                                          7.22583634609022e-06, 3.238395177632407e-05, 5.339211012295271e-05,
                                          3.238395177632407e-05, 7.22583634609022e-06, 5.931327665253336e-07,
                                          1.7911057571106018e-08, 1.989738765536754e-10],
                                         [6.5891098500480135e-09, 5.931327665253336e-07, 1.9641859634995952e-05,
                                          0.00023928683638032346, 0.0010724091992814686, 0.0017681038577498497,
                                          0.0010724091992814686, 0.00023928683638032346, 1.9641859634995952e-05,
                                          5.931327665253336e-07, 6.5891098500480135e-09],
                                         [8.027179095462168e-08, 7.22583634609022e-06, 0.00023928683638032346,
                                          0.002915110439079131, 0.01306461859364934, 0.02153991456893406,
                                          0.01306461859364934, 0.002915110439079131, 0.00023928683638032346,
                                          7.22583634609022e-06, 8.027179095462168e-08],
                                         [3.5975320817778996e-07, 3.238395177632407e-05, 0.0010724091992814686,
                                          0.01306461859364934, 0.0585515583592937, 0.09653519969960742,
                                          0.0585515583592937, 0.01306461859364934, 0.0010724091992814686,
                                          3.238395177632407e-05, 3.5975320817778996e-07],
                                         [5.931327665253336e-07, 5.339211012295271e-05, 0.0017681038577498497,
                                          0.02153991456893406, 0.09653519969960742, 0.15915963711602737,
                                          0.09653519969960742, 0.02153991456893406, 0.0017681038577498497,
                                          5.339211012295271e-05, 5.931327665253336e-07],
                                         [3.5975320817778996e-07, 3.238395177632407e-05, 0.0010724091992814686,
                                          0.01306461859364934, 0.0585515583592937, 0.09653519969960742,
                                          0.0585515583592937, 0.01306461859364934, 0.0010724091992814686,
                                          3.238395177632407e-05, 3.5975320817778996e-07],
                                         [8.027179095462168e-08, 7.22583634609022e-06, 0.00023928683638032346,
                                          0.002915110439079131, 0.01306461859364934, 0.02153991456893406,
                                          0.01306461859364934, 0.002915110439079131, 0.00023928683638032346,
                                          7.22583634609022e-06, 8.027179095462168e-08],
                                         [6.5891098500480135e-09, 5.931327665253336e-07, 1.9641859634995952e-05,
                                          0.00023928683638032346, 0.0010724091992814686, 0.0017681038577498497,
                                          0.0010724091992814686, 0.00023928683638032346, 1.9641859634995952e-05,
                                          5.931327665253336e-07, 6.5891098500480135e-09],
                                         [1.989738765536754e-10, 1.7911057571106018e-08, 5.931327665253336e-07,
                                          7.22583634609022e-06, 3.238395177632407e-05, 5.339211012295271e-05,
                                          3.238395177632407e-05, 7.22583634609022e-06, 5.931327665253336e-07,
                                          1.7911057571106018e-08, 1.989738765536754e-10],
                                         [2.210400105835432e-12, 1.989738765536754e-10, 6.5891098500480135e-09,
                                          8.027179095462168e-08, 3.5975320817778996e-07, 5.931327665253336e-07,
                                          3.5975320817778996e-07, 8.027179095462168e-08, 6.5891098500480135e-09,
                                          1.989738765536754e-10, 2.210400105835432e-12]])

Moving_diagonal_7 = IH.Convolution_filter([
    [100, 10, 1, 0, 1, 10, 100],
    [10, 100, 10, 1, 10, 100, 10],
    [1, 10, 100, 10, 100, 10, 1],
    [0, 1, 10, 100, 10, 1, 0],
    [1, 10, 100, 10, 100, 10, 1],
    [10, 100, 10, 1, 10, 100, 10],
    [100, 10, 1, 0, 1, 10, 100]
])

Sharpening_3 = IH.Convolution_filter([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], cut=True)

Sobels_Vertical = IH.Convolution_filter([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
], cut=True)

Borderlines = IH.Convolution_filter([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
], cut=True)

iFilter = IH.Convolution_filter([
    [-1, -1, -1, -1, -1],
    [-1, -4, -4, -4, -1],
    [-1, -4, 48, -4, -1],
    [-1, -4, -4, -4, -1],
    [-1, -1, -1, -1, -1]
], cut=True)
