from tkinter import *
from IMGSudoku import *
import sudokuGUI

def predict(f):
    arMat = []
    for i in range(9):
        arMat.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    arr = recognizer(f)
    window = Tk()
    window.title("Modify Sudoku")
    window.geometry('1000x1000')
    window.configure(background = '#5792CF', borderwidth = '5px')

    dim = int(len(arr) ** 0.5)

    for i, e in enumerate(arr):
        arMat[i // dim][i % dim] = e

    for i in range(len(arMat)):
            for j in range(len(arMat[0])):
                vals = ["("+str(i)+"-"+str(j)+") "+ str(k) for k in range(dim+1)]
                varUnfilled = StringVar(window)
                varUnfilled.set('(' + str(i) + '-' + str(j) + ')' + str(arMat[i][j]))
                def setV(event):
                    stringEvent = [event.split('-')[0][1:], event[event.index('-') + 1:event.index(')')], event.split()[1]]
                    arMat[int(stringEvent[0])][int(stringEvent[1])] = int(stringEvent[-1])
                menuUnfilled = OptionMenu(window, varUnfilled, *vals, command = setV)
                menuUnfilled.config(width = 5, font = ('calibri', (10)), bg='WHITE')
                menuUnfilled['menu'].config(font=('calibri',(10)), bg='#c9aa88')
                menuUnfilled.grid(row = i, column = j)
    
    button = Button(window, text = "Start Game, Submit Selection", pady = 20, command = lambda : sudokuGUI.finalProc(arMat))
    button.grid(row = 101, sticky = 'nsew', columnspan = dim)

    window.mainloop()

if __name__ == '__main__':
    predict("/home/goshrow/Sudoku/testIMGsudoku.jpg")