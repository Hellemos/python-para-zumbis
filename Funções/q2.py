# -*- coding: utf-8 -*-

"""
    2. Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
"""

def imprimir(a, b = []):
    b.append(a)	
    return b

if __name__ == '__main__':
    print(imprimir(1))
    print(imprimir(2))
    print(imprimir(3))
    print(imprimir(4))
    print(imprimir(5))
    print(imprimir(6))

