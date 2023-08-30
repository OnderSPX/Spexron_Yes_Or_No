from tkinter import *
from tkinter import messagebox
import random

def no():
    messagebox.showinfo("Thank you", "Teşekkür ederim")
    quit()

def motionMouse(event):
    btnYes.place(x=random.randint(0, 580), y=random.randint(0, 500))

root = Tk()
root.geometry("600x600")
root.title("SPEXRON YES OR NO")
root.resizable(width=False, height=False)
root.configure(bg='white')

label = Label(root, text='BURAYA SORU YAZILIR ?', font='Arial 20 bold', bg='white')
label.pack()

btnYes = Button(root, text='No', font="Arial 20 bold", command=no)
btnYes.place(x=170, y=100)
btnYes.bind('<Enter>', motionMouse)

btnNo = Button(root, text='Yes', font="Arial 20 bold", command=root.quit)
btnNo.place(x=350, y=100)

root.mainloop()
