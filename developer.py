from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1370x768+0+0")
        self.root.title("Developers")
        
        
if __name__ == "__main__":
   root=Tk()
   obj=Developer(root)
   root.mainloop() 