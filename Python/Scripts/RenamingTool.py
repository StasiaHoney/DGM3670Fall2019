def RenamingTool(input):
    import maya.cmds as cmds
    sels = cmds.ls(selection=True)
    tokens = []

    tokens = input.split("#")
    num = len(tokens) - 1
    del tokens[1:num]

    digitsDelimeter = (len(input) - len(tokens[0]) - len(tokens[1]))

    for i in range(len(sels)):
        digitsIter = len(str(i + 1))
        numPad = (digitsDelimeter - digitsIter)
        pad = ""

        for j in range(numPad):
            pad = pad + "0"

        cmds.rename(sels[i], (tokens[0] + pad + str(i + 1) + tokens[1]))


RenamingTool("L_Arm_###_Geo")