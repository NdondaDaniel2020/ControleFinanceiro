
class Criptografia:
    def __init__(self):
        self.ancii = [" ", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4",
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

    def corrigirErroNamberPositivo(self, n):

        while True:
            try:
                a = self.ancii[n]
                return n
            except:
                n = n - (len(self.ancii) - 1)
                return n

    def corrigirErroNamberNegativo(self, n):
        a = self.ancii[n]
        a = self.ordSelf(a)
        return a

    # converter caracter para numero
    def ordSelf(self, getCaract):
        for n, caracter in enumerate(self.ancii):
            if getCaract == caracter:
                return n

    # converter de cnúmero para caracter
    def chrSelf(self, getNun):
        for n, caracter in enumerate(self.ancii):
            if getNun == n:
                return caracter

    # criptogáfar
    def criptografar(self, caracteres):
        chave = len(caracteres)
        caracterNovos = ''
        for caracter in caracteres:
            indice = self.ordSelf(caracter)

            valorNovaLetra = (indice + chave)

            while True:
                try:
                    caracterNovos += self.chrSelf(valorNovaLetra)
                    break
                except:
                    valorNovaLetra = self.corrigirErroNamberPositivo(valorNovaLetra)

        return caracterNovos

    # descriptogáfar
    def descriptografar(self, caracteres):
        chave = len(caracteres)
        caracterNovos = ''
        for letra in caracteres:
            indice = self.ordSelf(letra)

            valorNovaLetra = (indice - chave)

            while True:
                try:
                    caracterNovos += self.chrSelf(valorNovaLetra)
                    break
                except:
                    valorNovaLetra = self.corrigirErroNamberNegativo(valorNovaLetra)

        return caracterNovos

    