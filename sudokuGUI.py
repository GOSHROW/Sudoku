from tkinter import *
from GenerateSudoku import Gen

class procStore:
    eltMat = []

def sudokuProc(dim, vacancy):

    ob = procStore()

    dim = eval(dim.replace('x', '*'))
    vacancy = int(int(vacancy) / 100 * dim * dim)
    sudokuUnfilled = Gen(dim, vacancy).remove()
    
    while len(sudokuUnfilled) == 0:
            sudokuUnfilled = Gen(dim, vacancy).remove()
    ob.eltMat = sudokuUnfilled

    sudokuWin = Tk()
    sudokuWin.title("Goshrow " + str(dim) + " " + str(vacancy))
    sudokuWin.geometry('700x700')
    sudokuWin.configure(background = '#c9aa88', borderwidth = '5px')

    for i in range(len(sudokuUnfilled)):
        for j in range(len(sudokuUnfilled[0])):
            if sudokuUnfilled[i][j]:
                Label(sudokuWin, text = str(sudokuUnfilled[i][j]), width = 5, height = 3).grid(row = i, column = j)
            else:
                vals = [str(i)+" "+str(j)+" "+ str(k) for k in range(dim+1)]
                varUnfilled = StringVar(sudokuWin)
                varUnfilled.set(vals[0])
                def setV(event):
                    stringEvent = str(event).split()
                    ob.eltMat[int(stringEvent[0])][int(stringEvent[1])] = int(stringEvent[-1])
                menuUnfilled = OptionMenu(sudokuWin, varUnfilled, *vals, command = setV)
                menuUnfilled.config(width = 5, font = ('calibri', (5)))
                menuUnfilled['menu'].config(font=('calibri',(5)),bg='white')
                menuUnfilled.grid(row = i, column = j)

    def sudokuCheck():
        print(ob.eltMat)
        pass
        
    button = Button(sudokuWin, text = "Submit and Check", pady = 20, command = sudokuCheck)
    button.grid(row = 100, column = 0, sticky = 'nsew', columnspan = len(sudokuUnfilled))

    sudokuWin.mainloop()


if __name__ == '__main__':
    sudokuProc('2 x 2', 40)