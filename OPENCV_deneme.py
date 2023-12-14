import cv2
import numpy as np

img = cv2.imread("kaynaks/istockphoto-148421596-612x612.jpg")
print(img.shape)

kernel = np.ones((5,5),np.uint8)

imgResize = cv2.resize(img,(300,200))

imgCropped = img[0:350,300:700]

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)#7,7 sayýlarý hep tek olmalý  3,3     5,5 gibi
imgCanny = cv2.Canny(img,150,200)#kalýnlýk beyazlarýn
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("resize aura",imgResize)
cv2.imshow("aura",img)
cv2.imshow("gray aura",imgGray)
cv2.imshow(" blur aura",imgBlur)
cv2.imshow(" canny aura",imgCanny)
cv2.imshow(" dialation aura",imgDialation)
cv2.imshow("Erode aura",imgEroded)
cv2.imshow("Cropped aura",imgCropped)
cv2.waitKey(0) 

cap = cv2.VideoCapture(0)
cap.set(3,640)#width
cap.set(4,480)#height
cap.set(10,100)#parlaklýðýný deðiþtirir.

while True:#video aslýnda resimlerden oluþtuðu için while kullanýldý.
 success,img=cap.read()
 cv2.imshow("Video",img)
 if cv2.waitKey(1)& 0xFF ==ord('q'):
   break                             