import cv2
pic = cv2.imread('cat.jpg')
pic = cv2.resize(pic, (700, 700), interpolation=cv2.INTER_CUBIC)
cv2.imshow('', pic)
cv2.waitKey(0)
cv2.destroyAllWindows()