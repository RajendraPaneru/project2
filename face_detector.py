from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Face_Detector:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1370x768+0+0")
        self.root.title("Face Detector")
        
        #----title and background image-----------
        
        img1=Image.open(r"C:\Users\dell\OneDrive\Desktop\Project2\college-images\background2.jpg")
        img1=img1.resize((1370,568),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        bg_img=Label(self.root,image=self.photoimg1)
        bg_img.place(x=0,y=100,width=1370,height=568)
        title_lbl=Label(bg_img,text="Face Detector",font=("Arial",30,"bold"),bg="silver",fg="black")
        title_lbl.place(x=0,y=0,width=1370,height=50)
        
        
        
        #----face detector img and button-----
        
        img_left=Image.open(r"C:\Users\dell\OneDrive\Desktop\Project2\college-images\facedetector.jpg")
        img_left=img_left.resize((356,356),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(bg_img,image=self.photoimg_left,cursor="hand2")
        f_lbl.place(x=500,y=75,width=356,height=356)
        
        
        b1=Button(bg_img,text="Detect Face",command=self.face_recog,cursor="hand2",font=("arial",20,"bold"),bg="darkgreen",fg="white")
        b1.place(x=500,y=430,width=358,height=50)
        
        
    def face_recog(self):
        def draw_boundary(img,classifier,scalefactor,minNeighbour,color,text,clf):
            gray_image=cv2.cvtcolor(img,cv2.COLOR_BRG2GRA)
            features=classifier.detectMultiScale(gray_image,scalefactor,minNeighbour)
                
            coord=[]
                
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                    
                conn=mysql.connector.connect(host="localhost",username="root",password="xCx@#3219669",database="project2")
                my_cursor=conn.cursor()
                    
                    
                    
                    
                my_cursor.execute("select Name from student_table where ID="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                    
                my_cursor.execute("select ID from student_table where ID="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                    
                    
                my_cursor.execute("select Dep from student_table where ID="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                    
                if confidence>77:
                    cv2.putText(img,f"ID:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                        
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
                            
            return coord                    

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
            
        video_cap=cv2.VideoCapture(0)
            
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("welcome to face recognition",img)
                
            if cv2.waitKey(1)==13:
                break
            video_cap.release()
            cv2.destroyAllWindows()
        
        
        
if __name__ == "__main__":
   root=Tk()
   obj=Face_Detector(root)
   root.mainloop() 