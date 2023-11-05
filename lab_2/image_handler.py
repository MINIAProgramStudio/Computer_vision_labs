import numpy
import cv2
import copy


class ImageContainer:
    def __init__(self, path=None):
        if path != None:  # if path is defined, import the image
            self.path = path
            self.data = cv2.imread(path)

    path = None
    data = []

    def show(self):  # show the image and wait for anykey
        cv2.imshow(self.path, self.data)
        cv2.waitKey(0)

    def save(self):
        cv2.imwrite(self.path, self.data)

    def standardize(self):
        if isinstance(self.data[0], list):
            maximum = float('-inf')
            minimum = float('inf')
            for row in self.data:
                row_max = max(max(row))
                row_min = min(min(row))
                if row_max > maximum: maximum = row_max
                if row_min < minimum: minimum = row_min
            for row in range(len(self.data)):
                for column in range(len(self.data[row])):
                    for color in range(0, 3):
                        self.data[row][column][color] = int(
                            (self.data[row][column][color] + minimum) / ((maximum - minimum) / 255))
        else:
            maximum = float('-inf')
            minimum = float('inf')
            for row in self.data:
                row_max = max(row)
                row_min = min(row)
                if row_max > maximum: maximum = row_max
                if row_min < minimum: minimum = row_min
            for row in range(len(self.data)):
                for pixel in range(len(self.data[row])):
                    self.data[row][pixel] = int((self.data[row][pixel] + minimum) / ((maximum - minimum) / 255))


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
    def __init__(self, matrix):
        self.matrix = matrix

    def apply(self, input_IC):
        if isinstance(input_IC.data[0][0], list):
            pass
        else:
            operation_IC = copy.deepcopy(input_IC)
            operation_IC.path = None
            output_IC = copy.deepcopy(input_IC)
            output_IC.path = None

            original_width = len(operation_IC.data[0])
            matrix_height = len(self.matrix)
            matrix_width = len(self.matrix[0])

            operation_IC.data = numpy.concatenate(([[[0,0,0]] * original_width] * int(
                matrix_height / 2), operation_IC.data))  # add empty rows at top
            operation_IC.data = numpy.concatenate((operation_IC.data, [[[0,0,0]] * original_width] * int(
                matrix_width / 2)))  # add empty rows at bottom

            for row in range(len(operation_IC.data)):
                waiter = numpy.concatenate(([[0,0,0]] * int(matrix_height / 2), operation_IC.data[row]))  # add empty columns at left
                operation_IC.data[row] = numpy.pad(operation_IC.data[row],int(len(operation_IC.data[row]) + matrix_height / 2)*3)
                operation_IC.data[row] = waiter
                operation_IC.data[row] = numpy.concatenate((operation_IC.data[row], [[0] * original_width] * int(
                    matrix_height / 2)))  # add empty columns at right

        for row in range(0, len(input_IC)):
            row += int(matrix_width / 2)
        for column in range(0, len(row)):
            column += int(matrix_height / 2)
        matrix_for_position_sum = 0
        for pos_x in range(-int(matrix_height / 2), int(matrix_height / 2 + 1)):
            for pos_y in range(-int(matrix_width / 2), int(matrix_width / 2 + 1)):
                matrix_for_position_sum += self.matrix[pos_x][pos_y] * operation_IC.data[pos_x + row][
                    pos_y + column]

        output_IC.data[row][column] = matrix_for_position_sum
        output_IC.standardize()
        return output_IC
