import numpy as np
import cv2
import pytesseract

def normalize_img(img):
    norm_img = np.zeros((img.shape[0], img.shape[1]))
    img = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    return img

def read_img(img):
    temp_image = cv2.imread(img)
    return temp_image

def remove_noise(image):
    img = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 15)
    return img

def get_grayscale(image):
    img =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return img
    
def thresholding(image):
    img = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)[1]
    return img

def binarization(image):
    ret, img = cv2.threshold(image, 0, 255,cv2.THRESH_BINARY,cv2.THRESH_OTSU)
    return img

def preprocess_image(img):
    img = read_img(img)
    img = normalize_img(img)
    img = remove_noise(img)
    img = get_grayscale(img)
    #img = thresholding(img)
    #img = binarization(img)
    return img

def img_to_text(img):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    text = pytesseract.image_to_string(img, lang='eng')
    return text