from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
fg = GREEN
checkmk = "✔"

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="./resources/images/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label.grid(column=1, row=0)

btn1 = Button(text="Start", highlightthickness=0)
btn1.grid(column=0, row=2)
btn2 = Button(text="Reset", highlightthickness=0)
btn2.grid(column=2, row=2)

checkmarks = Label(text=f"{checkmk}{checkmk}{checkmk}", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmarks.grid(column=1, row=3)

window.mainloop()