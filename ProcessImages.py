import numpy as np
import cv2
import glob
import os

CurDir = os.getcwd()
FileNames = glob.glob(CurDir + "/" + "Test_image*.png")
FileNames.sort(key=lambda x: os.path.getmtime(x))

print CurDir

for i in FileNames:
    img = cv2.imread(i,0)
    print i, img.max(), img.min(), np.median(img)

