from tkinter import *
root=Tk()
#width x height
root.geometry("600x400")
f1=Frame(root, bg="grey",borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")
f2=Frame(root, bg="grey",borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill="x")
l = Label(f1,text="vs code frame")
l.pack(pady=130)
l=Label(f2, text="welcome to the sublime",font="Helvetica 16 bold",fg="red")
l.pack()
root.mainloop()
