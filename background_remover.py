import cv2
#import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation 


cap = cv2.VideoCapture(0)
cap.set(3,648)
cap.set(4,488)

segmentor = SelfiSegmentation()

while True:
    sucess, img = cap.read()
    
    img_out = segmentor.removeBG(img,(125,0,125),threshold=0.8)
    
    cv2.imshow("image",img)
    cv2.imshow("img_out",img_out)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()    
cv2.destroyAllWindows()
    
