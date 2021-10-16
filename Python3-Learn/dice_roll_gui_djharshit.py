#! /usr/bin/env python3

"""
AUTHOR: Harshit Mehra
Python3 Concept: Dice Rolling implemented in tkinter GUI
GITHUB: https://github.com/djharshit

"""

# Importing the modules
import tkinter as tk
from tkinter import ttk
from random import choice

# The dice numbers
a = [1, 2, 3, 4, 5, 6]

# Creating a window
wind = tk.Tk()


def generate(*args):
    """It gives a random number from list."""

    n = choice(a)
    num_label.config(text=n)

# GUI program
wind.title('Dice Rolling')
wind.geometry('400x300')
wind.resizable(0, 0)

head_label = ttk.Label(wind, text='Dice Rolling', font=('Bodoni MT',
                       40, 'bold'))
head_label.pack(pady=10)


gen_button = ttk.Button(wind, text='Click', command=generate)
gen_button.pack(pady=10)

num_label = ttk.Label(wind, font=('Eras Bold ITC', 50), width=5)
num_label.pack(pady=10, anchor='c')

gen_button.bind('<Return>', generate)
wind.mainloop()
