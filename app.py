
from setup import main
main()
import rps
from tkinter import *

root = Tk()
root.title("Python C Extension")

def run(choice):
    answer.delete(0, END)
    num = int(choice)
    result = rps.rps(num)
    

    answer.insert(0, result)

answer = Entry(root)
answer.grid(row=0, column=0, columnspan=3)

rock = Button(root, text="Rock", command=lambda: run(0))
rock.grid(row=1, column=0)
paper = Button(root, text="Paper", command=lambda: run(1))
paper.grid(row=1, column=1)
scissors = Button(root, text="Scissors", command=lambda: run(2))
scissors.grid(row=1, column=2)


root.mainloop()