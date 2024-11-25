from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1370x768+0+0")
        self.root.title("Attendance")
        
if __name__ == "__main__":
   root=Tk()
   obj=Attendance(root)
   root.mainloop() 