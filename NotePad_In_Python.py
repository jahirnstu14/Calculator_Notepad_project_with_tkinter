from tkinter import *
from tkinter .messagebox import showinfo
from tkinter .filedialog import askopenfilename, asksaveasfilename
import os 
def newFile():
    global file
    root.title("untitled")
    file=None
    TextArea.delete(1.0, END)
def openFile():
    global file
    file=asksaveasfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Document","*.txt")])
    if file=="":
        file=None
    
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

    
def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled",defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Document","*.txt")])
        if file=="":
            file=None

        else:
            #save as new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "- Notepad")

    else:
        #save the  file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()   
            
def quitApp():
    root.destroy()
def copy():
    TextArea.event_generate(("<<Copy>>"))
def cut():
    TextArea.event_generate(("<<Cut>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad","software is made by Md. Jahirul lslam")

           


if __name__=='__main__':
    #Basic tkinter setup 
    root=Tk()
    root.title("NotePad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("644x788")

    #add text area 
    TextArea=Text(root, font="lucida 13")
    file=None
    TextArea.pack(expand=True, fill=BOTH)

    #lets create a menubar
    MenuBar=Menu(root)

    #file menu starts 
    FileMenu=Menu(MenuBar, tearoff=0)

    #to add new file 
    FileMenu.add_command(label="New", command=newFile)
    #to open already existing file
    FileMenu.add_command(label="Open", command=openFile)
    # to save current file 
    FileMenu.add_command(label="Save", command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)

    MenuBar.add_cascade(label="File", menu=FileMenu)

#file menu ends 

#edit menu starts 

EditMenu= Menu(MenuBar, tearoff=0)
#to give a feature of cut, copy and paste 
EditMenu.add_command(label="Cut", command =cut)
EditMenu.add_command(label="Copy", command =copy)
EditMenu.add_command(label="Paste", command =paste)

MenuBar.add_cascade(label="Edit", menu=EditMenu)

#edit menu ends  
#Help menu starts 
HelpMenu=Menu(MenuBar, tearoff=0)
HelpMenu.add_command(label="About Notepad",command=about)

MenuBar.add_cascade(label="Help", menu=HelpMenu)
#help menu stops 
root.config(menu=MenuBar)
#adding scrollbar using rules 

Scroll = Scrollbar(TextArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArea.yview)
TextArea.config(yscrollcommand=Scroll.set)

root.mainloop()