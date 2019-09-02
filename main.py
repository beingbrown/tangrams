import cv2

def get_color_images(input_image):
    high_poly = cv2.imread(input_image)
    # Use Otsu's method here ?
    gray_image = cv2.cvtColor(high_poly, cv2.COLOR_BGR2GRAY)
    ycbcr_image = cv2.cvtColor(high_poly, cv2.COLOR_RGB2YCrCb)
    return high_poly, gray_image, ycbcr_image

def main(*args, **kwargs):
    input_image = kwargs['input_image']
    output_image = kwargs['output_image']
    # handle errors here
