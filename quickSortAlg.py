import time 

def partition(array, head, tail, drawArray, timeScale):
    border = head
    pivot = array[tail]

    drawArray(array, createColourData(len(array), head, tail, border, border, False))
    time.sleep(timeScale)

    for i in range(head, tail):
        if array[i] < pivot:
            drawArray(array, createColourData(len(array), head, tail, border, i, True))
            time.sleep(timeScale)
            array[border], array[i] = array[i], array[border]
            border += 1
            drawArray(array, createColourData(len(array), head, tail, border, i, False))
            time.sleep(timeScale)
    
    drawArray(array, createColourData(len(array), head, tail, border, tail, True))
    time.sleep(timeScale)        
    array[border], array[tail] = array[tail], array[border]
    return border

def quick_sort(array, head, tail, drawArray, timeScale):
    if head < tail: 
        partitionIndex = partition(array, head, tail, drawArray, timeScale)
        #Left Side
        quick_sort(array, head, partitionIndex - 1, drawArray, timeScale)
        #Right Side
        quick_sort(array, partitionIndex + 1, tail, drawArray, timeScale)

def createColourData(arraylength, head, tail, border, currentIndex, isMoving = False):
    colourData = []
    for j in range(arraylength):
        if j >= head and j <= tail:
            colourData.append('gray')
        else:
            colourData.append('white')
        if j == tail:
            colourData[j] = 'blue'
        elif j == border:
            colourData[j] = 'red'
        elif j == currentIndex:
            colourData[j] = 'yellow'

        if isMoving:
            if j == border or j == currentIndex:
                colourData[j] = 'green'    
    return colourData

