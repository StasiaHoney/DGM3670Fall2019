import maya.cmds as cmds

def colorControl(color):
    sels = cmds.ls(sl=True)


    for sel in sels:  # iterate through each selection
        shapes = cmds.listRelatives(sel, children=True, shapes=True)  # return all shape nodes

        for shape in shapes:  # iterate through each shape
            cmds.setAttr('%s.overrideEnabled' % shape, True)
            cmds.setAttr('%s.overrideColor' % shape, color)