from tkinter import *

def getvals():
    print(f"the value of username is {uservalue.get()}")
    print(f"the value of password is {passvalue.get()}")
    
root=Tk()
#width x height
root.geometry("600x400")
user=Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid(row=1)

# variable classes in tkinter
# Boolen, DoubleVar, Intvar, StringVar

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root, textvariable = uservalue)
passentry=Entry(root, textvariable=passvalue)

Button(text="Sumit", command=getvals).grid()

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)
root.mainloop()
