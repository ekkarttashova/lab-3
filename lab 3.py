from tkinter import Tk, Label, PhotoImage, Button, CENTER
from tkinter import ttk
import random
import pygame


def clicked():
    key = ''
    letters_list = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    number_list = '0123456789'
    for j in range(4):
        code = ''
        number = ''
        letter = ''
        for i in range(3):
            letter += random.choice(letters_list)
        number = random.choice(number_list)
        str_code = letter + number
        list_code = list(str_code)
        random.shuffle(list_code)
        code = ''.join(list_code)
        key += code + '-'
    key = key[:-1]
    lbl = Label(tab1, text=f'Ваш ключ: {key}', font=('Arial Bold', 30), relief="groove")
    lbl.grid(row=4)
    lbl.place(anchor=CENTER, relx=0.5, rely=0.5)


def play():
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play()


M_WIDTH = 1600
M_HIGHT = 1000
WIDTH = 1000
HIGHT = 500
window = Tk()
window.title('Key generator for Homescapes :)')
window.maxsize(M_WIDTH, M_HIGHT)
window.geometry(f"{WIDTH}x{HIGHT}")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Основное')
tab_control.add(tab2, text='Доп')
tab_control.pack(expand=1, fill='both')

image_game = PhotoImage(file="Homescapes.png")
background_label = Label(tab1, image=image_game)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

image_bg = PhotoImage(file="gif.gif")
background_label1 = Label(tab2, image=image_bg, border=50)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)

lbl_hi = Label(tab1, text='Генератор ключа', font=('Arial Bold', 40), relief="groove")
lbl_hi.grid(column=0, row=0)
lbl_hi.place(anchor=CENTER, relx=0.5, rely=0.1)

btn = Button(tab1, text='generate', bg='red', fg='black', command=clicked, border=0)
btn.grid(column=0)
btn.place(anchor=CENTER, relx=0.5, rely=0.35)

pygame.mixer.init()

my_button = Button(tab2, text="Play Song", font=("Helvetica", 32), command=play)
my_button.pack(pady=10)

window.mainloop()
