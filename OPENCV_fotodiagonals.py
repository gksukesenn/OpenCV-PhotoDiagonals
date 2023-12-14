import cv2
import numpy as np

img = cv2.imread("kaynaks2/card.webp")

width,height = 800,800
pts1= np.float32([[481,285],[648,374],[334,548],[511,636]])
pts2= np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Cards",img)
cv2.imshow("Card",imgOutput)

cv2.waitKey(0)