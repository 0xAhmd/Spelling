from autocorrect import Speller
import tkinter as tk
from tkinter import *

win = tk.Tk()

win.geometry('600x300')
win.title("Spell Checker")
win.resizable(False, False)

corrected = Label(win, font=("Myriad Pro", 16), bg="#0E0D12", fg='#FFFFFF', text="Correct Spelling is:")
corrected.place(x=30, y=205)

# Use Speller from autocorrect
spell_checker = Speller(lang='en')

def spell(*args):
    word = enter_kalam.get()
    right = spell_checker(word).capitalize()
    corrected.config(text="Correct Spelling is: " +right)

Icon = PhotoImage(file=r"C:\Users\abo7med\PycharmProjects\pythonProject1\PAYTHON\ICONS\language.png")
win.iconphoto(False, Icon)
win.configure(bg="#0E0D12")
heading = Label(win, text="Spell Checker", font=("trebuchet MS", 30), bg="#0E0D12", fg="#FFFFFF", borderwidth=2)
heading.pack(pady=(50, 0))
enter_kalam = Entry(win, justify="center", width=20, font=("Myriad Pro", 25), bg="White")
enter_kalam.pack(pady=10)
enter_kalam.focus()
button = Button(win, width=12, height=1, text="Check", bg="#A4FFAF", fg="Black", font=("Isra", 15), border=1, command=spell)
button.pack()
win.bind("<Return>", spell)
win.mainloop()
