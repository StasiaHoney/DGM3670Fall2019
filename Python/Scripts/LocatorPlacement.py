import maya.cmds as cmds
def MidpointLocator(midpointInd):

    sels = cmds.ls(selection=True)

    if midpointInd == True:
        for i in range(len(sels)):
            selectionBB = cmds.xform(sels[i], query=True, boundingBox=True)
            midpointX = ((selectionBB[0] + selectionBB[3]) / 2)
            midpointY = ((selectionBB[1] + selectionBB[4]) / 2)
            midpointZ = ((selectionBB[2] + selectionBB[5]) / 2)

            cmds.spaceLocator(position=[midpointX, midpointY, midpointZ])

    elif midpointInd==False:

        cmds.group(sels, name="Locators")

        selectionBB = cmds.xform('Locators', query=True, boundingBox=True)
        midpointX = ((selectionBB[0] + selectionBB[3]) / 2)
        midpointY = ((selectionBB[1] + selectionBB[4]) / 2)
        midpointZ = ((selectionBB[2] + selectionBB[5]) / 2)

        cmds.spaceLocator(position=[midpointX, midpointY, midpointZ])
        cmds.ungroup('Locators')


