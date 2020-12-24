
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
root.mainloop()
