from tkinter import *

window=Tk()

window.title("My first GUI program")
window.minsize(500,300)

my_label = Label(text="I", font=("Sans Serif", 24, "italic"))
my_label.pack()

def btn_click():
    print("I got Clicked")







button=Button(text="Click Me!",command=btn_click)
button.pack()


input=Entry(width=10)
input.pack()
















window.mainloop()
