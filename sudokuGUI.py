from tkinter import *
from GenerateSudoku import Gen
from Solution import BackTrackSolution
from IMGSudoku import *

class procStore:
    eltMat = []
    newSolution = []
    c = 0

ob = procStore()

def sudokuProc(dim = '3x3', vacancy = 50):

    dim = eval(dim.replace('x', '*'))
    vacancy = int(int(vacancy) / 100 * dim * dim)
    sudokuUnfilled = Gen(dim, vacancy).remove()
    dim = len(sudokuUnfilled)
    while len(sudokuUnfilled) == 0:
        sudokuUnfilled = Gen(dim, vacancy).remove()
    ob.eltMat = sudokuUnfilled

def sudokuIMG(arr = [[0]* 9]* 9):
    ob.eltMat = arr
    finalProc()

def finalProc(sudokuUnfilled):
    solved = BackTrackSolution(ob.eltMat).sudokuMatrix
    sudokuWin = Tk()
    sudokuWin.title("Goshrow " + str(dim) + " " + str(vacancy))
    sudokuWin.geometry('700x700')
    sudokuWin.configure(background = '#c9aa88', borderwidth = '5px')

    for i in range(len(sudokuUnfilled)):
        for j in range(len(sudokuUnfilled[0])):
            if sudokuUnfilled[i][j]:
                Label(sudokuWin, text = str(sudokuUnfilled[i][j]), width = 5, height = 3).grid(row = i, column = j)
            else:
                vals = ["("+str(i)+"-"+str(j)+") "+ str(k) for k in range(dim+1)]
                varUnfilled = StringVar(sudokuWin)
                varUnfilled.set(vals[0])
                def setV(event):
                    stringEvent = [event.split('-')[0][1:], event[event.index('-') + 1:event.index(')')], event.split()[1]]
                    ob.eltMat[int(stringEvent[0])][int(stringEvent[1])] = int(stringEvent[-1])
                menuUnfilled = OptionMenu(sudokuWin, varUnfilled, *vals, command = setV)
                menuUnfilled.config(width = 5, font = ('calibri', (10)), bg='WHITE')
                menuUnfilled['menu'].config(font=('calibri',(10)), bg='#c9aa88')
                menuUnfilled.grid(row = i, column = j)

    def sudokuCheck():
        ob.c += 1 
        try :
            ob.newSolution = BackTrackSolution(ob.eltMat).sudokuMatrix
        except Exception as e :
            temp = ob.eltMat[0][0]
            ob.eltMat[0][0] = 0
            ob.newSolution = BackTrackSolution(ob.eltMat).sudokuMatrix
            ob.eltMat[0][0] = temp

        for i in ob.newSolution:
            if 0 in i:
                ob.newSolution = []
                break
        solvedCells = 0

        ret = "Congrats!!" if ob.eltMat == ob.newSolution else "Not fully Solved in " + str(ob.c) + " attempt."
        for i in range(len(solved)):
            for j in range(len(solved[0])):
                if ob.eltMat[i][j] == solved[i][j]:
                    solvedCells += 1
        ret = ret + "\t" + str(solvedCells * 100 / dim / dim) + " % Solved wrt Initial Solution"
        Label(sudokuWin, text = ret, bg = '#c9aa88', pady = 10).grid( row = 101 + ob.c, column = 0, columnspan = len(sudokuUnfilled))

        
    Label(sudokuWin, text = "", bg = '#c9aa88', pady = 20).grid( row = 100, column = 0)
    button = Button(sudokuWin, text = "Submit and Check", pady = 20, command = sudokuCheck)
    button.grid(row = 101, column = 0, sticky = 'nsew', columnspan = len(sudokuUnfilled))

    sudokuWin.mainloop()


if __name__ == '__main__':
# For testing purposes only,
# Run Code by entering your own
# Specifications as Parameters to sudokuProc()
# and by python3 sudokuGUI.py
    sudokuProc('2 x 2', 40)