import cv2
from face import Face
Face = Face()

capture = cv2.VideoCapture(0)
while capture.isOpened():
    ret, frame = capture.read()
    try:
        if ret:
            #detect face
            try:
                coords = Face.face_area(frame)
                
                
                #crop face
                img = Face.crop_face(frame, coords)
                cv2.imshow('Cropped Face', img)
                if cv2.waitKey(1) & 0xFF == 27:
                    break

                for x, y, w, h in coords:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    cv2.imshow('LIVE', frame)
                    if cv2.waitKey(1) & 0xFF == 27:
                        break
            except:
                pass
    except:
        pass

capture.release()
cv2.destroyAllWindows()