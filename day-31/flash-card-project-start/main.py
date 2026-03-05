BACKGROUND_COLOR = "#B1DDC6"

import tkinter as tk
from tkinter import PhotoImage

display = tk.Tk()
display.title("Flashy")

canvas = tk.Canvas(display, width=800, height=600, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Background Image
background_image = PhotoImage(file="images/background.png")
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Foreground Image
foreground_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 300, image=foreground_image)

display.mainloop()