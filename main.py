from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title('Flashy - Flashcard app')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file='images/card_front.png')
canvas.create_image(400, 263, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)

r_btn_img = PhotoImage(file='images/right.png')
right_button = Button(image=r_btn_img, highlightthickness=0)
right_button.grid(column=1, row=1)

w_btn_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=w_btn_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

window.mainloop()