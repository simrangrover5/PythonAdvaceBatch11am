
from tkinter import *

root = Tk()
root.config(bg="#D79F5C")
root.title("TkinterFile")
image = PhotoImage(file="icon.png")
root.iconphoto(False, image)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.minsize(width//2, height//2)
root.resizable(1, 0)

l1 = Label(root, text="Label1", fg="red", bg="black", font=(None, 20)) # font=(Family, size, style)
b1 = Button(root, text="Button1", fg="white", bg="black")


b1.pack()
l1.pack(side="left")
root.mainloop()
