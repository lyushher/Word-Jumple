from tkinter import*
import tkinter as tk
from random import choice
from random import shuffle

root = tk.Tk()
root.title('Word Jumple Game')
root.geometry('600x400')

frame = tk.Frame(root, bg="#FFFEF7")
frame.place(relwidth=1, relheight=1)

title = tk.Label(frame, text="Word Jumple Game", fg="#FFFEF7",bg="#c5c6ed" ,font=("Helvatica",40))
title.place(relx=0.20, rely=0.06)

word_title = tk.Label(frame, text="", fg="#7b5cc7", font=("Helvetica", 48))
word_title.place(rely=0.28, relx=0.32)

answerlabel = tk.Label(frame, text='', bg="#e4e4f7", font=("Gill Sans", 24))
answerlabel.place(rely=0.565, relx=0.77)

def shuffler():
    entry.delete(0, END)
    fruits = ['apple', 'strawberry', 'orange', 'blueberry', 'pineapple', 'banana', 'avocado', 'watermelon', 'cherry', 'lemon','grapes', ]
    answerlabel.config(text="")

    global word
    word = choice(fruits)

    break_apart_word = list(word)
    shuffle(break_apart_word)

    global shuffled_word
    shuffled_word = ''
    for letter in break_apart_word:
        shuffled_word += letter

    word_title.config(text=shuffled_word)

def answer():
    if word == entry.get():
        answerlabel.config(text='Correct!', fg="#12c00a")
    else:
        answerlabel.config(text='False!', fg="#e42e0c")

entry = tk.Entry(frame, bg="#e4e4f7", fg="#7b5cc7",font=("PT Serif", 24))
entry.place(rely=0.56, relx=0.25)

btnframe = tk.Frame(frame, bg="red")
btnframe.place(rely=0.7, relx=0.77)

answer = tk.Button(frame, text="Answer",fg="#7b5cc7", command = answer, font=("PT Serif",18))
answer.place(relx=0.13, rely=0.565, relwidth=0.12, relheight=0.09)

next = tk.Button(btnframe, text='Next→', fg="#7b5cc7",command = shuffler, font=("PT Serif",18))
next.grid()

shuffler()
root.mainloop()

