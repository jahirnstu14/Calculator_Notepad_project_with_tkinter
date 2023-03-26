from tkinter import *
root=Tk()

def getvals():
    print("data is submitted ")
#width x height
root.geometry("600x400")
#heading
Label(root, text="Welcome to Harry Travels", font="comicsansms 13 bold",pady=15).grid(row=0,column=3)

# text for our form

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmode = Label(root, text="Paymentmode")

# pack text for our form

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2) 

# tkinter Variable for storing

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicevalue=IntVar()

# entry for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)


# packing the entries 

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmodeentry.grid(row=5,column=3)

# checking  and packing it 

foodservice = Checkbutton(text="want to prebook your meals?",variable = foodservicevalue)
foodservice.grid(row=6, column=3)

# Button and packing it and assining it a command 

Button(text="Submit",command=getvals).grid(row=7, column=3)






 #gui logic here
root.mainloop()
