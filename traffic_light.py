import time
import cv2

cascade_src = 'cas1.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)

ta1=20
ta2=20
ta3=20
ta4=20
temp1=10
temp2=10
temp3=10
temp4=10
light_on=0
count1=0
count2=0
count3=0
count4=0

def vehicle_detection1():
    global count1
    count1=0
    img1=cv2.imread('car1.jpg',cv2.IMREAD_GRAYSCALE)

    cars = car_cascade.detectMultiScale(img1, 1.1, 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(img1,(x,y),(x+w,y+h),(0,0,255),2)
        count1=count1+1
    cv2.imshow('img1',img1)
    
    print(count1)
    return count1

def vehicle_detection2():
    global count2
    count2=0
    img2=cv2.imread('car2.jpg',cv2.IMREAD_GRAYSCALE)
    
    cars = car_cascade.detectMultiScale(img2, 1.1, 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(img2,(x,y),(x+w,y+h),(0,0,255),2)
        count2=count2+1
    cv2.imshow('img2',img2)
    print(count2)
    return count2

def vehicle_detection3():
    global count3
    count3=0
    img3=cv2.imread('car3.png',cv2.IMREAD_GRAYSCALE)
    
    cars = car_cascade.detectMultiScale(img3, 1.1, 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(img3,(x,y),(x+w,y+h),(0,0,255),2)
        count3=count3+1
    cv2.imshow('img3',img3)
    print(count3)
    return count3

def vehicle_detection4():
    global count4
    count4=0
    img4=cv2.imread('car4.jpg',cv2.IMREAD_GRAYSCALE)
    
    cars = car_cascade.detectMultiScale(img4, 1.1, 1)
    for (x,y,w,h) in cars:
        cv2.rectangle(img4,(x,y),(x+w,y+h),(0,0,255),2)
        count4=count4+1
    cv2.imshow('img4',img4)
    print(count4)
    return count4

def check():
    global ta1, ta2, ta3, ta4

    if(ta1<20):
        ta1=20
    if(ta2<20):
        ta2=20
    if(ta3<20):
        ta3=20
    if(ta4<20):
        ta4=20
##    
##    print("1st street: ",round(ta1))
##    print("2nd street: ",round(ta2))
##    print("3rd street: ",round(ta3))
##    print("4th street: ",round(ta4))

def maxcount(a1, a2, a3, a4):
    global ta1, ta2, ta3, ta4, temp1, temp2, temp3, temp4
    
    add=a1+a2+a3+a4
    ta1=(a1/add)*360
    ta2=(a2/add)*360
    ta3=(a3/add)*360
    ta4=(a4/add)*360
    temp1=a1
    temp2=a2
    temp3=a3
    temp4=a4
    tadd=360
    check()

def mincount(a1, a2, a3, a4):
    global ta1, ta2, ta3, ta4, temp1, temp2, temp3, temp4
    
    add=a1+a2+a3+a4
    ta1=(a1/add)*80
    ta2=(a2/add)*80
    ta3=(a3/add)*80
    ta4=(a4/add)*80
    temp1=a1
    temp2=a2
    temp3=a3
    temp4=a4
    tadd=80
    check()

def othercount(a11, a21, a31, a41):
    global ta1, ta2, ta3, ta4, temp1, temp2, temp3, temp4
    
    add=a11+a21+a31+a41
    ta1=ta1+((a11-temp1)*4)
    ta2=ta2+((a21-temp2)*4)
    ta3=ta3+((a31-temp3)*4)
    ta4=ta4+((a41-temp4)*4)
    temp1=a11
    temp2=a21
    temp3=a31
    temp4=a41
    tadd=ta1+ta2+ta3+ta4
    if(ta1+ta2+ta3+ta4>360):
        maxcount(a11,a21,a31,a41)
    else:
        check()

def lights():   
    green1=False
    green2=False
    green3=False
    green4=False
    
    global ta1, ta2, ta3, ta4, light_on

    if(light_on==0):
        green1=True
        light_on=light_on+1
        time.sleep(round(ta1)/10)
    elif(light_on==1):
        green2=True
        light_on=light_on+1
        time.sleep(round(ta2)/10)
    elif(light_on==2):
        green3=True
        light_on=light_on+1
        time.sleep(round(ta3)/10)
    elif(light_on==3):
        green4=True
        light_on=0
        time.sleep(round(ta4)/10)
    
    print("1st street: ",green1)
    print("2nd street: ",green2)
    print("3rd street: ",green3)
    print("4th street: ",green4)
    
test=1
while (test!=0):
    a1=vehicle_detection1()
    a2=vehicle_detection2()
    a3=vehicle_detection3()
    a4=vehicle_detection4()
    if(a1>=50 or a2>=50 or a3>=50 or a4>=50):
        maxcount(a1, a2, a3, a4)
    elif(a1+a2+a3+a4<50):
        mincount(a1, a2, a3, a4)
    else:
        othercount(a1, a2, a3, a4)

    lights()
    cv2.destroyAllWindows()

    test=test+1

    
    
