testScores = ['Bill', 86, 'Nancy', 98, 'Joel', 54]
names = []
scores = []
for i in range(len(testScores)):
    if (i%2 == 0):
        names.append(testScores[i])
    else:
        scores.append(testScores[i])

print 'Names:', names
print 'Scores:', scores

############################

for i in range(10):
    print i