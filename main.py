from tkinter import *
import pandas as pd
from random import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("words_to_learn")
except FileNotFoundError:
    original_data = pd.read_csv("Frenchwords.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_bg, image=card_f)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(words,text=current_card["French"],fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_bg,image=card_b)
    canvas.itemconfig(words, text=current_card["English"],fill="white")

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("words_to_learn",index = False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800,height=526)
card_f = PhotoImage(file="card_front.png")
card_b =PhotoImage(file="card_back.png")

card_bg = canvas.create_image(400,263,image=card_f)
card_title = canvas.create_text(400,150,text="",font=("Ariel", 40, "italic"))
words = canvas.create_text(400,263,text="",font=("Ariel", 60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

cross_img = PhotoImage(file="wrong.png")
crt_img = PhotoImage(file="right.png")

unknown_button = Button(image=cross_img,highlightthickness=0,command=next_card)
unknown_button.grid(row = 1 ,column= 0)

known_button = Button(image=crt_img,highlightthickness=0,command=is_known)
known_button.grid(row = 1,column = 1)

next_card()


window.mainloop()
