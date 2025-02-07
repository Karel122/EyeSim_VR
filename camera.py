from eye import *

LCDMenu("","","","END")
CAMInit(QVGA)
while (KEYRead () != KEY4):
    img = CAMGet()
    LCDImage(img)