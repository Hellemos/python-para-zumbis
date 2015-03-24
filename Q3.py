# -*- coding: utf-8 -*-
peso = float(input('Entre com o peso: '))
excesso = 0
multa = 0
if peso > 50:
    excesso = peso - 50
    multa = 4 * excesso
    print('Voce excedeu %d kg' %(excesso) + '\nO valor da multa eh: R$ %.2f' %(multa))
else:
    print('Voce esta dentro do regulamento! \nExcesso: %d kg \nMulta: R$ %.2f' %(excesso, multa))
   
    
