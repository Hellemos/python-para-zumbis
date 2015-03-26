# -*- coding: utf-8 -*-
i = 0
while i <= 10:
    usuario = raw_input('Usuário: ')
    senha = raw_input('Senha: ')
    if usuario == senha:
        print('Os nomes de usuario e senha nao podem ser iguais!')
    else:
        print('Sucesso!')
        break
    i += 1


