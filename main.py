from tkinter import *
root = Tk()
root.title("New Window")
root.geometry("400x400")
root.config(background="red")


l1 = Label(root ,pady = 10, text = "Welcome To Python Tkinter", bg = "white", fg = "blue")
l2 = Label(root ,pady = 10, text = "Enter Your Name", bg = "white", fg = "blue")
l1.pack()
l2.pack()
e1 = Entry(root)
e1.pack()
def display():
    name = e1.get()
    t1 = "Welcome "+ name
    l3 = Label(root, text = t1)
    l3 .pack()
b1 = Button(root, text = "Show", command = display)
b1.pack()
root.mainloop()