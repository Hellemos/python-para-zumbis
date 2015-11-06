'''
Created on 6 de nov de 2015

@author: hellen
'''
from src.Pessoa import Pessoa

class Jose(Pessoa):

    def __init__(self):
        super().__init__("Jose", "456467", "Engenheiro")
    
    def passear(self):
        print("José gosta de passear!")
    
        