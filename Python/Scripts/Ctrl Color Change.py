def colorControl(colorname):

    import maya.cmds as cmds

    sels = cmds.ls(sl=True)

    if colorname == 'yellow':
        color = 17
    elif colorname == 'pink':
        color = 9
    elif colorname == 'red':
        color = 13


    for sel in sels: #iterate through each selection
        shapes = cmds.listRelatives(sel, children=True, shapes=True) #return all shape nodes

        for shape in shapes: #iterate through each shape
            cmds.setAttr('%s.overrideEnabled' % shape, True)
            cmds.setAttr('%s.overrideColor' % shape, color)