ancii = [" ", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6",
         "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "À", "Á", "Ã", "B", "C", "Ç", "D", "E", "È", "É", "F",
         "G", "H", "I", "Ì", "Í", "J", "K", "L", "M", "N", "O", "Ò", "Ó", "Õ", "P", "Q", "R", "S", "T", "U", "Ù", "Ú",
         "V", "W", "X", "Y", "Z", "[", "^", "_", "a", "à", "á", "ã", "b", "c", "d", "e", "è", "é", "f", "g", "h", "i",
         "ì", "í", "j", "k", "l", "m", "n", "o", "ò", "ó", "õ", "p", "q", "r", "s", "t", "u", "ù", "ú", "v", "w", "x",
         "y", "z", "{", "|", "}", "~", '"']

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

