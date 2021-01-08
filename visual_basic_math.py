from hackattic import *
# import cv2

from PIL import Image
import pytesseract
# sudo apt-get install tesseract-ocr
import argparse
import cv2 # pip install opencv-python
import os
import numpy as np


CHALLENGE = 'visual_basic_math'
# https://hackattic.com/challenges/visual_basic_math

'''References:

NOT USEFUL:
Install tesseract
https://www.pyimagesearch.com/2017/07/03/installing-tesseract-for-ocr/

General reference:
https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/

'''


def fill():
    img = cv2.imread("temp/original.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ## Threshold 
    ret, threshed = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)

    ## FindContours
    cnts, hiers = cv2.findContours(threshed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]

    canvas = np.zeros_like(img)
    n = len(cnts)
    hiers = hiers[0]

    for i in range(n):
        if hiers[i][3] != -1:
            ## If is inside, the continue 
            continue
        ## draw 
        cv2.drawContours(canvas, cnts, i,  (255,255,255), -1, cv2.LINE_AA)

        ## Find all inner contours and draw 
        ch = hiers[i][2]
        while ch!=-1:
            # print(" {:02} {}".format(ch, hiers[ch]))
            cv2.drawContours(canvas, cnts, ch, (255,255,255), -1, cv2.LINE_AA)
            ch = hiers[ch][0]


    cv2.imwrite(f'./temp/filled.png', (255-canvas))
    os.system("cp ~/Hackattic/temp/filled.png /mnt/c/Users/Usuario/Downloads/")


def find():
    # load the example image and convert it to grayscale
    img = cv2.imread('./temp/filled.png')
    orig = cv2.imread("temp/original.png")

    (h, w) = img.shape[:2]
    image_size = h*w
    mser = cv2.MSER_create()
    mser.setMaxArea(image_size//8)
    mser.setMinArea(30)

    filtered = cv2.medianBlur(img, 5)

    gray = cv2.cvtColor(filtered, cv2.COLOR_BGR2GRAY) #Converting to GrayScale
    _, bw = cv2.threshold(gray, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    regions, rects = mser.detectRegions(bw)


    # sort the rectangles
    mean_H = h/(8*2)
    rects_sorted = sorted(rects, key=lambda a: ((a[1]/2+a[3]/2)//mean_H)*100000000 + a[0])

    # With the rects you can e.g. crop the letters
    for i, (x, y, w, h) in enumerate(rects_sorted):
        cv2.rectangle(orig, (x, y), (x+w, y+h), color=(255, 0, 255), thickness=1)
        cv2.putText(orig, str(i), (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (36,255,12), 1)

    cv2.imwrite('./temp/found.png', orig)
    os.system("cp ~/Hackattic/temp/found.png /mnt/c/Users/Usuario/Downloads/")

    return rects_sorted


def read(rectangles):
    img = cv2.imread("temp/original.png")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    margin = 8

    # With the rects you can e.g. crop the letters
    for i, (x, y, w, h) in enumerate(rectangles):
        crop_img = gray[y-margin:y+h+margin, x-margin:x+w+margin]
        text = pytesseract.image_to_string(crop_img, config="--psm 10 --oem 3 -c tessedit_char_blacklist=Ssgq")
        print(text.strip(), end='')
        if i==7:
            # print('--------------------')
            # print('--------------------')
            break

    cv2.imwrite('./temp/crop.png', crop_img)
    os.system("cp ~/Hackattic/temp/crop.png /mnt/c/Users/Usuario/Downloads/")


def main(token):
    # Data of the challenge to a dict
    challenge_dict = data_request(CHALLENGE, token)

    image = "temp/original.png"

    # Get the file URL
    image_url = challenge_dict['image_url']
    image_request(image_url, image_name=image)
    os.system("cp ~/Hackattic/temp/original.png /mnt/c/Users/Usuario/Downloads/")

    fill()

    find()

    # face_tiles = face_detect("faces.png")

    # # Solution POST
    # return solution_post(CHALLENGE, token,  {"result": result})
    

def test():
    fill()
    rectangles = find()
    read(rectangles)


if __name__ == "__main__":
    # Token filename
    # token = read_token("token.config")
    # main(token)

    test()
