import maya.cmds as cmds
def SelectAll():
    cmds.ls(all=True)
    sels= cmds.ls(sl=True)
    return sels
def ball():
    obj = cmds.polySphere('Ball_Geo')[0]
    return obj