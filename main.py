from logging import PlaceHolder
import tkinter
from gtts import gTTS
from tkinter import *

window = Tk()
window.title("Arabic voice over")
window.geometry("500x400")

inp = Entry(window, width=50)
inp.place(bordermode=INSIDE, y= 10, x= 100)


window.mainloop()
