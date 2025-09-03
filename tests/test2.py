import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
plt.ion()  # interactive mode

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Emal
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    plt.imshow(gray, cmap='gray')
    plt.pause(0.001)
    plt.clf()  # clear previous frame
