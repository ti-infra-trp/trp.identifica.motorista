from pickletools import TAKEN_FROM_ARGUMENT4
from tkinter import * 

  
  
login = Tk()  
login.title("Gerenciamento de Controle de Acesso - Rotinas Auxiliares")  
login.geometry("392x216")       
user= Label(login, text = "Usuário : ").place(x = 40, y = 60)   
user_input = Entry(login, width = 30).place(x = 110, y = 60)       
password = Label(login, text = "Senha : ").place(x = 40, y = 100)   
password_entry = Entry(login, width = 30).place(x = 110, y = 100)       
acess_button = Button(login, text = "Acessar").place(x = 40, y = 130)      
login.mainloop() 