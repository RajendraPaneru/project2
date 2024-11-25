from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1370x768+0+0")
        self.root.title("Help Desk")
        
        title_lbl=Label(text="Help Desk",font=("Arial",30,"bold"),bg="silver",fg="black")
        title_lbl.place(x=0,y=0,width=1370,height=75)
        
        
if __name__ == "__main__":
   root=Tk()
   obj=Help(root)
   root.mainloop() 