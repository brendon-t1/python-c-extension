
from setup import main
main()
import rps
from tkinter import *

root = Tk()
root.title("Python C Extension")

def run():
    answer.delete(0, END)
    num = int(choice_entry.get())
    result = rps.rps(num)
    #result = rps.rps(1)

    answer.insert(0, result)

answer = Entry(root)
answer.grid(row=0, column=0, columnspan=1)

choice_entry = Entry(root, width=20)
choice_entry.grid(row=1, column=0,columnspan=1)
choice_label = Label(root, text="Enter num here")
choice_label.grid(row=2, column=0)

button_run = Button(root, text="Run", command=run)
button_run.grid(row=3, column=0, columnspan=1)


root.mainloop()