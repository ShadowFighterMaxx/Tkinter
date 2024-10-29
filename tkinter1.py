from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("New Window")
root.geometry("400x400")
root.config(background="red")
upload = Image.open("img.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

l1 = Label(root ,pady = 10, image = image, bg = "white", fg = "blue")
l2 = Label(root ,pady = 10, text = "Hey User, Welcome To Denomination Counter", bg = "white", fg = "blue")
l1.pack()
l2.pack()
def display():
 Msgbox=   messagebox.showinfo("ALERT", "Do you want to calculate denominations?")
 if Msgbox == "ok":
  topwin()
b1 = Button(root, text = "Lets Get Started", command = display)
b1.pack()
def topwin():  
   top = Toplevel()
   top.title("Denominations Calculator")
   top.config(bg="light grey")
   top.geometry('600x350+50+50')

   label = Label(top, text = "Enter Amount", bg = "light grey")
   entry = Entry(top)
   lbl = Label(top, text = "Here are no of notes for each denomination", bg = "light grey")

   l1 = Label(top, text = "2000", bg = "light grey")
   l2 = Label(top, text = "500", bg = "light grey")
   l3 = Label(top, text = "200", bg = "light grey")

   t1 = Entry(top)
   t2 = Entry(top)
   t3 = Entry(top)
root.mainloop()