# -*- coding: utf-8 -*-

"""
    6. Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
    Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois 
    inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a 
    saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim,
     a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. 
     ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores 
     de entrada todas as vezes que desejar.
"""

#converter a hora
def converteHora(hora, minuto):
	hora = input("Hora: ")
	minuto = input("Minuto: ")

	convert = input("Digite 'A' para converter para A.M ou 'P' para converter para P.M")
	if convert == 'a'.upper():
		print("Ainda vou fazer :p ")
	elif convert == 'p'.upper():
		

#resultado
def saidaHora():
	pass

if __name__ == '__main__':
    somaImposto(20, 30)
    

