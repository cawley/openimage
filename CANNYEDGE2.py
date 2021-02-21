import cv2

image = cv2.imread("salahpic.jpeg", 0)
cv2.imwrite("canny.jpg",	cv2.Canny(image,100,200))
cv2.imshow("canny",	cv2.imread("canny.jpg"))
cv2.imshow("Original Image", image)
cv2.waitKey()
cv2.destroyAllWindows()
