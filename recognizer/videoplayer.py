import cv2 as cv
import numpy as np
import time
detector = cv.CascadeClassifier('')
cap = cv.VideoCapture('')


while True:
#    读取摄像头当前这一帧的画面  ret:True fase image:当前这一帧画面
    ret,image = cap.read()
#   图片灰度处理
    gray = cv.cvtColor(image,cv.COLOR_RGB2GRAY)
#   检查人脸
    faces=detector.detectMultiScale(gray, 1.3, 5)
#   标记人脸
    for (x,y,w,h) in faces:
        #矩形标记
        cv.rectangle(image,(x,y),(x+w,y+h),(255,30,30),2)
        #显示图片
        print(faces)
        cv.putText(image, 'the cat', (x, y + h), cv.FONT_HERSHEY_COMPLEX, 0.55, (0, 255, 0), 1)
    cv.imshow("faces in video",image)
        #暂停窗口
    if cv.waitKey(5) & 0xFF ==ord('q'):
        break
cap.release()
cv.destroyAllWindows()
exit()