# i will put my code in github
# check the links below
import cv2
import handtracker as ht

Cwidth, Cheight = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, Cwidth)
cap.set(4, Cheight)
detector = ht.handTracker()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPos(img)
    # oh sorry :)
    if len(lmList) != 0:
        fingers = detector.fingersUp()
        nfinger = fingers.count(1)
        print(nfinger)
        cv2.putText(img, f'you are showing {nfinger} fingers', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow('img', img)
    cv2.waitKey(1)
