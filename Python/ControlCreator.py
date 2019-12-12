import maya.cmds as cmds

def CtrlCreator(moveX, moveY, moveZ, rotX, rotY, rotZ, scaleX, scaleY, scaleZ):
    sels = cmds.ls(sl=True)

    if len(sels) == 0:
        cmds.circle(name='default_Ctrl')
        cmds.move(moveX, moveY, moveZ)
        cmds.rotate(rotX, rotY, rotZ)
        cmds.scale(scaleX, scaleY, scaleZ)
    if len(sels) != 0:

        for i in range(len(sels)):
            name = sels[i]
            posX = cmds.getAttr(name + '.translateX')
            posY = cmds.getAttr(name + '.translateY')
            posZ = cmds.getAttr(name + '.translateZ')

            tokens = name.split('_')
            if len(tokens) == 4:
                cmds.circle(name=(tokens[0] + '_' + tokens[1] + '_' + tokens[2] + '_Ctrl'))
                cmds.move(posX, posY, posZ)
                cmds.rotate(rotX, rotY, rotZ)
                cmds.scale(scaleX, scaleY, scaleZ)
            elif len(tokens) != 4:
                cmds.circle(name=(name + '_Ctrl'))
                cmds.move(posX, posY, posZ)
                cmds.rotate(rotX, rotY, rotZ)
                cmds.scale(scaleX, scaleY, scaleZ)


CtrlCreator(0,0,0, 0,0,0, 1,1,1)