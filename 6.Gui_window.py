from tkinter import *
root=Tk()
root.geometry("600x400")

root.title("My GUI")

# important Label options
# text- adds the text 
# bd - background
# fg - foreground 
# font - sets the font 
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED,GROOVE, RIDGE

title_label = Label(text = '''
Abdul Rashid Salim Salman Khan is an Indian 
\nfilm actor, producer, occasional playback singer and television personality. In a film career spanning 
\nalmost thirty years, Khan has received numerous awards, including two National Film Awards as a film 
\nproducer, and two Filmfare Awards for acting. He has a significant following in Asia and the Indian 
\ndiaspora worldwide, and is cited in the media as one of the most commercially successful actors of Indian 
\n''',bg="red", fg="blue",padx=30, pady=50,font="comicsansms 9 bold",borderwidth=3, relief=SUNKEN)



# Important Pack options
# anchor = nw means north and west side 
# side = top, bottom, left, right where default reamin top
# fill
# padx
# pady
# title_label.pack(side=BOTTOM ,anchor ="se", fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)

title_label.pack()

root.mainloop()
