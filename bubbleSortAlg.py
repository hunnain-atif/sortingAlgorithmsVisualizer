import time

def bubble_sort(array, drawArray, timeScale):
    for _ in range(len(array)-1):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                drawArray(array, ['green' if j == i or j == i+1 else 'red' for j in range(len(array))])
                time.sleep(timeScale)
    drawArray(array, ['green' for k in range(len(array))])