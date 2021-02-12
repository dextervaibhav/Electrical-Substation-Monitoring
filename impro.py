from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt1
from matplotlib import pyplot as plt2

img = cv2.imread('inputimg.png')
img4 = cv2.imread('rcb.png',0)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray.png', gray_image)

img1 = cv2.imread('gray.png',0)

img2 = cv2.imread('gray.png',0)

height,width = img1.shape[:2]

for i in range(height):
    for j in range(width):
        if img2[i,j]<220:
            img2[i,j]=0


for i in range(height):
    for j in range(width):
        print(img2[i,j],end=" ")
    print()

cv2.imshow("RGBimage",img4)

cv2.imshow("actualimage",img)

cv2.imshow("unprocessed",img1)

cv2.imwrite("unprocessed.png",img1)

cv2.imshow("prcessed",img2)

cv2.imwrite('processed.png',img2)


histr = cv2.calcHist([img],[0],None,[256],[0,256])
plt.figure(figsize=(4,3))
plt.plot(histr)
plt.title("Input Image Histogram")
plt.show()


histr = cv2.calcHist([img1],[0],None,[256],[0,256])
plt.figure(figsize=(4,3))
plt.plot(histr)
plt.title("Gray Scale Image Histogram")
plt.show()


histr = cv2.calcHist([img2],[0],None,[256],[0,256])
plt.figure(figsize=(4,3))
plt.plot(histr)
plt.title("Processed Image Histogram")
plt.show()




""""
img3 = cv2.imread('processed.png')
img3 = cv2.resize(img3,(400,500))
gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret,gray = cv2.threshold(gray,200,200,0)
gray2 = gray.copy()
mask = np.zeros(gray.shape,np.uint8)

contours, hier = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    if 200<cv2.contourArea(cnt)<5000:
        cv2.drawContours(img,[cnt],0,(0,255,0),2)
        cv2.drawContours(mask,[cnt],0,255,-1)



cv2.imshow("contours",img3)
"""

cv2.waitKey(0)


