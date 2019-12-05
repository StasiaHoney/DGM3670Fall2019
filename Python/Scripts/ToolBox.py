import maya.cmds as cmds

class Toolbox():
    def __init__(self):
        self.window_name = 'acToolbox'

    def create(self):
        self.delete()

        self.window_name = cmds.window(self.window_name)
        self.m_column = cmds.columnLayout(p=self.window_name, adj=True)
        cmds.button(p=self.m_column, label='MyButton',
                    c=lambda *args: cmds.polySphere(r=2))
        cmds.button(p=self.m_column, label='Yellow',
                    c=lambda *args: self.colorControl('yellow'))
        cmds.button(p=self.m_column, label='Red',
                    c=lambda *args: self.colorControl('red'))
        self.row1 = cmds.rowLayout(p=self.m_column, adj=True, nc=2)
        self.color = cmds.textField(p=self.row1,
                                    placeholderText='Enter color name...')
        cmds.button(p=self.row1,
                    label='Change Color',
                    c=lambda *args: self.colorButton())
        cmds.button(p=self.m_column,
                    label = 'Select Everything Ever',
                    c=lambda *args: self.selectBtn())

        cmds.showWindow(self.window_name)

    def delete(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)

    def colorButton(self):
        value = cmds.textField(self.color, q=True, text=True)
        self.colorControl(value)
        cmds.textField(self.color, e=True, text='')

    def selectBtn(self):
        from tools import SelectAll
        SelectAll()

    def colorControl(self, colorname):
        sels = cmds.ls(sl=True)

        if colorname == 'yellow':
            color = 17
        elif colorname == 'pink':
            color = 9
        elif colorname == 'red':
            color = 13

        for sel in sels:  # iterate through each selection
            shapes = cmds.listRelatives(sel, children=True, shapes=True)  # return all shape nodes

            for shape in shapes:  # iterate through each shape
                cmds.setAttr('%s.overrideEnabled' % shape, True)
                cmds.setAttr('%s.overrideColor' % shape, color)

myTool = Toolbox()
myTool.create()


