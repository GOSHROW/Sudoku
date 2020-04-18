import cv2
import numpy as np
import matplotlib.pyplot as plt
import keras

def order_points(pts):
    rect = np.zeros((4, 2), dtype = "float32")
    s = pts.sum(axis = 1)
    # print(s)

    rect[2] = pts[np.argmax(s)]
    rect[0] = pts[np.argmin(s)]
    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def four_point_transform(image, pts):
    # This function has been taken from https://www.pyimagesearch.com/2014/08/25/4-point-opencv-getperspective-transform-example/ 
	rect = order_points(pts)
	(tl, tr, br, bl) = rect
	widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
	widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
	maxWidth = max(int(widthA), int(widthB))
	heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
	heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
	maxHeight = max(int(heightA), int(heightB))
	dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")
	M = cv2.getPerspectiveTransform(rect, dst)
	warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
	return warped

def preprocess(path):
    imgPath = path
    img = cv2.imread(imgPath, 0)
    blurimg = cv2.bilateralFilter(img, 7, 25, 25)
    # blurimg = cv2.GaussianBlur(img, (5, 5), 7)
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
        
        epsilon = 0.1*cv2.arcLength(c,True)
        approx = cv2.approxPolyDP(c,epsilon,True)
        # print(approx, type(approx))

        warped = four_point_transform(output, approx.sum(axis = 1))
    
    di = (900, 900)     # assuming that all common sudokus are just 9 x 9
    resized = cv2.resize(warped, di, interpolation = cv2.INTER_AREA)
    return resized

def digit_extract(path):
    image = preprocess(path)
    im = []
    for i in range(0, 900, 100):
        for j in range(0, 900, 100):
            im.append(image[i + 5 : i + 95, j + 5 : j + 95])
    for i, e in enumerate(im):
        im[i] = cv2.resize(e, (28, 28), interpolation = cv2.INTER_AREA)
    return im

def recognizer():
    model = keras.models.load_model("GOSHROWDigitClassifier.h5")
    # print(model.summary)
    obt = digit_extract(path = 'sudoku.jpg')
    dim = 9
    SudokuIdentified = []
    helperAr = [0] * 81

    for i, e in enumerate(obt):
        # if i % dim == 0 :
        #     SudokuIdentified.append(helperAr)
        #     helperAr = []
        e = cv2.bitwise_not(e)
        if cv2.countNonZero(e[10 : 19, 10 : 19]) >= 10:
            IMG = e.reshape((1, 28, 28, 1))
            pred = model.predict(IMG)
            pred = pred.tolist()
            print(pred)
            ind = pred[0].index(max(pred[0]))
            cv2.imshow(str(i) + str(ind), e)
            cv2.waitKey(600)
            helperAr[i] = (int(str(ind)))

    SudokuIdentified = helperAr
    return SudokuIdentified

s = recognizer()
print(s)