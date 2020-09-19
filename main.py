#!/usr/bin/python3
"""
Main menu
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from codemaker import MakerApplication
from tkinter import * 
import sys
import subprocess
import random

# this is the function called when the button is clicked
def btnClickFunction():
  """ Starts the game 
  """
  if (CbeCheckboxVariable.get() == 1):
    ms_width = rbDifficult.get() + 3
    colors = ['blue', 'red', 'yellow', 'green', 'orange', 'cyan', 'purple', 'pink']
    colors_code = []
    for i in range(ms_width):
      n = random.randint(0, len(colors) - 1)
      colors_code.append(colors[n])
    print("Selected play vs AI level {}".format(rbDifficult.get()))
    arguments = " ".join(colors_code)
    print("python3 mastermind.py {}".format(arguments))
    root.wm_state('iconic')
    subprocess.call("python3 mastermind.py {}".format(arguments), shell=True)
  elif  (CbeCheckboxVariable.get() == 2):
    root.wm_state('iconic')
    print("Selected play vs Friend")
    subprocess.call("python3 codemaker.py", shell=True)
    sys.exit()
  else:
     messagebox.showinfo(title="Please select a gamemode", message="There's no secret mode, choose between playing with friends or AI")

# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValueAI():
	checkedOrNot = cbPlayvsAIVariable.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCheckboxValueFriend():
	checkedOrNot = cbPlayFriendVariable.get()
	return checkedOrNot


# this is a function to get the selected radio button value
def getRadioButtonValue():
	buttonSelected = rbDifficult.get()
	return buttonSelected

root = Tk()
#this is the declaration of the variable associated with the checkbox
CbeCheckboxVariable = tk.IntVar()


#this is the declaration of the variable associated with the radio button group
rbDifficult = tk.IntVar()

def CheckboxSelected():
  return
  
def DifficultChanged():
  return
# This is the section of code which creates the main window
root.geometry('800x600')
root.configure(background='#A9A9A9')
root.title('Mastermind')

# This is the section of code which creates the a label
Label(root, text='Created with love by @Nathaly Sotomayor Ampudia @Santiago Peña @Emma Navarro @Ricardo Alfonso Camayo Erazo @David Orejuela', wraplength=500, bg='#A9A9A9', font=('arial', 10, 'normal')).place(x=200, y=20)


# This is the section of code which creates the a label
Label(root, text='Mastermind', bg='#A9A9A9', font=('arial', 36, 'normal')).place(x=285, y=81)


# This is the section of code which creates a button
Button(root, text='Play', bg='#2F4F4F', font=('arial', 36, 'normal'), borderwidth= 25, command=btnClickFunction).place(x=340, y=385)


# This is the section of code which creates a checkbox
cbFriendPlay=Checkbutton(root, text='Play vs Friend', variable=CbeCheckboxVariable, bg='#A9A9A9', command=CheckboxSelected, onvalue=2, font=('arial', 24, 'normal'))
cbFriendPlay.place(x=500, y=161)


# This is the section of code which creates a checkbox
cbPlayvsAI=Checkbutton(root, text='Play vs A.I', variable=CbeCheckboxVariable, command=CheckboxSelected, bg='#A9A9A9',onvalue=1, font=('arial', 24, 'normal'))
cbPlayvsAI.place(x=75, y=161)
CbeCheckboxVariable.set(1)

# This is the section of code which creates a group of radio buttons
frame=Frame(root, width=0, height=0, bg='#A9A9A9')
frame.place(x=95, y=221)
ARBEES=[
('Easy', 1), 
('Medium', 2), 
('Hard', 3), 
]
for text, mode in ARBEES:
	rbDifficulta=Radiobutton(frame, text=text, variable=rbDifficult, value=mode, command=DifficultChanged, bg='#A9A9A9', font=('arial', 24, 'normal')).pack(side='top', anchor = 'w')
rbDifficult.set(1)

root.resizable(False, False)
root.mainloop()
