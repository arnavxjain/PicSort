import cv2
import numpy as np
import time
import os

t1 = os.listdir("Assets")
t2 = []
t3 = []
t4 = []
t5 = []
tDel = []
DESKTOP_14 = (1080, 1920, 3)

for eacht1 in t1:
    loopedImg1 = cv2.imread(f"Assets/{eacht1}")
    t2.append(loopedImg1)

# for each in t2:
#     cv2.imshow("frame", each)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

for eacht2 in t2:
    loopedImg2 = cv2.cvtColor(eacht2, cv2.COLOR_BGR2RGB)
    t3.append(loopedImg2)

for eacht3 in t3:
    loopedImg3 = cv2.resize(eacht3, (1000, 650))
    loopedImg3 = cv2.cvtColor(loopedImg3, cv2.COLOR_BGR2RGB)
    t4.append(loopedImg3)
    t5 = t4

def verifyUnique(imageSrc):
    for i in range(len(t5)):
        difference = cv2.subtract(imageSrc, t5[i])
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return False
        else:
            return True


for x in range(len(t4)):
    imageInCheck = t4[x]
    # if verifyUnique(imageInCheck):
    #     tDel.append(imageInCheck)
    #     print(len(tDel))
    if not verifyUnique(imageInCheck):
        os.remove(f"Assets/{t1[x]}")

# for eachDel in tDel:
    # cv2.imshow("frame", eachDel)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()