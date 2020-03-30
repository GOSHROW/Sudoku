from tkinter import *

window = Tk()
window.title("Goshrow Sudoku")
window.geometry('700x400')
window.configure(background = '#5792CF', borderwidth = '5px')

Label(window, text = "Choose the dimensions.", width = 30).grid(row = 0, column = 0, pady = 10)
Label(window, text = "Choose % vacancy for the Sudoku", width = 30).grid(row = 1, column = 0, pady = 10)


dimOption = ['2 x 2', '3 x 3', '4 x 4']
vacancyOption = list(str(i) for i in range(30, 91, 10))

varDim = StringVar(window)
varDim.set(dimOption[1])
menuDim = OptionMenu(*(window, varDim) + tuple(dimOption))
menuDim.config(width = 20)
menuDim.grid(row = 0, column = 1)
dim = varDim.get()

varVacancy = StringVar(window)
varVacancy.set(vacancyOption[2])
menuVacancy = OptionMenu(*(window, varVacancy) + tuple(vacancyOption))
menuVacancy.config(width = 20)
menuVacancy.grid(row = 1, column = 1)
vacancy = varVacancy.get()

button = Button(window, text = "Submit, Start Game", pady = 10)
button.grid(row = 2, column = 1, sticky = 'nsew')

window.mainloop()