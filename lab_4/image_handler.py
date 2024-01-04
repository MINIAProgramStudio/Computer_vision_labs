import numpy
import cv2
import copy
from tqdm import tqdm
import random


class ImageContainer:
    def __init__(self, path=None):
        if path != None:  # if path is defined, import the image
            self.path = path
            self.data = cv2.imread(path).astype('int')

    path = None
    data = []

    def show(self):  # show the image and wait for anykey
        cv2.imshow(self.path, self.data.astype('uint8'))
        cv2.waitKey(0)

    def save(self):
        cv2.imwrite(self.path, self.data)

    def standardize(self):
        maximum = float('-inf')
        minimum = float('inf')
        for row in self.data:
            row_max = numpy.amax(numpy.amax(row))
            row_min = numpy.amin(numpy.amin(row))
            if row_max > maximum: maximum = row_max
            if row_min < minimum: minimum = row_min
        for row in range(len(self.data)):
            for column in range(len(self.data[row])):
                for color in range(0, 3):
                    self.data[row][column][color] = int(
                        (self.data[row][column][color] - minimum) * 255 / (maximum - minimum))

    def cut(self):
        for row in range(len(self.data)):
            for column in range(len(self.data[row])):
                for color in range(0, 3):
                    if self.data[row][column][color] > 255:
                        self.data[row][column][color] = 255
                    elif self.data[row][column][color] < 0:
                        self.data[row][column][color] = 0


def IC_to_monochrome(input_IC):  # create monochromatic copy of an image
    if type(input_IC.data[0][0]) != list or not isinstance(input_IC, ImageContainer):
        Exception("IC_to_monochrome accepts only rgb image containers")
    output_IC = copy.deepcopy(input_IC)  # create copy of an image
    output_IC.path = None  # delete a path of a copy

    pos_y = 0
    for row in output_IC.data:
        pos_x = 0
        for pixel in row:
            output_IC.data[pos_y][pos_x] = int(
                pixel[0] * 0.36 + pixel[1] * 0.53 + pixel[2] * 0.11)  # monochromatic transformation
            pos_x += 1
        pos_y += 1

    return output_IC  # return a monochromatic copy


def monochrome_to_binary(input_IC):
    if type(input_IC.data[0][0]) != int or not isinstance(input_IC, ImageContainer):
        Exception("monochrome_to_binary accepts only monochromatic image containers")
    output_IC = copy.deepcopy(input_IC)  # create copy of an image
    output_IC.path = None  # delete a path of a copy

    if True:
        brightness_graph = [0] * 256
        for row in input_IC.data:
            for pixel in row:
                brightness_graph[pixel[0]] += 1

        total_brightness = sum(brightness_graph)

        brightness_possibility = [0] * 256
        for i in range(0, 255):
            brightness_possibility[i] = brightness_graph[i] / total_brightness

        def q1(t):
            output = sum(brightness_possibility[0:t])
            if output != 0:
                return output
            else:
                return 0.0001

        def q2(t):
            output = sum(brightness_possibility[t + 1:])
            if output != 0:
                return output
            else:
                return 0.0001

        def mu1(t):
            output = 0
            for i in range(0, t):
                output += i * brightness_possibility[i] / q1(t)
            return output

        def mu2(t):
            output = 0
            for i in range(t + 1, 255):
                output += i * brightness_possibility[i] / q2(t)
            return output

        def main_disp(t):
            return q1(t) * q2(t) * ((mu1(t) * mu2(t)) ** 2)

        max_val = -10 ** 10
        t_max = 0
        for t in range(0, 255):
            value = main_disp(t)
            if value > max_val:
                t_max = t
                max_val = value
        pos_y = 0
        for row in output_IC.data:
            pos_x = 0
            for pixel in row:
                if pixel[0] > t_max:
                    output_IC.data[pos_y][pos_x] = 255
                else:
                    output_IC.data[pos_y][pos_x] = 0
                pos_x += 1
            pos_y += 1

        return output_IC


def mask_cut(mask_IC, input_IC, negative=False):
    if type(mask_IC.data[0][0]) != int or not isinstance(input_IC, ImageContainer) or not isinstance(mask_IC,
                                                                                                     ImageContainer):
        Exception("mask_cut accepts only binary image containers for masks and image containers for input_IC")

    if mask_IC.data.size != input_IC.data.size:
        Exception("mask must have the same size and shape as the image")
    output_IC = copy.deepcopy(input_IC)  # create copy of an image
    output_IC.path = None  # delete a path of a copy

    if negative:
        pos_y = 0
        for row in input_IC.data:
            pos_x = 0
            for pixel in row:
                if (mask_IC.data[pos_y][pos_x] == 255).all():
                    output_IC.data[pos_y][pos_x] = [0, 0, 0]
                pos_x += 1
            pos_y += 1
    else:
        pos_y = 0
        for row in input_IC.data:
            pos_x = 0
            for pixel in row:
                if (mask_IC.data[pos_y][pos_x] == 0).all():
                    output_IC.data[pos_y][pos_x] = [0, 0, 0]
                pos_x += 1
            pos_y += 1
    return output_IC


class Convolution_filter:
    def __init__(self, matrix, cut = False):
        self.matrix = matrix
        self.sum = 0
        self.cut = cut
        for i in range(len(matrix)):
            for ii in range(len(matrix[i])):
                self.sum+=self.matrix[i][ii]

    def apply(self, input_IC):
        if isinstance(input_IC.data[0][0], list):
            pass
        else:
            operation_IC = copy.deepcopy(input_IC)
            operation_IC.path = None
            output_IC = copy.deepcopy(input_IC)
            output_IC.path = None
            original_height = int(len(output_IC.data))
            original_width = int(len(output_IC.data[0]))
            matrix_height = len(self.matrix)
            matrix_width = len(self.matrix[0])

            operation_IC.data = numpy.pad(operation_IC.data, (
            (int(matrix_height / 2), int(matrix_height / 2) + 1), (int(matrix_width / 2), int(matrix_width / 2) + 1),
            (0, 0)), mode='constant')
        for row in tqdm(range(0, original_height)):
            row = row + int(matrix_height / 2)
            for column in range(0, original_width):
                column = column + int(matrix_width / 2)
                matrix_for_position = []

                for pos_y in range(-int(matrix_height / 2), int(matrix_height / 2 + 1)):
                    for pos_x in range(-int(matrix_width / 2), int(matrix_width / 2 + 1)):
                        matrix_for_position.append(self.matrix[pos_y][pos_x] * operation_IC.data[pos_y + row][
                            pos_x + column])
                output_IC.data[row - int(matrix_height / 2)][column - int(matrix_width / 2)] = sum(matrix_for_position)
        if self.cut:
            output_IC.cut()
        else:
            output_IC.standardize()
        return output_IC


class Morfological_Operation:
    def __init__(self, matrix, pos, fit = False, negative = False):
        self.matrix = matrix
        self.pos = pos
        self.fit = fit
        self.negative = negative

    def apply(self, input_IC):
        if isinstance(input_IC.data[0][0], list):
            pass
        else:
            operation_IC = copy.deepcopy(input_IC)
            operation_IC.path = None
            output_IC = copy.deepcopy(input_IC)
            output_IC.data = numpy.zeros((len(operation_IC.data)-len(self.matrix)+1,
                                          len(operation_IC.data[0]) - len(self.matrix[0]) + 1,
                                          3))
            if self.negative:
                if self.fit:
                    for row in tqdm(range(self.pos[0], len(operation_IC.data))):
                        for column in range(self.pos[1], len(operation_IC.data[0])):
                            fit = True
                            for pos_y in range(0, len(self.matrix)):
                                for pos_x in range(0, len(self.matrix[0])):
                                    if (operation_IC.data[row+pos_y-self.pos[1]-1][column+pos_x-self.pos[0]-1] <= [127,127,127]).all() and self.matrix[pos_y][pos_x]:
                                        fit = False
                            if fit:
                                output_IC.data[row - len(self.matrix) + 1][column - len(self.matrix[0]) + 1] = [0,
                                                                                                                0,
                                                                                                                0]
                            else:
                                output_IC.data[row - len(self.matrix) + 1][column - len(self.matrix[0]) + 1] = [255, 255,255]
                else:
                    for row in tqdm(range(self.pos[0], len(operation_IC.data))):
                        for column in range(self.pos[1], len(operation_IC.data[0])):
                            hit = False
                            for pos_y in range(0, len(self.matrix)):
                                for pos_x in range(0, len(self.matrix[0])):
                                    if (operation_IC.data[row+pos_y-self.pos[1]-1][column+pos_x-self.pos[0]-1] >= [127,127,127]).all() and self.matrix[pos_y][pos_x]:
                                        hit = True
                                        break
                                if hit:
                                    break
                            if hit:
                                output_IC.data[row - len(self.matrix) + 1][column - len(self.matrix[0]) + 1] = [0,
                                                                                                                0,
                                                                                                                0]
                            else:
                                output_IC.data[row - len(self.matrix) + 1][column - len(self.matrix[0]) + 1] = [255, 255, 255]
            else:
                if self.fit:
                    for row in tqdm(range(self.pos[0], len(operation_IC.data))):
                        for column in range(self.pos[1], len(operation_IC.data[0])):
                            fit = True
                            for pos_y in range(0, len(self.matrix)):
                                for pos_x in range(0, len(self.matrix[0])):
                                    if (operation_IC.data[row+pos_y-self.pos[1]-1][column+pos_x-self.pos[0]-1] <= [127,127,127]).all() and self.matrix[pos_y][pos_x]:
                                        fit = False
                                        break
                                if not fit: break
                            if fit:
                                output_IC.data[row - len(self.matrix) + 1][column - len(self.matrix[0]) + 1] = [255,
                                                                                                                255,
                                                                                                                255]
                            else:
                                output_IC.data[row - len(self.matrix) + 1][column - len(self.matrix[0]) + 1] = [0, 0, 0]
                else:
                    for row in tqdm(range(self.pos[0],len(operation_IC.data))):
                        for column in range(self.pos[1], len(operation_IC.data[0])):
                            hit = False
                            for pos_y in range(0, len(self.matrix)):
                                for pos_x in range(0, len(self.matrix[0])):
                                    if (operation_IC.data[row+pos_y-self.pos[1]-1][column+pos_x-self.pos[0]-1] >= [127,127,127]).all() and self.matrix[pos_y][pos_x]:
                                        hit = True
                                        break
                                if hit:
                                    break
                            if hit:
                                output_IC.data[row - len(self.matrix)+1][column - len(self.matrix[0]) + 1]=[255,255,255]
                            else:
                                output_IC.data[row - len(self.matrix) + 1][column - len(self.matrix[0]) + 1] = [0,0,0]
        return output_IC

def sp_noise(input_IC, prob = 0.03, white = [255,255,255], black = [0,0,0]):
    output_IC = copy.deepcopy(input_IC)
    output_IC.path = ""
    tres = 1-prob
    for i in range(len(input_IC.data)):
        for ii in range(len(input_IC.data[0])):
            rand = random.random()
            if rand < prob:
                output_IC.data[i][ii] = white
            elif rand > tres:
                output_IC.data[i][ii] = black
    return output_IC

def norm_noise(input_IC, mean = 0, var=0.1, a=0.5):
    output_IC = copy.deepcopy(input_IC)
    output_IC.path = ""
    sigma = var**0.5
    size_1, size_2 = len(input_IC.data), len(input_IC.data[0])
    gauss = numpy.random.normal(mean, sigma, (size_1,size_2, 3))
    gauss = gauss.reshape(size_1, size_2, 3)
    noisy = output_IC.data*a + (1-a)*gauss
    output_IC.data = noisy
    output_IC.standardize()
    return output_IC

def median_filter(input_IC, size = 3):
    if size%2==0 or size<1 or not isinstance(size,int):
        raise Exception("size must be odd positive integer")
    output_IC = copy.deepcopy(input_IC)
    output_IC.path = ""
    margin = int((size-1)/2)
    median_pos = int(size**2/2)
    for row in tqdm(range(margin,len(input_IC.data)-margin)):
        for column in range(margin, len(input_IC.data[0])-margin):
            pixels = []
            for pos_y in range(-margin,margin+1):
                for pos_x in range(-margin,margin+1):
                    pixels.append(input_IC.data[row+pos_y][column+pos_x])
            pixels = sorted(pixels, key = sum)
            output_IC.data[row][column] = pixels[median_pos]
    return output_IC

