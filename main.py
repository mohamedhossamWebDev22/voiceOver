from gtts import gTTS
from tkinter import *
import os

window = Tk()
window.title("Arabic voice over")
window.geometry("500x400")

txt = Label(window, width=500, text="Arabic voice over", bg= "blue", fg= "white", font=("sans-serif", 40))
txt.pack()

l = Label(window, width=500, text="", bg= "blue", fg= "white", font=("sans-serif", 15))
l.pack()

inpt = Entry(window, width=20, font=("sans-serif", 30))
inpt.place(bordermode=INSIDE, y= 100, x= 25)

def go():
    klam = str(inpt.get())
    robot = gTTS(text = klam, lang='ar', slow=False)

    l.configure(text=klam)
    # print(klam)
    
    robot.save('go.mp3')
    os.system('go.mp3')
    

btn = Button(window, text="Go", bg= "blue",fg= "white", font=("sans-serif", 20), command= go)
btn.place(bordermode=INSIDE, y= 200, x = 200)

window.mainloop()
