import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

a = input('Please Enter Your Addres Image : ')

img = cv2.imread(a) # Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4) # Detect faces
for (x, y, w, h) in faces: # Draw rectangle around the faces
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imshow('img', img) # Display the output
b = cv2.imwrite('imge.jpg', img)
b
print(b)
cv2.waitKey()
