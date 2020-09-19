# # import the module
# """ esto es un comentario """
# from tkinter import *


# top = tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()
import tkinter as tk
import random
from tkinter import *
combinations = []
checks = []
colors = ['blue', 'red', 'yellow', 'green', 'orange', 'cyan', 'purple', 'pink']
import random
import subprocess
from tkinter import messagebox
import sys
ms_heigt = 7
ms_widht = 4

class Application(Frame):

    button_idx = 0
    combination_number = 0

    def change_style(btn):
        color = random.choice(['red', 'blue', 'yellow', 'dark gray', 'purple', 'cyan', 'brown', 'orange'])
        btn.configure('Die.TButton', background=color)


    def change_color(self, btn):
        btn.configure(bg=self.tkvar2.get()) 
  

    def createWidgets(self):
        self.title = Label(self, text="Master-Mind")
        self.title.grid(row=0, column=1, pady=(10, 10))
        self.score = Label(self, text="")
        self.score.grid(row=1, column=0, padx=(50, 50))
        # Frame para combinaciones de colores
        self.center_block = Frame(self)
        self.center_block.grid(row=1, column=1, padx=(30, 30))
        self.color_menu = OptionMenu(self, self.tkvar2,  *colors)
        self.color_menu.config(font=('arial', 25, 'normal'))
        self.color_menu['menu'].config(font=('arial', 25, 'normal'))
        self.color_menu.place(x=20, y=100)
        for i in range (ms_heigt):
          buttons = []
          self.center_block.container = Frame(self.center_block)
          for j in range (self.ms_widht):
            self.center_block.container.button = Button(self.center_block, height = 3, width = 3, bg="gray")
            btn = self.center_block.container.button
            # btn.config(activebackground=btn.cget('background'))
            if j == 0:
              self.center_block.container.button.grid(padx=(70, 0))
            btn["command"] = lambda m=btn: self.change_color(m) 
            btn["state"] = "disable"         
            btn.grid(row=i, column=j)
            buttons.append(btn)
          combinations.append(buttons)
        
        # Frame para checks de colores
        self.right_block = Frame(self)
        self.right_block.grid(row=1, column=2)
        for i in range (ms_heigt):
          check = []
          self.right_block.container = Frame(self.right_block)
          for j in range (self.ms_widht):
            self.right_block.container.button = Button(self.right_block, height = 3, width = 3)
            btn2 = self.right_block.container.button
            btn2["command"] = lambda m=btn2: self.change_color(m)
            btn2["state"] = "disable"
            btn2.grid(row=i, column=j)
            check.append(btn2)
          checks.append(check)
        self.accept = Button(self, text="Accept", width=10, height=2)
        self.accept["command"] = self.check_code
        self.accept.grid(row=2, column=1, pady=(30, 50))
        

    def activate_row(self, row_num):
      for btn in combinations[row_num]:
        btn["state"] = "normal"

    def disable_row(self, row_num):
      for btn in combinations[row_num]:
        btn["state"] = "disable"

    def random_code(self):
      # self.disable_row(Application.combination_number)
      return sys.argv[1:]

    def check_code(self):
      my_combination = []
      for button in combinations[Application.combination_number]:
        my_combination.append( button["bg"])
      if "gray" in my_combination:
        messagebox.showinfo(title="Empty Spot!", message="You must fill all the spots")
        return
      self.disable_row(Application.combination_number)
      print(my_combination)
      if self.code == my_combination:
        messagebox.showinfo(title="You are the winner", message="Congrats! You cracked the code")
        subprocess.call("python3 main.py", shell=True)
        sys.exit()
      else:
        print("incorrecto")
        cp_code = list(enumerate(self.code[:]))
        cp_my_combination = list(enumerate(my_combination))
        # print((cp_code))
        # print((cp_my_combination))
        comprobation = []
        for i, my_color in cp_my_combination:
          for j, code_color in cp_code:
            if i == j and my_color == code_color:
              comprobation.append("black")
              cp_code[j] = (-1, "----")
              break
            if i != j and my_color == code_color:
              comprobation.append("white")
              cp_code[j] = (-1, "----")
              break
        print(comprobation)
        for i, c in enumerate(comprobation):
          checks[Application.combination_number][i]["bg"] = c 
      
      if Application.combination_number == ms_heigt - 1:
        messagebox.showinfo(title="Sorry you lose", message="Sorry! You didn't crack the code")
        subprocess.call("python3 main.py", shell=True)
        sys.exit()
      else:
        Application.combination_number += 1
      self.activate_row(Application.combination_number)
     

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack(fill=X, padx=0, pady=0)
        self.tkvar2 = tk.StringVar()
        self.tkvar2.set(colors[0])
        self.code = Application.random_code(self)
        self.ms_widht = len(self.code)
        self.createWidgets()
        self.activate_row(Application.combination_number)
        print(self.code)


if __name__ == '__main__':
  root = Tk()
  # tamaño de la ventana
  root.geometry('1200x1000')
  # titulo de la ventana
  app = Application(master=root)
  app.mainloop()
  root.destroy()