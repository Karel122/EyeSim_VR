from eye import *
from random import *

"""
for x in range (0,4):
    VWStraight(300,500)
    VWWait()
    VWTurn(90,100)
    VWWait()

LCDPrintf("Hello World")
LCDMenu("DONE", "BYE", "EXIT", "OUT")
KEYWait(ANYKEY)


while PSDGet(PSD_FRONT) > 200:
    VWSetSpeed(100,0)
VWSetSpeed(0,0)


LCDMenu("","","","END")
CAMInit(QVGA)
while (KEYRead () != KEY4):
    img = CAMGet()
    LCDImage(img)

"""
safe = 300
LCDMenu ("","","","END")

while (KEYRead() != KEY4):
    OSWait(100)
    if(PSDGet(PSD_FRONT)>safe and PSDGet(PSD_LEFT ) > safe) and PSDGet(PSD_RIGHT)> safe:
        VWStraight(100,200)
    else:
        VWStraight(-25,50)
        VWWait()
        dir = int(180*random()-0.5)
        VWTurn(dir,45)
        VWWait()
