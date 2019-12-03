def RandomDuplicater(duplicateAmount,
                     xMin, xMax,
                     yMin, yMax,
                     zMin, zMax,
                     xOffset, yOffset, zOffset):
    import maya.cmds as cmds
    import random
    sels = cmds.ls(sl=True)
    if (len(sels) != 1):
        cmds.error("Must select one object!")
    obj = []
    objects = []
    name = str(sels[0])

    for i in range(duplicateAmount):
        obj = cmds.duplicate()
        objects.append(obj[0])
        x = random.uniform(xMin, xMax)
        y = random.uniform(yMin, yMax)
        z = random.uniform(zMin, zMax)
        cmds.move(x, y, z)

    cmds.group(objects, name=name + "Group")
    cmds.move(xOffset, yOffset, zOffset)


RandomDuplicater(10, -10, 10, -3, 3, -10, 10, 0, 0, 0)
