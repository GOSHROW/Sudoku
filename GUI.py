from tkinter import *

window = Tk()
window.title("Goshrow Sudoku")
window.geometry('700x400')
window.configure(background = '#5792CF', borderwidth = '5px')

Label(window, text = "Choose the dimensions.").grid(row = 0, column = 0)
Label(window, text = " <Note 4x4 maybe computationally expensive and may take time to generate> ", font=("Courier", 6), activeforeground = 'red').grid(row = 1)
Label(window, text = "Choose % vacancy for the Sudoku").grid(row = 2, column = 0)

dimOption = ['2 x 2', '3 x 3', '4 x 4']
vacancyOption = list(str(i) for i in range(30, 91, 10))

varDim = StringVar(window)
varDim.set(dimOption[1])
menuDim = OptionMenu(*(window, varDim) + tuple(dimOption))
menuDim.grid(row = 0, column = 1)

varVacancy = StringVar(window)
varVacancy.set(vacancyOption[2])
menuVacancy = OptionMenu(*(window, varVacancy) + tuple(vacancyOption))
menuVacancy.grid(row = 2, column = 1)

window.mainloop()