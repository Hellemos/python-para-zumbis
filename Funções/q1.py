# -*- coding: utf-8 -*-

"""1. Faça um programa para imprimir:
	1
	2   2
	3   3   3
	.....
	n   n   n   n   n   n  ... n
"""


def imprimir(a, b = None):
	if b is None:
		b = []
	b.append(a)
	c = b * a
	return c
	

if __name__ == '__main__':
	print(imprimir(1))
	print(imprimir(2))
	print(imprimir(3))
	print(imprimir(4))
	print(imprimir(5))
	print(imprimir(6))
 


