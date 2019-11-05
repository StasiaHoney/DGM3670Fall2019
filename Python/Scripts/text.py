import maya.cmds as mc

mc.polySphere(axis=[1,0,0], radius=5, name='Head', constructionHistory=True)
mc.polyCube(d=3, h=1, w=5, n='Box')