import maya.cmds as cmds


class Toolbox():
    def __init__(self):
        self.window_name = 'acToolbox'

    def create(self):
        self.delete()

        self.window_name = cmds.window(self.window_name)
        self.m_column = cmds.columnLayout(p=self.window_name, adj=True, w=400)

        cmds.text(p=self.m_column,
                  label='Random Placement Generator')
        self.RPGrow1 = cmds.rowLayout(p=self.m_column, adj=True, nc=2)

        cmds.text(p=self.RPGrow1, label='Number of Duplicates:')
        self.Rval1 = cmds.intField(p=self.RPGrow1)
        self.RPGrow2 = cmds.rowLayout(p=self.m_column, adj=True, nc=3)
        cmds.text(p=self.RPGrow2, label='X Min and Max:')
        self.Rval2 = cmds.floatField(p=self.RPGrow2)
        self.Rval3 = cmds.floatField(p=self.RPGrow2)
        self.RPGrow3 = cmds.rowLayout(p=self.m_column, adj=True, nc=3)
        cmds.text(p=self.RPGrow3, label='Y Min and Max:')
        self.Rval4 = cmds.floatField(p=self.RPGrow3)
        self.Rval5 = cmds.floatField(p=self.RPGrow3)
        self.RPGrow4 = cmds.rowLayout(p=self.m_column, adj=True, nc=3)
        cmds.text(p=self.RPGrow4, label='Z Min and Max:')
        self.Rval6 = cmds.floatField(p=self.RPGrow4)
        self.Rval7 = cmds.floatField(p=self.RPGrow4)
        self.RPGrow5 = cmds.rowLayout(p=self.m_column, adj=True, nc=4)
        cmds.text(p=self.RPGrow5, label='XYZ Offset:')
        self.Rval8 = cmds.floatField(p=self.RPGrow5)
        self.Rval9 = cmds.floatField(p=self.RPGrow5)
        self.Rval10 = cmds.floatField(p=self.RPGrow5)
        cmds.button(p=self.m_column, label='Duplicate',
                    c=lambda *args: self.randButton())

        cmds.text(p=self.m_column, label='Sequential Renamer Tool')
        cmds.textField(p=self.m_column, placeholderText='Input must be in format: L_Arm_###_Geo')
        cmds.button(p=self.m_column, label='Rename',
                    c=lambda *args: self.renamerButton())

        cmds.text(p=self.m_column, label='Locator Placement')
        self.LProw1 = cmds.rowLayout(p=self.m_column, adj=True, nc=2)
        cmds.text(p=self.LProw1, label='Check for Individual Midpoints, Uncheck for Collective Midpoint:')
        self.LocBox1 = cmds.checkBox(p=self.LProw1, label='', value=False)
        self.nameButton = cmds.button(p=self.m_column, label='Find Midpoints',
                                      c=lambda *args: self.LocButton())

        cmds.text(p=self.m_column, label='Control Creator')
        self.CCrow1 = cmds.rowLayout(p=self.m_column, adj=True, nc=4)
        cmds.text(p=self.CCrow1, label='Move XYZ:')  # leave blank if you want control to be created at selection
        self.movex = cmds.floatField(p=self.CCrow1)
        self.movey = cmds.floatField(p=self.CCrow1)
        self.movez = cmds.floatField(p=self.CCrow1)
        self.CCrow2 = cmds.rowLayout(p=self.m_column, adj=True, nc=4)
        cmds.text(p=self.CCrow2, label='Rotate XYZ:')
        self.rotx = cmds.floatField(p=self.CCrow2)
        self.roty = cmds.floatField(p=self.CCrow2)
        self.rotz = cmds.floatField(p=self.CCrow2)
        self.CCrow3 = cmds.rowLayout(p=self.m_column, adj=True, nc=4)
        cmds.text(p=self.CCrow3, label='Scale XYZ:')
        self.scalex = cmds.floatField(p=self.CCrow3, v=1)
        self.scaley = cmds.floatField(p=self.CCrow3, v=1)
        self.scalez = cmds.floatField(p=self.CCrow3, v=1)
        self.CtrlButton = cmds.button(p=self.m_column, label='Create Control',
                                      c=lambda *args: self.ControlButton())

        cmds.text(p=self.m_column, label='Color Assignment')
        self.CArow1 = cmds.rowLayout(p=self.m_column, adj=True, nc=3)
        cmds.text(p=self.CArow1,
                  label='Color:')
        self.color = cmds.colorIndexSliderGrp(p=self.CArow1,
                                              minValue=0,
                                              maxValue=32)
        cmds.button(p=self.CArow1,
                    label='Change Color',
                    c=lambda *args: self.colorButton())

        cmds.text(p=self.m_column, label='Calulator')
        self.CalcRow3 = cmds.rowLayout(p=self.m_column, adj=True, nc=2)
        cmds.text(p=self.CalcRow3, label='Input:')
        self.CalcInput = cmds.textField(p=self.CalcRow3, w=100, text=b'') #separate numbs by commas
        self.CalcRow1 = cmds.rowLayout(p=self.m_column, nc=4, cw4=[100, 100, 100, 100])
        cmds.button(p=self.CalcRow1, label='Add', w=100,
                    c=lambda *args: self.AddButton())
        cmds.button(p=self.CalcRow1, label='Subtract', w=100,
                    c=lambda *args: self.SubButton())
        cmds.button(p=self.CalcRow1, label='Multiply', w=100,
                    c=lambda *args: self.MultButton())
        cmds.button(p=self.CalcRow1, label='Divide', w=100,
                    c=lambda *args: self.DivButton())
        self.CalcRow2 = cmds.rowLayout(p=self.m_column, nc=4, cw4=[100, 100, 100, 100])
        cmds.button(p=self.CalcRow2, label='Power', w=100,
                    c=lambda *args: self.PowerButton())
        cmds.button(p=self.CalcRow2, label='Mean', w=100,
                    c=lambda *args: self.MeanButton())
        cmds.button(p=self.CalcRow2, label='Median', w=100,
                    c=lambda *args: self.MedianButton())
        cmds.button(p=self.CalcRow2, label='Mode', w=100,
                    c=lambda *args: self.ModeButton())

        cmds.showWindow(self.window_name)

    def delete(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)

    def colorButton(self):
        import ColorChange
        value = cmds.colorIndexSliderGrp(self.color, q=True, v=True) - 1
        ColorChange.colorControl(value)

    def ControlButton(self):
        import ControlCreator

        mX = cmds.floatField(self.movex, q=True, v=True)
        mY = cmds.floatField(self.movey, q=True, v=True)
        mZ = cmds.floatField(self.movez, q=True, v=True)
        rX = cmds.floatField(self.rotx, q=True, v=True)
        rY = cmds.floatField(self.roty, q=True, v=True)
        rZ = cmds.floatField(self.rotz, q=True, v=True)
        sX = cmds.floatField(self.scalex, q=True, v=True)
        sY = cmds.floatField(self.scaley, q=True, v=True)
        sZ = cmds.floatField(self.scalez, q=True, v=True)

        ControlCreator.CtrlCreator(mX, mY, mZ, rX, rY, rZ, sX, sY, sZ)

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

    def renamerButton(self):
        import RenamingTool
        value = cmds.textField(self.nameButton, q=True, text=True)
        RenamingTool.RenamingTool(value)

    def LocButton(self):
        import LocatorPlacement as Loc
        midInd = cmds.checkBox(self.LocBox1, q=True, v=True)

        Loc.MidpointLocator(midInd)

    def AddButton(self):
        import Calculator as calc
        values = (cmds.textField(self.CalcInput, q=True, text=True)).split(',')
        for val in values:
            float(val)
        print calc.Add([values])
    def SubButton(self):
        import Calculator as calc
        values = (cmds.textField(self.CalcInput, q=True, text=True)).split(',')
        for val in values:
            float(val)
        print calc.Subtract([values])
    def MultButton(self):
        import Calculator as calc
        values = (cmds.textField(self.CalcInput, q=True, text=True)).split(',')
        for val in values:
            float(val)
        print calc.Multiplication([values])
    def DivButton(self):
        import Calculator as calc
        values = (cmds.textField(self.CalcInput, q=True, text=True)).split(',')
        for val in values:
            float(val)
        print calc.Division([values])
    def PowerButton(self):
        import Calculator as calc
        values = (cmds.textField(self.CalcInput, q=True, text=True)).split(',')
        for val in values:
            float(val)
        print calc.Power([values])
    def MeanButton(self):
        import Calculator as calc
        values = (cmds.textField(self.CalcInput, q=True, text=True)).split(',')
        for val in values:
            float(val)
        print calc.Mean([values])
    def MedianButton(self):
        import Calculator as calc
        values = (cmds.textField(self.CalcInput, q=True, text=True)).split(',')
        for val in values:
            float(val)
        print calc.Median([values])
    def ModeButton(self):
        import Calculator as calc
        values = (cmds.textField(self.CalcInput, q=True, text=True)).split(',')
        for val in values:
            float(val)
        print calc.Mode([values])

MyTB = Toolbox()
MyTB.create()
