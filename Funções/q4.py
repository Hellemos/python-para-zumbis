# -*- coding: utf-8 -*-

"""
    4. Faça um programa, com uma função que necessite de um argumento. 
    A função retorna o valor de caractere ‘P’, se seu argumento for positivo, 
    e ‘N’, se seu argumento for zero ou negativo.
"""

def valorDoArgumento(a):
	if a >= 1:
		return 'P'
	elif a == 0 or a <= 0:
		return 'N'

if __name__ == '__main__':
    print(valorDoArgumento(1))
    print(valorDoArgumento(0))
    print(valorDoArgumento(-2))
    print(valorDoArgumento(3))
    

