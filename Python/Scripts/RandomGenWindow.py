import maya.cmds as cmds

class RandGenWindow():
    def __init__(self):
        self.window_name = 'Random Duplicator'

    def create(self):
        self.row2 = cmds.rowLayout(p=self.m_column, adj=True, nc=3)
        cmds.text(p=self.row2,
                  label='Number of Duplicates:')
        self.Rval1 = cmds.intField(p=self.row2)
        self.row3 = cmds.rowLayout(p=self.m_column, adj=True, nc=3)
        cmds.text(p=self.row3, label='X Min and Max:')
        self.Rval2 = cmds.floatField(p=self.row3)
        self.Rval3 = cmds.floatField(p=self.row3)
        self.row4 = cmds.rowLayout(p=self.m_column, adj=True, nc=3)
        cmds.text(p=self.row4, label='Y Min and Max:')
        self.Rval4 = cmds.floatField(p=self.row4)
        self.Rval5 = cmds.floatField(p=self.row4)
        self.row5 = cmds.rowLayout(p=self.m_column, adj=True, nc=3)
        cmds.text(p=self.row5, label='Z Min and Max:')
        self.Rval6 = cmds.floatField(p=self.row5)
        self.Rval7 = cmds.floatField(p=self.row5)
        self.row6 = cmds.rowLayout(p=self.m_column, adj=True, nc=4)
        cmds.text(p=self.row6, label='XYZ Offset:')
        self.Rval8 = cmds.floatField(p=self.row6)
        self.Rval9 = cmds.floatField(p=self.row6)
        self.Rval10 = cmds.floatField(p=self.row6)
        cmds.button(p=self.m_column, label='Duplicate',
                    c=lambda *args: self.randButton())

        cmds.showWindow(self.window_name)

    def randButton(self):
        import RandomPlacementGenerator as random
        dA = cmds.intField(self.Rval1, q=True, v=True)
        xMin = cmds.floatField(self.Rval2, q=True, v=True)
        xMax = cmds.floatField(self.Rval3, q=True, v=True)
        yMin = cmds.floatField(self.Rval4, q=True, v=True)
        yMax = cmds.floatField(self.Rval5, q=True, v=True)
        zMin = cmds.floatField(self.Rval6, q=True, v=True)
        zMax = cmds.floatField(self.Rval7, q=True, v=True)
        xOff = cmds.floatField(self.Rval8, q=True, v=True)
        yOff = cmds.floatField(self.Rval9, q=True, v=True)
        zOff = cmds.floatField(self.Rval10, q=True, v=True)

        random.RandomDuplicater(dA, xMin, xMax, yMin, yMax, zMin, zMax, xOff, yOff, zOff)
