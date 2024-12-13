import tkinter
import pandas
import random
# from pandas import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"
english_translation = ""
to_learn = {}

# data = pandas.read_csv("data/french_words.csv")
# to_learn = data.to_dict(orient="records")
# print(to_learn)
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global english_translation, flip_timer, random_pair
    window.after_cancel(flip_timer)
    random_pair = random.choice(to_learn)
    # random_pair["French"]
    canvas.itemconfig(card_title, text="French", fill="black") # re-assigning value of card_title variable
    canvas.itemconfig(card_word, text=random_pair["French"], fill="black")
    english_translation = random_pair["English"]
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_translation, fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    to_learn.remove(random_pair)
    # print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
# Canvas
canvas = tkinter.Canvas(width=800 , height=526)
card_front_image= tkinter.PhotoImage(file="images/card_front.png")
card_back_image = tkinter.PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)       # are x and y positions on the canvas
card_title = canvas.create_text(400,150, text="Title", font=(FONT_NAME, 40, "italic"), fill="black")

card_word = canvas.create_text(400, 263, text="word", font=(FONT_NAME, 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# window.after_cancel(3000)

# Buttons:
yes_image = tkinter.PhotoImage(file="images/right.png")
yes_button = tkinter.Button(image=yes_image, highlightthickness=0, command=is_known)
yes_button.grid(column=1, row=1)
no_image = tkinter.PhotoImage(file="images/wrong.png")
no_button = tkinter.Button(image=no_image, highlightthickness=0, command=next_card)
no_button.grid(column=0, row=1)

next_card() # calling that function here ensures "Title" does not display when initially running the app


window.mainloop()