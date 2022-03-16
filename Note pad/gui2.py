import tkinter as tkr

root = tkr.Tk()

def myClick():
    myLabel =tkr.Label(root, text="Look! ")
    myLabel.pack()

myButton = tkr.Button(root, text="Click Me" ,padx=0, pady = 0, command =myClick, fg="black", bg="#fffff0")    #state=enabled

myButton.pack()

root.mainloop()
