from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
my_timer = None
reps=0

my_timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, timer
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global  reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_secs=SHORT_BREAK_MIN*60
    long_break_secs=LONG_BREAK_MIN*60


    if reps%8==0:
        countdown(long_break_secs)
        label.config(text="Long Break",fg=RED)

    elif reps%2==0:
        countdown(short_break_secs)
        label.config(text="Short Break",fg=PINK)
    else:
        countdown(work_sec)
        label.config(text="Work",fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time

def countdown(count):


    count_min=math.floor(count / 60)
    count_sec=count %60
    if count_sec<10:
        count_sec=f"0{count_sec}"


    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")


    if count>0:
        global timer
        timer= window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark=" "
        for _ in range(math.floor(reps/2)):
            mark+="✔"
        check_mark.config(text=mark,fg=YELLOW)




# ---------------------------- UI SETUP ------------------------------- #

window=Tk()

window.title("Promodoro")

window.config(padx=100,pady=50,bg=YELLOW)
window.resizable(False,False)




label=Label(text="Timer",font=(FONT_NAME,30,"bold"),bg=YELLOW,fg=GREEN)
label.grid(row=0,column=1)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
my_image=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=my_image)

timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))


start_button=Button(window, text="Start",command=start_timer)
start_button.grid(row=2, column=0)



reset_button=Button(window, text="Reset",command=reset)
reset_button.grid(row=2, column=2)

check_mark=Label(text="",fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)



canvas.grid(row=1, column=1)





window.mainloop()
