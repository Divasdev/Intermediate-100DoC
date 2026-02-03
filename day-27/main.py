import tkinter

window=tkinter.Tk()

window.title("My first GUI program")
window.minsize(500,300)

my_label=tkinter.Label(text="I am a label",font=("Sans Serif",24,"italic"))
my_label.pack(side="left")












window.mainloop()
