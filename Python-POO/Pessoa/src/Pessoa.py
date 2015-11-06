'''
Created on 6 de nov de 2015

@author: hellen
'''

class Pessoa():
    
    #Método construtor para inicializar os atributos    
    def __init__(self, nome, cpf, profissao):
        self.__nome = nome
        self.__cpf = cpf
        self.__profissao = profissao
        
    def saudacao(self):
        print("Olá " + self.__nome)
    
    def setCpf(self, cpf):
        self.__cpf = cpf
    
    def getCpf(self):
        return "CPF: " + self.__cpf
    
    def setProfissao(self, profissao):
        self.__profissao = profissao
    
    def getProfissao(self):
        return "Profissão: " + self.__profissao