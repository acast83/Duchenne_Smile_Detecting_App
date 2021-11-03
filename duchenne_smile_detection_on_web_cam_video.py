import cv2
import time                        
face_cascade = cv2.CascadeClassifier('cascade.xml' )   

video = cv2.VideoCapture(0)          
                                                    

while True:                          
    check, frame = video.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    
    #face detecting method
    faces=face_cascade.detectMultiScale(gray_img, 
    scaleFactor =1.05,                    
    minNeighbors = 5)              
    
 
    for x,y,w,h in faces :
        frame = cv2.rectangle(
            frame,                #source
            (x,y),              #upper right corner of the rectangle
            (x+w, y+h),         #lower left corner of the rectangle
            (0,255,0),          # rectangle color
            3)                     #line width


    cv2.imshow('window', frame)
    key = cv2.waitKey(1)          #one frame per milisecond
    if key == ord('q'):     #exits if We press q
        break

video.release()
cv2.destroyAllWindows