
import cv2

cascade_src = 'cas1.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)

count1=0
img1=cv2.imread('car2.jpg',cv2.IMREAD_GRAYSCALE)

cars = car_cascade.detectMultiScale(img1, 1.1, 1)
print(cars)
for (x,y,w,h) in cars:
    cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),2)
    count1=count1+1
cv2.imshow('img1',img1)
print(count1)
