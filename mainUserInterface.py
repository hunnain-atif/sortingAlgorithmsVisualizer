from tkinter import *
import random 
from tkinter import ttk 
from bubbleSortAlg import bubble_sort
from quickSortAlg import quick_sort
from mergeSortAlg import merge_sort


#Create root for Tkinter layout
base = Tk()
base.maxsize(900, 600)
base.title('Sorting Algorithm Visualizer')
base.config(bg = 'orange')

#supporting Variables
selectedAlgorithm = StringVar()
array = []

#supporting Functions 
#starting animation and algorithm
def Start(): 
    global array
    if not array: return 

    if(algorithmSelectionMenu.get() == 'Quick Sort'):
        quick_sort(array, 0, len(array)-1, drawArray, speedInput.get())
    elif(algorithmSelectionMenu.get() == 'Merge Sort'):
        merge_sort(array, drawArray, speedInput.get())    
    elif(algorithmSelectionMenu.get() == 'Bubble Sort'):
        bubble_sort(array, drawArray, speedInput.get()) 
    
    drawArray(array, ['green' for j in range(len(array))])    
    

#Generating based on userInputs
def Generate():
    global array
    minValue = int(minInput.get())
    maxValue = int(maxInput.get())
    sizeValue = int(sizeInput.get())

    array = []
    for _ in range(sizeValue):
        array.append(random.randrange(minValue, maxValue + 1))

    drawArray(array, ['red' for j in range(len(array))])

#Drawing the array onto the screen for user to see
def drawArray(array, colorData):
    drawingArea.delete('all')
    drawingAreaHeight = 370
    drawingAreaWidth = 600
    barWidth = drawingAreaWidth / (len(array) + 1)
    barOffset = 25
    barSpacing = 10

    normalizedArray = [index / max(array) for index in array]
    for index, height in enumerate(normalizedArray):
        #getting top left point to draw rectangle
        leftX = index * barWidth + barOffset + barSpacing
        leftY = drawingAreaHeight - height * 340
        #getting bottom right point to draw rectangle
        rightX = (index + 1) * barWidth + barOffset
        rightY = drawingAreaHeight

        drawingArea.create_rectangle(leftX, leftY, rightX, rightY, fill = colorData[index])
        drawingArea.create_text(leftX + 2, leftY, anchor = SW, text = str(array[index]))
    base.update_idletasks()

#creating layout for user interface
frame = Frame(base, width = 600, height = 200, bg = 'grey')
frame.grid(row = 0, column = 0, padx = 10, pady = 5)

#creating latout for array visualization 
drawingArea = Canvas(base, width = 600, height = 370, bg ='white')
drawingArea.grid(row = 1, column = 0, padx = 10, pady = 5)

#create buttons and labels for user interface
Label(frame, text = "Choose Algorithm: ", bg = 'grey').grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)

algorithmSelectionMenu = ttk.Combobox(frame, textvariable = selectedAlgorithm, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
algorithmSelectionMenu.grid(row = 0, column = 1, padx = 5, pady = 5)
algorithmSelectionMenu.current(0)

speedInput = Scale(frame, from_ = 0.1, to = 4.0, length = 200, digits = 2, resolution = 0.2, orient = HORIZONTAL, label = "Select Speed")
speedInput.grid(row = 0, column = 2, padx =5, pady = 5)

Button(frame, text = "Start", command = Start, fg = 'white', bg = 'red').grid(row = 0, column = 3, padx = 5, pady = 5)

minInput = Scale(frame, from_ = 0, to = 10, resolution = 1, orient = HORIZONTAL, label = "Minimum Value")
minInput.grid(row = 1, column = 0, padx = 5, pady = 5)

maxInput = Scale(frame, from_ = 10, to = 100, resolution = 1, orient = HORIZONTAL, label = "Maximum Value")
maxInput.grid(row = 1, column = 1, padx = 5, pady = 5)

sizeInput = Scale(frame, from_ = 3, to = 30, resolution = 1, orient = HORIZONTAL, label = "Array Size")
sizeInput.grid(row = 1, column = 2, padx = 5, pady = 5)

Button(frame, text = "Generate", command = Generate, fg = 'white', bg = 'red').grid(row = 1, column = 3, padx = 5, pady = 5)

base.mainloop()