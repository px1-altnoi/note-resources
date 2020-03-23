import pymel.core as pm
import random

count = 0
while count < 800:
    cube = pm.polyCube()
    x = random.random()*10
    y = random.random()*10
    z = random.random()*10
    pm.move(x, y, z, a = True)
    count += 1

i = 0
while i < 800:
    temp = "pCubeShape" + str(i) + ".aiOpaque"
    print(maya.cmds.setAttr(temp, 0))
    i += 1
