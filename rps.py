import tkinter as tk
from random import choice
from tkinter import messagebox

def determine_winner(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = choice(choices)
    if user_choice == computer_choice:
         msgbox = messagebox.showinfo("Alert", "ITS A DRAW!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        msgbox = messagebox.showinfo("Better Luck!", "You Lost")
    else:
       msgbox = messagebox.showinfo("Good Job!", "You Won")

def play(choice):
    determine_winner(choice)

root = tk.Tk()
root.title("Rock Paper Scissors")

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.pack()

button_frame = tk.Frame(root)
button_frame.pack()
buttons = ['rock', 'paper', 'scissors']
for b in buttons:
    tk.Button(button_frame, text=b.capitalize(), command=lambda b=b: play(b)).pack(side='left')
root.mainloop()
