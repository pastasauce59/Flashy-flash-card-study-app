from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv('data/french_words.csv')
# print(data['French'][0])
df = data.to_dict(orient='records')
# print(df[0]['French'])
current_card = {}



def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(df)
    word = current_card['French']
    canvas.itemconfig(canvas_img, image=front_card_img)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=word, fill='black')
    timer = window.after(3000, flip_card)


def flip_card():
    english_word =  current_card['English']
    canvas.itemconfig(canvas_img, image=back_card_img),
    canvas.itemconfig(card_title, text='English', fill='white'),
    canvas.itemconfig(card_word, text=english_word, fill='white')
    
    
window = Tk()
window.title('Flashy - Flashcard app')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file='images/card_front.png')
back_card_img = PhotoImage(file='images/card_back.png')
canvas_img = canvas.create_image(400, 263, image=front_card_img)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 40, 'italic'), fill='black')
card_word = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'), fill='black')
canvas.grid(column=0, row=0, columnspan=2)

r_btn_img = PhotoImage(file='images/right.png')
right_button = Button(image=r_btn_img, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

w_btn_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=w_btn_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)


next_card()

window.mainloop()