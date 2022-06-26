import cv2
filePath = 'luffy.PNG'
image = cv2.imread(filePath, 1)
cv2.imshow("monkey", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
