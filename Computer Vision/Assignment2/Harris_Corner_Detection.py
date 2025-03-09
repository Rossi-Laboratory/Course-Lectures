import matplotlib.pyplot as plt
import numpy as np
import cv2
%matplotlib inline

from scipy import ndimage

def gaussian_smooth(size, sigma=1):
    ########################################################################
    # TODO:                                                                #
    #   Perform the Gaussian Smoothing                                     #
    #   Input: window size, sigma                                          #
    #   Output: smoothing image                                            #
    ########################################################################

    ########################################################################
    #                                                                      #
    #                           End of your code                           #
    #                                                                      # 
    ########################################################################
    return img

from scipy.ndimage.filters import convolve
img_filtered_K5 = convolve(img_Gray, gaussian_smooth(size=5,sigma=5))
img_filtered_K10 = convolve(img_Gray, gaussian_smooth(size=10,sigma=5))

def sobel_edge_detection(im):
    ########################################################################
    # TODO:                                                                #
    #   Perform the sobel edge detection                                   #
    #   Input: image after smoothing                                       #
    #   Output: the magnitude and direction of gradient                    #
    ########################################################################

    ########################################################################
    #                                                                      #
    #                           End of your code                           #
    #                                                                      # 
    ########################################################################
    return  (gradient_magnitude, gradient_direction)


def structure_tensor(gradient_magnitude, gradient_direction, k):
    ########################################################################
    # TODO:                                                                #
    #   Perform the cornermess response                                    #
    #   Input: gradient_magnitude, gradient_direction                      #
    #   Output: second-moment matrix of Structure Tensor                   #
    ########################################################################

    ########################################################################
    #                                                                      #
    #                           End of your code                           #
    #                                                                      # 
    ########################################################################
    return  StructureTensor

def NMS(harrisim,window_size=30,threshold=0.1):
    ########################################################################
    # TODO:                                                                #
    #   Perform the Non-Maximum Suppression                                #
    #   Input: Structure Tensor, window size, threshold                    #
    #   Output: filtered coordinators                                      #
    ########################################################################

    ########################################################################
    #                                                                      #
    #                           End of your code                           #
    #                                                                      # 
    ########################################################################
    return filtered_coords

def plot_harris_points(image,filtered_coords):
    plt.figure()
    plt.gray()
    plt.figure(figsize=(20,10))
    plt.imshow(image)
    plt.plot([p[1] for p in filtered_coords],[p[0]for p in filtered_coords],'+')
    plt.axis('off')
    plt.show()
    
def rotate(image, angle, center = None, scale = 1.0):

    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    return rotated