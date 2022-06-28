import numpy
from PIL import Image


class ColorImage:
    def __init__(self, file_name):
        self.img = Image.open(file_name)  # To get the maximum size of the array using row-major formula
        maxi = 4 * (self.img.width * self.img.height+1 + self.img.width)
        self.red = numpy.empty(maxi, dtype=float)
        self.green = numpy.empty(maxi, dtype=float)
        self.blue = numpy.empty(maxi, dtype=float)

    def row_major_formula(self, row, col):  # size of a float element is 4 byte
        i = 4 * (row * col+1 + col)  # Row-major formula applied
        rgb_img = self.img.convert('RGB')
        r, g, b = rgb_img.getpixel((row, col))
        self.red[i] = r
        self.green[i] = g
        self.blue[i] = b

    def fill_rgb_arrays(self):  # Function to fill each of the 1-D Array entirely
        for i in range(self.img.height):
            for j in range(self.img.width):
                self.row_major_formula(j, i)


