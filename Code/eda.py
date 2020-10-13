import numpy as np
import pandas as pd
import cv2
import os
import re
import matplotlib.pyplot as plt
#%matplotlib inline


CARDBOARD = 1
GLASS = 2
METAL = 3
PAPER = 4
PLASTIC = 5
TRASH = 6
IMAGE_WIDTH=128
IMAGE_HEIGHT=128
IMAGE_SIZE=(IMAGE_WIDTH, IMAGE_HEIGHT)
IMAGE_CHANNELS=3
path='./test2'

def create_ds(path):
    categories = []
    ImgArray = []
    name = []

    for p in os.listdir(path):
        name.append(p)
        category = re.findall(r'(\w+?)(\d+)', p)[0][0]
        if category == 'cardboard':
            categories.append(CARDBOARD)
        elif category == 'glass':
            categories.append(GLASS)
        elif category == 'metal':
            categories.append(METAL)
        elif category == 'paper':
            categories.append(PAPER)
        elif category == 'plastic':
            categories.append(PLASTIC)
        else:
            categories.append(TRASH)
        img_array = cv2.imread(os.path.join(path, p), cv2.IMREAD_GRAYSCALE)
        #cv2.imshow(p, img_array)
        #cv2.waitKey(0)
        resizedimg_array = cv2.resize(img_array, dsize=(IMAGE_WIDTH, IMAGE_HEIGHT))
        #cv2.imshow(p, resizedimg_array)
        #cv2.waitKey(0)
        ImgArray.append(resizedimg_array)

    df = pd.DataFrame(name, columns=['Name'])
    df['Category'] = categories
    df['Array'] = ImgArray
    print(df.head(10))

    return (df)


df = create_ds(path)

df.head()