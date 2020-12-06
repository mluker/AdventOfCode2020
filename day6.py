f = open("day6input.txt", "r")
runningCount = 0
answers = {}

for l in f:
    if l == "\n":
        runningCount += len(answers)
        #print('group count: {}'.format(len(answers)))
        answers = {}

    for c in l.strip():
        #print("-" + c + '-')
        answers[c] = 1

#print('group count: {}'.format(len(answers)))
runningCount += len(answers)
f.close()
print('running count: {}'.format(runningCount))
