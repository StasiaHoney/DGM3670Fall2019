def colorControl(color):

    import maya.cmds as cmds

    sels = cmds.ls(sl=True)

    for sel in sels: #iterate through each selection
        children = cmds.listRelatives(sel, children=True, shapes=True) #return all shape nodes

        for child in children: #iterate through each shape
            cmds.setAttr('%s.overrideEnabled' % shape, True)
            cmds.setAttr('%s.overrideColor' % shape, 6)