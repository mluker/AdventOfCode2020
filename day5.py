seatIds = set()
with open('day5input.txt') as f:
    for line in f:
        minRow = 0
        maxRow = 127
        for i in range(7):
            offset = minRow + int(int(maxRow - minRow) / 2)
            if line[i] == 'F':
                maxRow = offset
            else:
                minRow = offset + 1
        row = min(minRow, maxRow)

        minColumn = 0
        maxColumn = 7
        for i in range(7, 10):
            offset = minColumn + int(int(maxColumn - minColumn) / 2)
            if line[i] == 'L':
                maxColumn = offset
            else:
                minColumn = offset + 1
        column = max(minColumn, maxColumn)

        seatId = row * 8 + column
        seatIds.add(seatId)

lst = sorted(seatIds)
print(lst)
print(sorted(set(range(lst[0], lst[-1])) - set(lst)))
