# -*- coding: utf-8 -*-
i = 0
while i <= 10:
    nota = int(input('Entre com um nota: '))
    if(nota < 0) or (nota > 10):
        print('Valor inválido!')
    else:
        print('Valor correto!')
        break
    i += 1
    
    
    
