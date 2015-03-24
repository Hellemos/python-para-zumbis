i = 1
maior = 0
menor = 0
while i <= 3:
    n = int(input('Digite os numeros: '))
    if n > maior:
        maior = n
    else:
        if n <= menor:
            menor = n
    i += 1
print('Maior: %d' %(maior) + '\nMenor: %d' %(menor))
    
