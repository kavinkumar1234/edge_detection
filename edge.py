import cv2
import imutils
import matplotlib

img=cv2.imread(r"C:\Users\Parents Gift\Desktop\roboAI\edge_detect\lane.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayImage", gray_img)
cv2.waitKey(0)

#Canny_1 = cv2.Canny(gray_img, 50,170)
#cv2.imshow("mid",Canny_1)
#cv2.waitKey(0)

#Canny_2 = cv2.Canny(gray_img, 30,150)
#cv2.imshow("low",Canny_2)
#cv2.waitKey(0)

Canny_3 = cv2.Canny(gray_img, 165,170)
cv2.imshow("high",Canny_3)
cv2.imwrite(r"C:\Users\Parents Gift\Desktop\roboAI\edge_detect\canny_lane.jpg",Canny_3)
cv2.waitKey(0)