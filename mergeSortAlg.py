import time

def merge_sort(array, drawArray, timeScale):
    merge_sort_algorithm(array, 0, len(array) - 1, drawArray, timeScale)


def merge_sort_algorithm(array, left, right, drawArray, timeScale):
    if left < right: 
        middleIndex = (left + right) // 2
        merge_sort_algorithm(array, left, middleIndex, drawArray, timeScale)
        merge_sort_algorithm(array, middleIndex + 1, right, drawArray, timeScale)
        mergeLists(array, left, middleIndex, right, drawArray, timeScale)

def mergeLists(array, left, middleIndex, right, drawArray, timeScale):
    drawArray(array, createColourData(len(array), left, middleIndex, right))
    time.sleep(timeScale)
    leftPartition = array[left:middleIndex + 1]
    rightPartition = array[middleIndex + 1: right + 1]
    leftIndex = 0
    rightIndex = 0
    for i in range(left, right+1):
        if leftIndex < len(leftPartition) and rightIndex < len(rightPartition):
            if leftPartition[leftIndex] <= rightPartition[rightIndex]:
                array[i] = leftPartition[leftIndex]
                leftIndex += 1
            else:
                array[i] = rightPartition[rightIndex]
                rightIndex += 1
        elif leftIndex < len(leftPartition):
            array[i] = leftPartition[leftIndex]
            leftIndex += 1
        else:
            array[i] = rightPartition[rightIndex]
            rightIndex += 1

    drawArray(array, ['green' if j >= left and j <= right else 'white' for j in range(len(array))])
    time.sleep(timeScale)

def createColourData(arrayLength, left, middleIndex, right):
    colourData =[]
    for j in range(arrayLength):
        if j >= left and j <= right:
            if j <= middleIndex:
                colourData.append('yellow')
            else:
                colourData.append('gray')
        else:
            colourData.append('white')
    return colourData


            