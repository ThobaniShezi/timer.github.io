from tkinter import *
from tkinter.ttk import *
from time import strftime

window = Tk()
window.title("Digital Clock")

def digitalClock():
    string = strftime('%H:%M:%S %p')
    Label.config(text=string)
    Label.after(1000, digitalClock)

Label = Label(window, font=("ds-digital", 80), background="black", foreground="cyan")
Label.pack(anchor="center")

digitalClock()
window.mainloop()
