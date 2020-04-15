import cv2
import numpy as np
import matplotlib.pyplot as plt

imgPath = '../Downloads/sudoku.jpg'
img = cv2.imread(imgPath, 0)
blurimg = cv2.bilateralFilter(img, 7, 25, 25)
blurimg = cv2.GaussianBlur(img, (5, 5), 7)
blurimg = cv2.adaptiveThreshold(blurimg, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2) 
blurimg = cv2.bitwise_not(blurimg)

detector = cv2.SimpleBlobDetector_create()
keypoints = detector.detect(blurimg)
im_with_keypoints = cv2.drawKeypoints(blurimg, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

im2, contours, hierarchy = cv2.findContours(blurimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
output = blurimg.copy()

if len(contours) != 0:
    cv2.drawContours(output, contours, -1, 255, 3)
    c = max(contours, key = cv2.contourArea)
    
    x,y,w,h = cv2.boundingRect(c)
    # cv2.rectangle(output,(x,y),(x+w,y+h),(100,90,0),2)
    letter = output[y:y+h,x:x+w]
    print(letter)
    cv2.drawContours(output, contours, -1, 255, 3)
    c = max(contours, key = cv2.contourArea)

    xxx, yyy = [], []
    for i in c:
        for j in i:
            xxx.append(j[0])
            yyy.append(j[1])
    
    xxx = np.asarray(xxx)
    yyy = np.asarray(yyy)

    print(yyy, xxx)
    plt.plot(xxx, yyy)
    plt.show()

cv2.imshow("Keypoints", letter)
cv2.waitKey(0)