import cv2,time
video=cv2.VideoCapture(0)
check,frame=video.read()
print(check)
print(frame)
cv2.imshow("Capturing",frame)
keycv2.waitKey(0)
video.release()
