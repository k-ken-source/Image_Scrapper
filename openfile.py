from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image
       
def Openfile(dir_name):
    
    W=Tk()
    W.title("Pictures")
    W.filename = filedialog.askopenfilename(initialdir="/home/ham/"+dir_name,title="Select a file", filetypes=(("png files","*.*"),("all files","*.*")))
    filelocation=Label(W,text=W.filename)
    my_image=ImageTk.PhotoImage(Image.open(W.filename))
    image_label=Label(image=my_image)
    image_label.pack()
    filelocation.pack()

    W.mainloop()

if __name__=='__main__':
    i=input()
    root=Tk()
    p=Openfile(i)
    root.mainloop()
    

