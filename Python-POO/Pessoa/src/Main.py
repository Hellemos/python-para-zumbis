'''
Created on 6 de nov de 2015

@author: hellen
'''
from src.Pessoa import Pessoa
from src.Jose import Jose

if __name__ == '__main__':
    pes = Pessoa("Maria","","")
    pes.saudacao()
    pes.setCpf("123445576")
    print(pes.getCpf())
    pes.setProfissao("Analista de Sistemas")
    print(pes.getProfissao())
    
    print("\n----------------------------\n")
    
    jose = Jose()
    jose.saudacao()
    jose.passear()
    print(jose.getCpf())
    print(jose.getProfissao())
    
    
    