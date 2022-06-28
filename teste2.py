#-------------------- IMPORTS --------------------
from tkinter import *

#-------------------- TELA DE CONSULTA --------------------
class Application: # cria a classe
    def __init__(self, master=None): #metodo construtor
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master) #cria o conteiner 
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()  #usa o gerenciador de geometria pack

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Digite o código do veículo \n (Placa ou Frota): ")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.entrada = Entry(self.segundoContainer)
        self.entrada["width"] = 30
        self.entrada["font"] = self.fontePadrao
        self.entrada.pack(side=LEFT)

        self.buscar = Button(self.terceiroContainer)
        self.buscar["text"] = "Buscar"
        self.buscar["font"] = ("Calibri", "8")
        self.buscar["width"] = 12
        self.buscar["command"] = self.consulta
        self.buscar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método consulta 
    def consulta(self):
        entrada = self.entrada.get()
        self.mensagem["text"] = entrada
 
root = Tk() #instancia a classe Tk atraves da variavel
Application(root) #passa a variavel root como parametro do metodo construtor
root.mainloop()