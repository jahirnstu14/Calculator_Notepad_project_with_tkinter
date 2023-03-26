from tkinter import *
from PIL import Image, ImageTk

root=Tk()
#width x height
root.geometry("789x902")

# photo=PhotoImage(file="myscreenshotphoto.png")
# label=Label(image=photo)
# label.pack() 

#for jpg image import 
image= Image.open("Capture.JPG")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack() 



 #gui logic here
root.mainloop()
