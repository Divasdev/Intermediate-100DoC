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
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
reps = 0
def start_timer():
        global reps
        reps+= 1
        work_sec=WORK_MIN*60
        short_break_sec=SHORT_BREAK_MIN*60
        long_break_secs=LONG_BREAK_MIN*60
        if reps % 8 == 0:
            title_label.config(text="Break",fg=RED)
            count_down(long_break_secs)
        elif reps % 2 == 0:
            title_label.config(text="Break", fg=PINK)
            count_down(short_break_sec)

        else:
            title_label.config(text="Work", fg=GREEN)
            count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
import time

def count_down(count):
   count_mins=math.floor(count/60)
   count_secs=count%60
   if count_secs<10:
       count_secs=f"0{count_secs}"

   canvas.itemconfig(timer_text,text=f"{count_mins}:{count_secs}")
   if count>0:
       global my_timer
       my_timer=window.after(1000, count_down, count - 1)
   else:
       start_timer()
       mark=""
       work_sessions=math.floor(reps/2)
       for _ in range(work_sessions):
           mark+="✅"
       check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Promodoro")
window.config(padx=100,pady=50,bg=YELLOW)



title_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(column=1, row=0)


canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text =canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,'bold'))

canvas.grid(column=1,row=1)


start_btn=Button(text="Start",highlightthickness=0,bg=YELLOW,command=start_timer)
start_btn.grid(column=0,row=2)

reset_btn=Button(text="Reset",highlightthickness=0,bg=YELLOW,command=reset_timer)
reset_btn.grid(column=2,row=2)

check_marks=Label(text="",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)






window.mainloop()
