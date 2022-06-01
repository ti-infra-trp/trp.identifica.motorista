#-----------   IMPORTS   ----------- 
from pickletools import TAKEN_FROM_ARGUMENT4
from tkinter import * 



#-----------    TELA DE LOGIN   -----------    
LoginScreen = Tk()  

LoginScreen.title("Controle de Acesso")  
LoginScreen.geometry("456x216")   
LoginScreen.iconbitmap('D:\\trp.identifica.motorista\\perola_icon.ico')
LoginScreen.configure(background='white') 
LoginScreen.resizable(0, 0)    

user= Label(LoginScreen,background='white', text = "Usuário : ").place(x = 40, y = 66)   
user_input = Entry(LoginScreen, width = 25).place(x = 110, y = 66)     

password = Label(LoginScreen, background='white', text = "Senha : ").place(x = 40, y = 92)   
password_entry = Entry(LoginScreen, show='*', width = 25).place(x = 110, y = 92)       

bg = PhotoImage(file = "D:\\trp.identifica.motorista\\autentication_icon.png") 
autenticationImage = Label(LoginScreen, background='white', image = bg) 
autenticationImage.place(x = 320, y = 40)

acess_button = Button(LoginScreen, text = "Acessar", width=9, height=2).place(x = 151, y = 130)  
LoginScreen.mainloop() 