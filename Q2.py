# -*- coding: utf-8 -*-
ano = int(input('Entre com o ano: '))
if ano % 4 == 0 and ano % 100 != 0:
    print('É bissexto')
else:
    print('Nao eh bissexto')
