
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import subprocess
colors = ['blue', 'red', 'yellow', 'green', 'orange', 'cyan', 'purple', 'pink']
class MakerApplication(Frame):

    button_idx = 0

    def btnClickFunction(self):
      for data in self.combination:
        if '#d9d9d9' in data['bg']:
          messagebox.showinfo(title="Sorry no empty spaces", message="No empty spaces, that's too hard for us")
          return
      
      arguments = " ".join([color['bg'] for color in self.combination])
      print("python3 mastermind.py {}".format(arguments))
      subprocess.call("python3 mastermind.py {}".format(arguments), shell=True)
      sys.exit()

    def reload(self):
      self.combination=[]
      list1 = root.grid_slaves()
      for l in list1:
        l.destroy()
      list2 = self.pack_slaves()
      for l in list2:
        l.destroy()
      self.createWidgets()

    def menu(self):
      subprocess.call("python3 main.py", shell=True)
      sys.exit()

    def change_color(self, btn):
        btn.configure(bg=self.tkvar2.get())      

    def createWidgets(self):
        ms_heigt = 1
        self.right_block = Frame(self)
        self.right_block.grid(row=1, column=2)
        self.right_block.pack(fill=X)
        self.title = Label(self, text='Mastermind', font=('arial', 72, 'normal')).place(x=0, y=0)

        self.player_name = Label(self, text='Code maker: create the code', font=('arial', 32, 'normal')).place(x=0, y=150)
        choices = [ 4, 5, 6]
        self.color_menu = OptionMenu(self, self.tkvar2,  *colors)
        self.color_menu.config(font=('arial', 25, 'normal'))
        self.color_menu['menu'].config(font=('arial', 25, 'normal'))
        self.color_menu.place(x=0, y=100)

        popupMenu = OptionMenu(self, self.tkvar,  *choices)
        popupMenu.config(font=('arial', 30, 'normal'))
        popupMenu['menu'].config(font=('arial', 30, 'normal'))
        popupMenu.place(x=650, y=150)
        ms_widht = self.tkvar.get()
        for i in range (ms_heigt):
          check = []
          self.right_block.container = Frame(self.right_block)
          for j in range (ms_widht):

            self.right_block.container.button = Button(self.right_block, height = 3, width = 3, activebackground = None, activeforeground= None, takefocus=0)
            self.right_block.container.button["command"] = lambda m=self.right_block.container.button: self.change_color(m)
            self.right_block.container.button.grid(row=i, column=j)
            if j == 0:
              self.right_block.container.button.grid(padx=(50, 20), pady=250, ipadx = 15, ipady = 15)
            else:
              self.right_block.container.button.grid(padx=20, pady=250, ipadx = 15, ipady = 15)
            self.combination.append(self.right_block.container.button)
        Button(root, text='Set Colors', bg='#2F4F4F', font=('arial', 36, 'normal'), borderwidth= 25, command=self.btnClickFunction).place(x=250, y=385)
        Button(root, text='Menu', bg='gray', font=('arial', 24, 'normal'), borderwidth= 12, command=self.menu).place(x=50, y=520)
        Button(root, text='Reload', font=('arial', 30, 'normal'),command=self.reload).place(x=600, y=80)
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.tkvar = tk.IntVar()
        self.tkvar2 = tk.StringVar()
        self.tkvar2.set(colors[0])
        self.tkvar.set(4) # set the default option
        self.pack(fill=X, padx=0, pady=0)
        self.combination=[]
        self.createWidgets()

if __name__ == '__main__':
  root = Tk()
  root.geometry('1200x1000')
  root.title('esto es una ventana')
  app = MakerApplication(master=root)
  app.master.title('esto es una ventana')
  app.mainloop()
  root.destroy()