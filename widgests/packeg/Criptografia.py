ancii = [" ", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4",
             "5", "6",
             "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "À", "Á", "Ã", "B", "C", "Ç", "D", "E", "È",
             "É", "F",
             "G", "H", "I", "Ì", "Í", "J", "K", "L", "M", "N", "O", "Ò", "Ó", "Õ", "P", "Q", "R", "S", "T", "U",
             "Ù", "Ú",
             "V", "W", "X", "Y", "Z", "[", "^", "_", "a", "à", "á", "ã", "b", "c", "d", "e", "è", "é", "f", "g",
             "h", "i",
             "ì", "í", "j", "k", "l", "m", "n", "o", "ò", "ó", "õ", "p", "q", "r", "s", "t", "u", "ù", "ú", "v",
             "w", "x",
             "y", "z", "{", "|", "}", "~", '"']

# esta fução e responsavel corrigir o erro de pedir um número positivo
def corrigirErroNamberPositivo(n):

    while True:
        try:
            a = ancii[n]
            return n
        except:
            n = n - (len(ancii) - 1)
            return n

# esta fução e responsavel corrigir o erro de pedir um número negativo
def corrigirErroNamberNegativo(n):
    a = ancii[n]
    a = ordSelf(a)
    return a

# converter caracter para numero
def ordSelf(getCaract):
    for n, caracter in enumerate(ancii):
        if getCaract == caracter:
            return n

# converter de cnúmero para caracter
def chrSelf(getNun):
    for n, caracter in enumerate(ancii):
        if getNun == n:
            return caracter

# criptogáfar
def criptografar(caracteres):
    chave = len(caracteres)
    caracterNovos = ''
    for caracter in caracteres:
        indice = ordSelf(caracter)

        valorNovaLetra = (indice + chave)

        while True:
            try:
                caracterNovos += chrSelf(valorNovaLetra)
                break
            except:
                valorNovaLetra = corrigirErroNamberPositivo(valorNovaLetra)

    return caracterNovos

# descriptogáfar
def descriptografar(caracteres):
    chave = len(caracteres)
    caracterNovos = ''
    for letra in caracteres:
        indice = ordSelf(letra)

        valorNovaLetra = (indice - chave)

        while True:
            try:
                caracterNovos += chrSelf(valorNovaLetra)
                break
            except:
                valorNovaLetra = corrigirErroNamberNegativo(valorNovaLetra)

    return caracterNovos
