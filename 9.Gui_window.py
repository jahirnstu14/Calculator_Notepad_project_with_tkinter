from tkinter import *
root=Tk()
#width x height
root.geometry("600x400")
def hello():
    print("how are you?")

def name():
    print("My name is shanto")
frame=Frame(root, bg="grey",borderwidth=6, relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")
b1=Button(frame, fg="red", text="print now",command=hello )
b1.pack(side=LEFT,padx=23)
b2=Button(frame, fg="red", text="print now name",command=name)
b2.pack(side=LEFT,padx=23 )
b3=Button(frame, fg="red", text="print now")
b3.pack(side=LEFT,padx=23)
b4=Button(frame, fg="red", text="print now")
b4.pack(side=LEFT,padx=23)

root.mainloop()
