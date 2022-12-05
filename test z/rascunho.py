def porPontoValor(conversao):
    conversaoAx = ''
    conversao = str(conversao)
    conversao = conversao.replace('.', ',')
    conversao = list(conversao)
    if len(conversao) >= 4 and len(conversao) <= 6:
        conversao.insert(-3, ".")
    elif len(conversao) >= 7 and len(conversao) <= 9:
        conversao.insert(-3, ".")
        conversao.insert(-7, ".")
    elif len(conversao) >= 10 and len(conversao) <= 12:
        conversao.insert(-3, ".")
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
    elif len(conversao) >= 13 and len(conversao) <= 15:
        conversao.insert(-3, ".")
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
    elif len(conversao) >= 16 and len(conversao) <= 18:
        conversao.insert(-3, ".")
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
    elif len(conversao) >= 19 and len(conversao) <= 21:
        conversao.insert(-3, ".")
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
        conversao.insert(-23, ".")
    elif len(conversao) >= 22 and len(conversao) <= 24:
        conversao.insert(-3, ".")
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
        conversao.insert(-23, ".")
        conversao.insert(-27, ".")
    elif len(conversao) >= 25 and len(conversao) <= 27:
        conversao.insert(-3, ".")
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
        conversao.insert(-23, ".")
        conversao.insert(-27, ".")
        conversao.insert(-31, ".")
    elif len(conversao) >= 27 and len(conversao) <= 30:
        conversao.insert(-3, ".")
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
        conversao.insert(-23, ".")
        conversao.insert(-27, ".")
        conversao.insert(-31, ".")
        conversao.insert(-35, ".")
    elif len(conversao) >= 31 and len(conversao) <= 33:
        conversao.insert(-3, ".")
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
        conversao.insert(-23, ".")
        conversao.insert(-27, ".")
        conversao.insert(-31, ".")
        conversao.insert(-35, ".")
        conversao.insert(-39, ".")
    elif len(conversao) >= 34 and len(conversao) <= 36:
        conversao.insert(-3, ".")
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
        conversao.insert(-23, ".")
        conversao.insert(-27, ".")
        conversao.insert(-31, ".")
        conversao.insert(-35, ".")
        conversao.insert(-39, ".")
        conversao.insert(-43, ".")
    elif len(conversao) >= 37 and len(conversao) <= 40:
        conversao.insert(-3, ".")
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
        conversao.insert(-23, ".")
        conversao.insert(-27, ".")
        conversao.insert(-31, ".")
        conversao.insert(-35, ".")
        conversao.insert(-39, ".")
        conversao.insert(-43, ".")
        conversao.insert(-47, ".")

    for c in conversao:
        conversaoAx += c

    return conversaoAx


a = 1000
a = porPontoValor(a)
print(a)


