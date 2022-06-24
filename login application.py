
from tkinter import*

import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import webbrowser





        #=================================================class Window1===================================================


class Window1:
    def __init__(self, master):
        self.master =master
        self.master.title(" Login System")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg ='grey')
        
        self.frame = Frame(self.master, bg ='grey')
        self.frame.pack()
        
        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.frame, text = ' Login System', font=('timenewroman',30,'bold'), bg='grey',
                              fg='black')
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)
        #====================================================================================================
        self.LoginFrame1 = LabelFrame(self.frame, width=1350, height=600
                               ,font=('arial',20,'bold'),relief='ridge',bg='grey', bd=20)
        self.LoginFrame1.grid(row=1, column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=1000, height=600
                               ,font=('arial',20,'bold'),relief='ridge',bg='grey', bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        #==============================Label And Entry=======================================================
        self.lblUsername=Label(self.LoginFrame1, text = 'Username',font=('arial',10,'bold'),bd=22,
                               bg='grey', fg='Cornsilk')
        self.lblUsername.grid(row=0,column=0)
        self.txtUsername=Entry(self.LoginFrame1,font=('arial',20,'bold'), textvariable =self.Username)
        self.txtUsername.grid(row=0,column=1)

        self.lblPassword=Label(self.LoginFrame1, text = 'Password',font=('arial',10,'bold'),bd=22,
                               bg='grey', fg='Cornsilk')
        self.lblPassword.grid(row=1,column=0)
        self.txtPassword=Entry(self.LoginFrame1,font=('arial',20,'bold'),show='*', textvariable =self.Password)
        self.txtPassword.grid(row=1,column=1)

        #==============================Buttons===============================================================

        self.btnLogin = Button(self.LoginFrame2, text = 'Login', width = 17,font=('arial',20,'bold'),
                               command =self.Login_System)
        self.btnLogin.grid(row=3,column=0, pady=20, padx=8)

        self.btnReset = Button(self.LoginFrame2, text = 'Reset', width = 17,font=('arial',20,'bold'),
                               command =self.Reset)
        self.btnReset.grid(row=3,column=1, pady=20, padx=8)

        self.btnExit = Button(self.LoginFrame2, text = 'Exit', width = 17,font=('arial',20,'bold'),
                              command =self.iExit)
        self.btnExit.grid(row=3,column=2, pady=20, padx=8)
        #==============================Buttons===========================================================
        
    def Login_System(self):
        if (self.Username.get() == "nes" and self.Password.get()=="1234"):
            self.Login_System = tkinter.messagebox.askyesno("Login Succed")
            self.newWindow = Toplevel(self.master)
            self.app = Windows2(self.newWindow)
            if self.Login_System > 0:
                self.master.destroy()
                command = self.new_window
            
            else:
                command = ""
                return
            
            
        
        else:
            tkinter.messagebox.askyesno("Login invalid ")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

        
        
           
    def Reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno( "Voulez vous sortir ?")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return
 
    def new_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Windows2(self.newWindow)

    
        
################==============================================class Window2==================================##############################

class Windows2():
    def __init__(self,master):
        
        self.master = Tk()
        self.master.title("My Application")
        self.master.geometry('1350x750+0+0')
        self.master.minsize(480, 360)
        #self.window.iconbitmap("logo.ico")
        self.master.config(background='grey')

        # initialization des composants
        self.frame = Frame(self.master, bg='grey')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)
    
        
 
    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create__button()
        self.create__button1()
        
        

    def create_title(self):
        label_title = Label(self.frame, text="Bienvenue sur l'application", font=("Courrier", 40), bg='grey',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, font=("Courrier", 25), bg='cadet blue',
                               fg='white')
        label_subtitle.pack()

    def create__button(self):
        yt_button = Button(self.frame, text="Algorithme supervisé", font=("Courrier", 25), bg='white', fg='cadet blue',
                           command=self.open)
        yt_button.pack(pady=25, fill=X)
        
        
        
    def create__button1(self):
       yt1_button = Button(self.frame, text="algorithme non supervisé", font=("Courrier", 25), bg='white', fg='cadet blue',
                           command=self.open1)
       yt1_button.pack(pady=25, fill=X)
        
          
          
   
        
    def open(self):
        self.newWindow = Toplevel(self.master)
        self.app = MyApp(self.newWindow)
        self.master.destroy()
        

    def open1(self):
        self.newWindow = Toplevel(self.master)
        self.app = Windows3(self.newWindow)
        self.master.destroy()
            
    
        

    
        
    




        #####################========================================class MyApp================################################

  

class MyApp:
    

    def __init__(self,master):
        
        self.master = Tk()
        self.master.title("Les algorithmes supervisés")
        self.master.geometry('1350x750+0+0')
        self.master.minsize(480, 360)
        #self.window.iconbitmap("logo.ico")
        self.master.config(background='grey')

        # initialization des composants
        self.frame = Frame(self.master, bg='grey')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)
    
        
 
    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create__button()
        self.create__button1()
        self.create__button2()
       
        

    def create_title(self):
        label_title = Label(self.frame, text="les algorithmes supervisés", font=("Courrier", 40), bg='grey',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, font=("Courrier", 25), bg='cadet blue',
                               fg='white')
        label_subtitle.pack()

    def create__button(self):
        yt_button = Button(self.frame, text="Naive_Bayes", font=("Courrier", 25), bg='white', fg='cadet blue',
                           command=self.open_naive)
        yt_button.pack(pady=25, fill=X)
        
        
        
    def create__button1(self):
          yt1_button = Button(self.frame, text="KNN", font=("Courrier", 25), bg='white', fg='cadet blue',
                           command=self.open_knn)
          yt1_button.pack(pady=25, fill=X)
          
          
    def create__button2(self):
          yt1_button = Button(self.frame, text="Quitter", font=("Courrier", 25), bg='white', fg='cadet blue',
                           command=self.quitter)
          yt1_button.pack(pady=25, fill=X)
          
          


    
    def open_naive(self):
        webbrowser.open_new("http://localhost:8888/notebooks/Desktop/projet%20foulle%20des%20donnees/naive%20bayes.ipynb")
        

    def open_knn(self):
        webbrowser.open_new("http://localhost:8888/notebooks/Desktop/projet%20foulle%20des%20donnees/knn.ipynb")
        
    def quitter(self):
        self.newWindow = Toplevel(self.master)
        self.app = Windows2(self.newWindow)
        self.master.destroy()


    

    


#======================================================================class windows3====================================#
class Windows3:
    

    def __init__(self,master):
        
        self.master = Tk()
        self.master.title("les algorithme non supervisés")
        self.master.geometry('1350x750+0+0')
        self.master.minsize(480, 360)
        self.master.config(background='grey')

        # initialization des composants
        self.frame = Frame(self.master, bg='grey')

        # creation des composants
        self.create_widgets()

        # empaquetage
        self.frame.pack(expand=YES)
    
        
 
    def create_widgets(self):
        self.create_title()
        self.create_subtitle()
        self.create__button()
        self.create__button1()
        

    def create_title(self):
        label_title = Label(self.frame, text="les algorithme non supervisés", font=("Courrier", 40), bg='cadet blue',
                            fg='white')
        label_title.pack()

    def create_subtitle(self):
        label_subtitle = Label(self.frame, font=("Courrier", 25), bg='cadet blue',
                               fg='white')
        label_subtitle.pack()

   
          
    def create__button(self):
        yt2_button = Button(self.frame, text="KMeans", font=("Courrier", 25), bg='white', fg='cadet blue',
                           command=self.open_kmeans)
        yt2_button.pack(pady=25, fill=X)
        
    def create__button1(self):
        yt2_button = Button(self.frame, text="Quitter", font=("Courrier", 25), bg='white', fg='cadet blue',
                           command=self.quitter)
        yt2_button.pack(pady=25, fill=X)
       

    

    def open_kmeans(self):
        webbrowser.open_new("http://localhost:8888/notebooks/Desktop/projet%20foulle%20des%20donnees/K-means.ipynb")
        


    def quitter(self):
        
        self.newWindow = Toplevel(self.master)
        self.app = Windows2(self.newWindow)
        self.master.destroy()

    

#=========================================================  main ============================================#
if __name__== '__main__':
    root = Tk()
    app = Window1(root)
    root.mainloop()
