
def getRow(rowIndex):

    if rowIndex == 0:
        return [1]


    previousRow = [1]
    currentRow = []

    for i in range(rowIndex):
        previousRow = currentRow
        currentRow = []

        for j in range(i):
            currentRow.append(previousRow[j] + previousRow[j+1])
        currentRow.append(1)

    return currentRow

print(getRow(1))