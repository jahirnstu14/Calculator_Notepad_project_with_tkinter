from tkinter import *
root=Tk()
#width x height
root.geometry("600x400")
#maxisize of the window will be (width,height)
root.title("text editor ")

def myfunc():
    print("I am not a good person ")
#create dropdown button    
# mymenu=Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit",command=quit)

# root.config(menu=mymenu)

filemenu=Menu(root)

m1=Menu(filemenu, tearoff=0)
m1.add_command(label="New project", command =myfunc)
m1.add_command(label="Save", command =myfunc)
m1.add_separator()
m1.add_command(label="Save AS ", command =myfunc)
m1.add_command(label="print", command =myfunc)

root.config(menu=filemenu)
filemenu.add_cascade(label="File",menu=m1)

m2=Menu(filemenu, tearoff=0)
m2.add_command(label="Copy", command =myfunc)
m2.add_command(label="Paste", command =myfunc)
m2.add_separator()
m2.add_command(label="cut down ", command =myfunc)
m2.add_command(label="Find", command =myfunc)

root.config(menu=filemenu)
filemenu.add_cascade(label="Edit",menu=m2)




root.mainloop()
