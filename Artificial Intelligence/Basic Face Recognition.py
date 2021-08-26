# Basic face detection AI program
import cv2 #imports opencv (the computer vision library)

#pre trained data from opencv github 
face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #premade opencv machine for front faces

# Assign image (s) to variable
image = cv2.imread('<insert image name>')
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # converts image to black and white (grayscale)

#face detection 
face_coor = face_data.detectMultiScale(grayscale) #determine the coordinates of the rectangle surrounding the face

# Draw out rectangles around the face
for x, y, w, h in face_coor:  #stores indivigual coordinates of face
    cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,30), 2) #Coordinates of face, rgb colour code and thickness of the line 


#show image
cv2.imshow('Face detector', image) #names window and tells program to show the image 
cv2.waitKey() # prevents program from closing right away in terminal


print("Program complete")
