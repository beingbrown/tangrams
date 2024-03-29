import sys
import cv2
import numpy as np
from math import hypot

def distance(p, q):
    return hypot(p[0] - q[0], p[1] - q[1])

def get_color_images(input_image):
    high_poly = cv2.imread(input_image)
    gray_image = cv2.cvtColor(high_poly, cv2.COLOR_BGR2GRAY)
    ycbcr_image = cv2.cvtColor(high_poly, cv2.COLOR_RGB2YCrCb)
    return high_poly, gray_image, ycbcr_image

def create_output_image(final_image, out_location):
    if final_image is not None:
        cv2.imwrite(out_location, final_image)
    return final_image

def main(*args, **kwargs):
    input_image = kwargs['input_image']
    output_image = kwargs['output_image']
    # handle errors here

# invoked with tangrams input_image output_image
if __name__ == '__main__':
    high, low, ycbcr = get_color_images(sys.argv[1])
    ycbcr = ycbcr[:, :, 0]
#    blur = cv2.GaussianBlur(ycbcr,(5,5),0)
    blur = cv2.GaussianBlur(ycbcr,(0,0),1)
    upper_thresh,img = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    edges = cv2.Canny(ycbcr, upper_thresh * 0.5, upper_thresh)
    vertices = np.transpose(np.nonzero(edges))
