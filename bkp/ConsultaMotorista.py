#-------------------- IMPORTS --------------------
from tkinter import * 

#-------------------- TELA DE CONSULTA --------------------
class ConsultaMotorista: # cria a classe
    def __init__(self, master=None): #metodo construtor
        self.entrada_conteiner = Frame(master) #cria o conteiner entrada
        self.entrada_conteiner.pack()  #usa o gerenciador de geometria pack

        self.botao_conteiner = Frame(master) #cria o conteiner entrada
        self.botao_conteiner.pack()  #usa o gerenciador de geometria pack

        self.msg_conteiner = Frame(master) #cria o conteiner entrada
        self.msg_conteiner.pack()  #usa o gerenciador de geometria pack
        
        self.msg = Label(self.entrada_conteiner, text="Digite o código do veículo \n (Placa ou Frota): ", anchor="w", justify=LEFT)
        self.msg["font"]=("Verdana","12","bold" )
        self.msg.pack(side=LEFT)

        self.input = Entry(self.entrada_conteiner)
        self.input.pack(side=RIGHT)
        
        self.buscar = Button(self.botao_conteiner)
        self.buscar["text"] = " Buscar"
        self.buscar["font"] = ("Calibri", "8")
        self.buscar["width"] = 12
        self.buscar["command"] = self.getInput
        self.buscar.pack()


    def getInput(self):
        veiculo = self.input.get()

root = Tk() #instancia a classe Tk atraves da variavel
ConsultaMotorista(root) #passa a variavel root como parametro do metodo construtor
root.mainloop()