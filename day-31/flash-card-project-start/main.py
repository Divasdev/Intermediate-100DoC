from textwrap import fill

from pandas.core.methods.selectn import DataFrame
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

import tkinter as tk
from tkinter import PhotoImage, Button
#-------------Functions------------------
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")
current_card = {}

def known_card():
    to_learn.remove(current_card)
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def next_card():
    global current_card, flip_timer

    display.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(title_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")

    flip_timer = display.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(title_text,text="English")
    canvas.itemconfig(word_text,text=current_card["English"],fill="white")
    canvas.itemconfig(card,image=card_back)








#---------------UI-------------------------------------
display = tk.Tk()
display.title("Flashy")
display.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


# Card Image
card_front = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263, image=card_front)

card_back=PhotoImage(file="images/card_back.png")
flip_timer=display.after(3000,flip_card)

title_text = canvas.create_text(400, 150, text="French", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", fill="black", font=("Arial", 60, "bold"))

canvas.itemconfig(title_text,text="French")
canvas.itemconfig(word_text,text=current_card.get("French",""))



# Button Images
right_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_image,
                    highlightthickness=0,
                    borderwidth=0,
                    command = known_card)
right_button.grid(row=1,column=1)


wrong_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image,
                    highlightthickness=0,
                    borderwidth=0,
                    command=next_card)
wrong_button.grid(row=1,column=0)





next_card()
display.mainloop()