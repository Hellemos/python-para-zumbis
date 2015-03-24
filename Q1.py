# -*- coding: utf-8 -*-
a = int(input('Entre com o lado A:'))
b = int(input('Entre com o lado B:'))
c = int(input('Entre com o lado C:'))

if a < b + c and b < a + c and c < a + b:
    print('É um triangulo')
    if a == b and b == c and a == c:
        print('E um triangulo equilatero')
    elif a == b != c or a == c != b or b == c != a:
        print('E um triangulo isoscele')
    else:
        print('E escaleno')
