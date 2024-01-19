import cv2
#import numpy as np
import datetime as dt

cap=cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    date_time=str(dt.datetime.now())
    frame=cv2.putText(frame,date_time,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2,cv2.LINE_AA)
    frame=cv2.putText(frame,"ANOUSHKA GOEL",(200,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),4)
    cv2.imshow("Video",frame)
    if cv2.waitKey(0)==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


# cap = cv2.VideoCapture(0)
# while True:
#     ret,frame = cap.read()
#     cv2.imshow("webcam",frame)
#     if cv2.waitKey(1)==ord("q"):
#         break
#
# print(frame.shape)
# cap.release()
# cv2.destroyAllWindows()
#
# cv2.putText(frame,"ANOUSHKA GOEL",(200,100),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),10)