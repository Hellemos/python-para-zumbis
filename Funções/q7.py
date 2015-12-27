# -*- coding: utf-8 -*-

"""
    Faça um programa que use a função valorPagamento para determinar o valor a ser pago 
    por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da 
    prestação e o número de dias em atraso e passar estes valores para a função 
    valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa 
    que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a 
    execução o programa deverá voltar a pedir outro valor de prestação e assim continuar 
    até que seja informado um valor igual a zero para a prestação. Neste momento o programa 
    deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor 
    total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte 
    forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, 
    cobrar 3 por cento de multa, mais 0,1 por cento de juros por dia de atraso.
"""

from datetime import date

#Calcular valor a pagar	
def valorPagamento(valorPrestacao, diasAtraso):
	if diasAtraso > 0:
		diasAtraso = diasAtraso + (diasAtraso * 0.03) + (0.001 * diasAtraso)
		valorPrestacao += diasAtraso
		print("Valor da prestação eh R$ %.2f centavos"%(valorPrestacao))
		print("-----------------------------------------")
	else:
		print("O valor pago será: %.2f " %(valorPrestacao))

if __name__ == '__main__':
	
	valorPrestacao = 5
	contador = 0
	quantPagas = 0

	while valorPrestacao != 0:
		
		#solicitando valor da prestação
		valorPrestacao = input("Digite o valor da prestação: ")

		#total das prestações
		contador += valorPrestacao

		#quantidade de prestações pagas
		quantPagas += 1
		
		hj = date.today()				
		if valorPrestacao == 0:
			print("--- Relatorio do dia ---")
			print(hj)
			print("-------------------------------------------")
			print("Total das prestacoes sem contar com as multas: ", contador)
			print("Quantidade de prestacoes pagas: %d " % (quantPagas - 1))
			break

		#solicitando os dias de atraso
		diasAtraso = input("Digite os dias em atraso: ")

		#fornecendo os valores para a função		
		valorPagamento(valorPrestacao, diasAtraso)

		

		
		
    

    

