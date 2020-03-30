from tkinter import *

class Store:
    vacancy = 50
    dim = '3 x 3'

def init():

    ob = Store()

    window = Tk()
    window.title("Goshrow Sudoku")
    window.geometry('700x400')
    window.configure(background = '#5792CF', borderwidth = '5px')

    Label(window, text = "Choose the dimensions.", width = 30).grid(row = 0, column = 0, pady = 10)
    Label(window, text = "Choose % vacancy for the Sudoku", width = 30).grid(row = 1, column = 0, pady = 10)


    dimOption = ['2 x 2', '3 x 3', '4 x 4']
    vacancyOption = list(str(i) for i in range(30, 91, 10))

    varDim = StringVar(window)
    varDim.set(ob.dim)
    def setD(event):
        ob.dim = event
    menuDim = OptionMenu(window, varDim, *dimOption, command = setD)
    menuDim.config(width = 20)
    menuDim.grid(row = 0, column = 1)

    varVacancy = StringVar(window)
    varVacancy.set(ob.vacancy)
    def setV(event):
        ob.vacancy = event
    menuVacancy = OptionMenu(window, varVacancy, *vacancyOption, command = setV)
    menuVacancy.config(width = 20)
    menuVacancy.grid(row = 1, column = 1)

    button = Button(window, text = "Submit, Start Game", pady = 10, command = lambda: sudokuProc(ob.dim, ob.vacancy))
    button.grid(row = 2, column = 1, sticky = 'nsew')

    window.mainloop()

def sudokuProc(dim, vacancy):
    dim = eval(dim.replace('x', '*'))
    vacancy = int(int(vacancy) / 100 * dim * dim)
    print(dim, vacancy)

if __name__ == '__main__':
    init()