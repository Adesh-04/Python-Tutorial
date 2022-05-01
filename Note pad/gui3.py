import tkinter as tkr
root = tkr.Tk()

e = tkr.Entry(root, width=50, borderwidth=5) #fg and bg
e.pack()
e.insert(0, "Enter :")

myButton = tkr.Button(root, text="Button", command = e.get())
myButton.pack()

root.mainloop()