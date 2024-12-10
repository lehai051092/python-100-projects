from tkinter import Tk, Canvas, PhotoImage, Button
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"

# Fetch Data
def read_data():
    return pandas.read_csv("data/japanese_words.csv", encoding="utf-8")

# Logic
def handle_wrong_click():
    data = read_data()
    df = pandas.DataFrame(data).fillna("").to_dict(orient="records")
    random_word = df[randint(0, len(df) - 1)]
    kanji = random_word.get('jp_kanji', "")
    hira_kata = random_word.get('jp_hira_or_kata', "")

    canvas.itemconfig(kanji_text, text=kanji)
    canvas.itemconfig(hira_kata_text, text=hira_kata)
    print(random_word)

# UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

img_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=img_front)

canvas.create_text(400, 150, text="Japanese", font=("Noto Sans JP", 30, "italic"))

kanji_text = canvas.create_text(400, 243, text="Kanji", font=("Noto Sans JP", 40, "bold"))

hira_kata_text = canvas.create_text(400, 313, text="Kata / Hira", font=("Noto Sans JP", 40, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

img_wrong = PhotoImage(file="images/wrong.png")
btn_wrong = Button(image=img_wrong, highlightthickness=0, command=handle_wrong_click)
btn_wrong.grid(column=0, row=1)

img_right = PhotoImage(file="images/right.png")
btn_right = Button(image=img_right, highlightthickness=0)
btn_right.grid(column=1, row=1)

window.mainloop()
