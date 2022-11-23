
"""while True:
    dolar = float(input("Valor Dolar: "))

    conversao = dolar*400

    print(conversao)""" #icon15 = QIcon()
                #icon15.addFile(u"../img/24x24/cil-volume-off.png", QSize(), QIcon.Normal, QIcon.Off)
                #QTimer.singleShot(200, lambda:  self.ui.toolButton.setIcon(icon15))
"""text = ''
while True:
    kz = float(input("Valor KZ: "))

    conversaof = kz*8482783.07

    print(f"{conversaof:.3f}")
    conversaof = str(f"{conversaof:.3f}").replace('.',',')
    conversao = list(conversaof)

    print(" a ",conversao, len(conversao))

    conversaoAx = ''
    conversao = list(conversao)
    if len(conversao) >= 7 and len(conversao) <= 10:
        conversao.insert(-7, ".")
    elif len(conversao) >= 11 and len(conversao) <= 13:
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
    elif len(conversao) >= 14 and len(conversao) <= 16:
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
    elif len(conversao) >= 17 and len(conversao) <= 19:
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
    elif len(conversao) >= 20 and len(conversao) <= 22:
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
        conversao.insert(-23, ".")
    elif len(conversao) >= 23 and len(conversao) <= 25:
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
        conversao.insert(-23, ".")
        conversao.insert(-27, ".")
    elif len(conversao) >= 26 and len(conversao) <= 28:
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
        conversao.insert(-23, ".")
        conversao.insert(-27, ".")
        conversao.insert(-31, ".")
    elif len(conversao) >= 28 and len(conversao) <= 31:
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
        conversao.insert(-23, ".")
        conversao.insert(-27, ".")
        conversao.insert(-31, ".")
        conversao.insert(-35, ".")
    elif len(conversao) >= 32 and len(conversao) <= 34:
        conversao.insert(-7, ".")
        conversao.insert(-11, ".")
        conversao.insert(-15, ".")
        conversao.insert(-19, ".")
        conversao.insert(-23, ".")
        conversao.insert(-27, ".")
        conversao.insert(-31, ".")
        conversao.insert(-35, ".")
        conversao.insert(-39, ".")
    elif len(conversao) >= 35 and len(conversao) <= 37:
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
    elif len(conversao) >= 38 and len(conversao) <= 40:
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

    print(conversaoAx)

"""
a = input("N: ")
saida = ''
anlz = False
a = list(a)
pre = 0
for n, c in enumerate(a):

    if n == 0:
        if c == ".":
            saida = "ERROR"
        else:
            saida += c
    else:

        if c == ".":
            pre+= 4

        if c == ",":
            pre+= 3

        if a.count("."):
            if c == ".":
                anlz = True
            else:
                saida += c

            if anlz:
                pre -= 1
        else:
            saida += c

if not pre == 0 and anlz == True:
    saida = "ERROR"


print(saida, pre, anlz)
