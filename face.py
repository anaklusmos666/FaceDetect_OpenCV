import cv2
#import time

class Face:
    def __init__(self):
        self.haarcascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def face_area(self, frame):
        #print('-----', frame.shape)
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cascade = self.haarcascade
        faces = cascade.detectMultiScale(img_gray)
        return faces

    def crop_face(self, frame, coords):
        print(frame.shape)
        for x, y, w, h in coords:
            crop_img = frame[y:(y+w), x:(x+h)]
        return crop_img