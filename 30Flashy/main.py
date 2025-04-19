from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
DATA_FILE_LOC = "./resources/Data/30french_words.csv"

current_card = {}
to_learn = {}

try:
    WORDS_TO_LEARN_LOC = "./resources/Data/30words_to_learn.csv"
    data = pandas.read_csv(WORDS_TO_LEARN_LOC)
except FileNotFoundError:
    original_data = pandas.read_csv(DATA_FILE_LOC)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(flashcard_title, text="French", fill="black")
    canvas.itemconfig(flashcard_background, image=flashcard_front_img)
    canvas.itemconfig(flashcard_text, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(flashcard_title, text="English", fill="white")
    canvas.itemconfig(flashcard_background, image=flashcard_back_img)
    canvas.itemconfig(flashcard_text, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    to_learn_data = pandas.DataFrame(to_learn)
    to_learn_data.to_csv(WORDS_TO_LEARN_LOC)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

# Flashcard
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front_img = PhotoImage(file="./resources/images/card_front.png")
flashcard_back_img = PhotoImage(file="./resources/images/card_back.png")
flashcard_background = canvas.create_image(400, 264, image=flashcard_front_img)
flashcard_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
flashcard_text = canvas.create_text(400, 264, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="resources/images/right.png")
wrong_image = PhotoImage(file="resources/images/wrong.png")

right_button = Button(image=right_image, width=100, height=100, highlightthickness=0, border=0, bg=BACKGROUND_COLOR,
                      command=next_card)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong_image, width=100, height=100, highlightthickness=0, border=0, bg=BACKGROUND_COLOR,
                      command=is_known)
wrong_button.grid(row=1, column=1)

# Keep a reference to the images to prevent garbage collection
right_button.image = right_image
wrong_button.image = wrong_image

next_card()

window.mainloop()
