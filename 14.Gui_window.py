from tkinter import *

def  harry(event):
    print(f"you clicked on the button at {event.x},{event.y}")
root=Tk()
root.title("events handling ")
root.geometry("644x334")

Widget=Button(root, text="click me please")
Widget.pack()

Widget.bind('<Button-1>', harry)
Widget.bind('<Double-1>', quit)

 #gui logic here
root.mainloop()
