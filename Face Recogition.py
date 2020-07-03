import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_alt.xml')
# Read the input image


img = cv2.imread('salah.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)



for (x, y , w ,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 500 , 333), 1)
    cv2.putText(img,'salah', (x, y), 5, 2, (222, 209, 244), 2, cv2.LINE_AA)
    # Display the output
cv2.imshow('img', img)
cv2.waitKey()

