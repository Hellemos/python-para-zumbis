# -*- coding: utf-8 -*-

"""
    5. Faça um programa com uma função chamada somaImposto. A função possui dois 
    parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa 
    em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” 
    o valor de custo para incluir o imposto sobre vendas.
"""

def somaImposto(taxaImposto, custo):
	calcImposto = custo + custo * taxaImposto * 0.01
	print("O valor eh: R$%.2f" %(custo) + ". Somado com o imposto de: %d " %(taxaImposto) +
	"resulta em: R$%.2f" % (calcImposto))

if __name__ == '__main__':
    somaImposto(20, 30)
    

