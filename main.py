#MARK 1 
from tkinter import messagebox
from tkinter import *
import tkinter.messagebox
from bs4 import BeautifulSoup 
import requests
from PIL import Image 
import os 
from io import BytesIO
from tkinter import scrolledtext  

#############################My Fuctions Import ################
import scrapper
import openfile

class StdRedirector():
    def __init__(self, text_space):
        self.text_space = text_space

    def write(self, string):
        self.text_space.config(state=NORMAL)
        self.text_space.insert("end", string)
        self.text_space.see("end")
        self.text_space.config(state=DISABLED)

################################################################################# Interface using class so that can be imporved later (part2)

class FirstFrame:
    def __init__(self,root):
        self.root = root

        root.geometry('650x600')
        root.title("Scrapper")
        root.configure(background='dark grey')
        

##########################################################Frames : Need three frames for now
        self.frameupper = Frame(root)
        self.frameupper.pack()

        self.frameMiddle = Frame(root)
        self.frameMiddle.pack()

        self.frameBottom= Frame(root)
        self.frameBottom.pack(side=BOTTOM)

        self.w=Scrollbar(root)



##################Frames Complete###########################################################################################################


        ##Frame1 Label:
        self.title=Label(self.frameupper,text='IMAGE SCRAPPER',font='Chandas',anchor=N,bd=10,bg='dark grey',fg='dark green')
        self.title.pack(fill=X)
        
        self.input1=Entry(self.frameMiddle,bg='grey',fg='white')
        self.input1.grid(row=4,column=6)

        self.label=Label(self.frameMiddle,text="Search For :")
        self.label.grid(row=4,column=2)
        
        self.button=Button(self.frameBottom,text="Scrape",command =self.Command1)
        self.button.pack(side=LEFT)

        self.button2=Button(self.frameBottom,text='Open in Folder',command=self.Command2)
        self.button2.pack(side=RIGHT)



##################################################################redirecting output to textbox##########
        self.text_box = Text(root,bg='black',fg='white')
        self.text_box.pack()

       
        sys.stdout = StdRedirector(self.text_box)
        sys.stderr = StdRedirector(self.text_box) 



#####################################################################################MY Commands              

    def mess(self):
        self.message=messagebox.showinfo("Information,Getting Images Please Wait!!!!\n This could take some time, depending on your Connection")
        self.message.pack()
    def Command1(self):
        
        i=self.input1.get()
        scrapper.Scrapper(i)
        
    def Command2(self):
        i=self.input1.get()
        search=i.replace(" ","_",).lower()
        openfile.Openfile(search)
##################################################################################################################################################################

Window = Tk()
obj=FirstFrame(Window)
Window.mainloop()
