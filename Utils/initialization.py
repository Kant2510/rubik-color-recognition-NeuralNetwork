import Utils.process as process
import Utils.Base64ToImage as bti
import cv2
import numpy as np


def intialization(name):
    image = bti.stringToImage(name)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # xu ly hinh anh thanh ma tran
    image_matrix = np.array(image_rgb)
    image_matrix_split = process.split_matrix(image_matrix)

    # create input
    input = []
    for co in range(9):
        sum = np.array([[0, 0, 0]])
        for ii in range(25, image_matrix_split[co].shape[0] - 25):
            for jj in range(25, image_matrix_split[co].shape[1] - 25):
                sum += image_matrix_split[co][ii][jj]
        input.append(np.round(
            sum / ((image_matrix_split[co].shape[0] - 50)*(image_matrix_split[co].shape[1] - 50)))[0])

    return np.array(input)
