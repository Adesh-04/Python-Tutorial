import tkinter as tkr

root = tkr.Tk() #Main

MyLabel = tkr.Label(root, text="Hello")

MyLabel1 = tkr.Label(root, text="world")

MyLabel.grid(row=0, column=0)
MyLabel1.grid(row=1, column=10)

root.mainloop()