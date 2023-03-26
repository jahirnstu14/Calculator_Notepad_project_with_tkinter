from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    elif text == "clear":
        scvalue.set("0")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
root=Tk()

root.geometry("250x450")
root.title("Calculator")
root.wm_iconbitmap("2344132.ico")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue, font="lucida 20 ")
screen.pack(fill=X,ipadx=8, padx=10, pady=10)

f =Frame(root, bg="grey")
b = Button(f, text="9", padx=10, pady=5, font="lucida 12 bold",bg="red")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=10, pady=5, font="lucida 12 bold",bg="red")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=10, pady=5, font="lucida 12 bold",bg="red")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

f.pack()

f =Frame(root, bg="grey")
b = Button(f, text="6", padx=10, pady=5, font="lucida 12 bold",bg="green")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=10, pady=5, font="lucida 12 bold",bg="green")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=10, pady=5, font="lucida 12 bold",bg="green")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

f.pack()

f =Frame(root, bg="grey")
b = Button(f, text="3", padx=10, pady=5, font="lucida 12 bold",bg="brown")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=10, pady=5, font="lucida 12 bold", bg="brown")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=10, pady=5, font="lucida 12 bold", bg="brown")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

f.pack()
f =Frame(root, bg="grey")
b = Button(f, text="0", padx=10, pady=5, font="lucida 11 bold", bg="blue")
b.pack(side=LEFT, padx=20.5,pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=10, pady=5, font="lucida 12 bold", bg="blue")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=11, pady=5, font="lucida 13 bold", bg="blue")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)
f.pack()
f =Frame(root, bg="grey")
b = Button(f, text="/", padx=10, pady=5, font="lucida 10 bold", bg="red")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=10, pady=5, font="lucida 12 bold", bg="red")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=10, pady=5, font="lucida 13 bold", bg="red")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

f.pack()
f =Frame(root, bg="grey")
b = Button(f, text="C", padx=5, pady=5, font="lucida 11 bold", bg="yellow")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=5, pady=5, font="lucida 13 bold", bg="yellow")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="clear", padx=5, pady=5, font="lucida 12 bold", bg="yellow")
b.pack(side=LEFT, padx=18,pady=12)
b.bind("<Button-1>", click)

f.pack()
root.mainloop()
