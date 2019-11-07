import maya.cmds as cmds

sels = cmds.ls(sl=True)
numInt = 6
numFloat = 3.4

print numInt
print numFloat
print sels[0]

students = [['Ellie', 'Joel', 'Dina', 'Jesse'],
            [100, 98, 67, 83],
            ['Rodayne', 'Clayton', 'Marty', 'Anthony']]

print students[0][3], 'respects', students[2][1]

for student in students:
    print student

for i in range(10):

for i in range(len(students)):
    print students[i]
    print i

for student in students:
    #student is ['Ellie', 'Joel', 'Dina', 'Jesse']
    for s in student:
        print s, 'is great!' #prints every item individually in each list in students

for i in range(len(students[0])):
    print 'Name:', students[0][i]
    print 'Score:', students[1][i]
    print 'Teacher:', students[2][i]
    print '-------------------------'

print 'complete'

nameString = 'MatthewSithLordMeyers'
print nameString[7:15]
#strings are basically lists of letters, so you can print individual letters