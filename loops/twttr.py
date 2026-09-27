def genz():
    string = input("Input: ")
    # Junta apenas as letras que NÃO são vogais
    print(''.join([l for l in string if l.lower() not in 'aeiou']))

genz()