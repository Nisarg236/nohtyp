import cv2
import numpy as np
import mouse

frame = None
roiPts = []
inputMode = False

width=1920
height=1080
dim=(width,height)

def selectROI(event, x, y, flags, param):
    global frame, roiPts, inputMode
    if inputMode and event == cv2.EVENT_LBUTTONDOWN and len(roiPts) < 4:
        roiPts.append((x, y))
        cv2.circle(frame, (x, y), 4, (0, 255, 0), 2)
        cv2.imshow("frame", frame)


cap = cv2.VideoCapture(0)
cv2.namedWindow("frame")
cv2.setMouseCallback("frame", selectROI)
termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
roiBox = None
while True:
    _, frame = cap.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,dim,interpolation=cv2.INTER_AREA)
    if roiBox is not None:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
        backProj = cv2.calcBackProject([hsv], [0], roiHist, [0, 180], 1)
        (r, roiBox) = cv2.CamShift(backProj, roiBox, termination)
        pts = np.int0(cv2.boxPoints(r))
        cv2.polylines(frame, [pts], True, (0, 255, 0), 2)
        p1=pts[0]
        p2=pts[1]
        p3=pts[2]
        p4=pts[3]

        center=(p1+p2+p3+p4)/4
        cv2.circle(frame, (int(center[0]), int(center[1])), 4, (0, 0, 255), 2)
        mouse.move(center[0],center[1],absolute=True,duration=0.0)
            
    cv2.imshow("frame", frame)
    key = cv2.waitKey(50) & 0xFF
    if key == ord("i") and len(roiPts) < 4:
        inputMode = True
        orig = frame.copy()
        while len(roiPts) < 4:
            cv2.imshow("frame", frame)
            cv2.waitKey(0)
        roiPts = np.array(roiPts)
        s = roiPts.sum(axis = 1)
        tl = roiPts[np.argmin(s)]
        br = roiPts[np.argmax(s)]
        roi = orig[tl[1]:br[1], tl[0]:br[0]]
        roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        roiHist = cv2.calcHist([roi], [0], None, [180], [0, 180])
        roiHist = cv2.normalize(roiHist, roiHist, 0, 255, cv2.NORM_MINMAX)
        roiBox = (tl[0], tl[1], br[0], br[1])

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
