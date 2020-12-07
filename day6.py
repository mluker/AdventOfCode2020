runningCount = 0
runningCountAllYes = 0
peopleInGroup = 0
answers = {}

f = open("day6input.txt", "r")
for l in f:
    if l == "\n":
        runningCount += len(answers)
        runningCountAllYes += len([v for v in answers.values() if int(v) >= peopleInGroup])
        peopleInGroup = 0
        answers = {}
    else:
        peopleInGroup += 1
        for c in l.strip():
            answers[c] = (answers.get(c) or 0) + 1

runningCount += len(answers)
runningCountAllYes += len([v for v in answers.values() if int(v) >= peopleInGroup])
f.close()

print('total running count: {}'.format(runningCount))
print('all yes: {}'.format(runningCountAllYes))
