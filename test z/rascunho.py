ancii = [" ", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6",
         "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "À", "Á", "Ã", "B", "C", "Ç", "D", "E", "È", "É", "F",
         "G", "H", "I", "Ì", "Í", "J", "K", "L", "M", "N", "O", "Ò", "Ó", "Õ", "P", "Q", "R", "S", "T", "U", "Ù", "Ú",
         "V", "W", "X", "Y", "Z", "[", "^", "_", "a", "à", "á", "ã", "b", "c", "d", "e", "è", "é", "f", "g", "h", "i",
         "ì", "í", "j", "k", "l", "m", "n", "o", "ò", "ó", "õ", "p", "q", "r", "s", "t", "u", "ù", "ú", "v", "w", "x",
         "y", "z", "{", "|", "}", "~", '"']

def corrigirErroNamberPositivo(n):

    while True:
        try:
            a = ancii[n]
            return n
        except:
            n = n-90
            return n

def corrigirErroNamberNegativo(n):
    a = ancii[n]
    a = ordSelf(a)
    return a

# converter caracter para numero
def ordSelf (getCaract):
    for n, caracter in enumerate(ancii):
        if getCaract == caracter:
            return n

# converter de cnúmero para caracter
def chrSelf (getNun):
    for n, caracter in enumerate(ancii):
        if getNun == n:
            return caracter

# criptogáfar
def criptografar(chave, mensagem):
    n =128
    novaMsm = ''
    for letra in mensagem:
        indice = ordSelf(letra)

        novaLetra = (indice+chave)

        while True:
            try:
                novaMsm += chrSelf(novaLetra)
                break
            except:
                print(novaLetra)
                novaLetra = corrigirErroNamberPositivo(novaLetra)

    return novaMsm

# descriptogáfar
def descriptografar(chave, mensagem):
    n = 128
    novaMsm = ''
    for letra in mensagem:
        indice = ordSelf(letra)

        novaLetra = (indice - chave)

        while True:
            try:
                novaMsm += chrSelf(novaLetra)
                break
            except:
                novaLetra = corrigirErroNamberNegativo(novaLetra)

    return novaMsm



mensagem = "Ndonda Daniel Matondo"
chave = len(mensagem)
#Ebojfm!Bmfy

#texto = criptografar(chave, mensagem)

#print(texto)
