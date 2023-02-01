import cv2 as cv
from PIL import Image
from PIL import ImageDraw

image = cv.imread('path/to/grupseniori.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

face_cascade = cv.CascadeClassifier('path/to/haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('path/to/haarcascade_eye.xml')

#draw a rectangle around the faces
def show_drept(faces):
      for (x,y,w,h) in faces:
            cv.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = image[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                  cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

#detect faces in the image
faces = face_cascade.detectMultiScale(gray, 1.3)
#show how many faces were found
print("Found {0} faces!".format(len(faces)))
#draw a rectangle around the faces
show_drept(faces)
#show time of detection
t1 = cv.getTickCount()
faces = face_cascade.detectMultiScale(gray, 1.3)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("Time of detection: {0} seconds".format(time))

'''#detect faces in the image and show time of execution
faces = face_cascade.detectMultiScale(gray, 1.25, 5)
#show how many faces were found
print("Found {0} faces!".format(len(faces)))
#draw a rectangle around the faces
show_drept(faces)
#show time of detection
t1 = cv.getTickCount()
faces = face_cascade.detectMultiScale(gray, 1.25)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("Time of detection: {0} seconds".format(time))'''


'''faces = face_cascade.detectMultiScale(gray, 1.05)
#show how many faces were found
print("Found {0} faces!".format(len(faces)))
#draw a rectangle around the faces
show_drept(faces)
#show time of detection
t1 = cv.getTickCount()
faces = face_cascade.detectMultiScale(gray, 1.05)
t2 = cv.getTickCount()
time = (t2-t1)/cv.getTickFrequency()
print("Time of detection: {0} seconds".format(time))'''

pil_img=Image.fromarray(gray,mode="L")
drawing=ImageDraw.Draw(pil_img)

cv.imshow('img',image)
#press any key to exit
cv.waitKey(0)
