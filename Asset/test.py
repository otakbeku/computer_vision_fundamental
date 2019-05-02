import cv2
import numpy as np

image = cv2.imread('gambar.jpg')


def gray_average(image: np.ndarray):
    temp = np.zeros(image.shape[:2], dtype=np.uint8)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            temp[y,x] = sum(e for e in image[y,x])/3
    return temp

def gray_lightness(image: np.ndarray):
    temp = np.zeros(image.shape[:2], dtype=np.uint8)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            temp[y,x] = (np.max(image[y,x])+np.min(image[y,x]))/2
    return temp


def gray_luminosity(image: np.ndarray):
    temp = np.zeros(image.shape[:2], dtype=np.uint8)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            temp[y,x] = (image[y,x,0]*0.07)+(image[y,x,1]*0.72)+(image[y,x,2]*0.21)
    return temp

def gray_opencv(image: np.ndarray):
    temp = np.zeros(image.shape[:2], dtype=np.uint8)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            temp[y,x] = (image[y,x,0]*0.114)+(image[y,x,1]*0.587)+(image[y,x,2]*0.299)
    return temp

gray_avg = gray_average(image)
gray_l = gray_lightness(image)
gray_lumi = gray_luminosity(image)
gray_op = gray_opencv(image)

cv2.imshow('gray avg', gray_avg)
cv2.imshow('gray lightness', gray_l)
cv2.imshow('gray luminos', gray_lumi)
cv2.imshow('gray opencv', gray_op)
cv2.waitKey()