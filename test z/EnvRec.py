import os
import shutil
#proget = os.listdir('..\pythonProject')

#for pastas in proget:
#    print(pastas)
enviar = []
pegar = []
ProgetosGuardados = '../Progrtos Guardados'
local = '../pythonProject1'


while True:
    print("[1] - Enviar aqruivos")
    print("[2] - Pegar arquivos")
    print("[3] - Sair")
    op = int(input(": "))
    if op == 1:
        for n, file in enumerate(os.listdir()):
            enviar.append(file)
            print(" ", n + 1, file)

        ope = int(input("envia nº: "))
        ope -= 1
        shutil.move(enviar[ope], ProgetosGuardados)
        print(enviar[ope], "enviado comsucesso!")
        enviar.clear()

    elif op == 2:
        for n, file in enumerate(os.listdir(ProgetosGuardados)):
            pegar.append(file)
            print(" ", n + 1, file)

        ope = int(input("Pegar nº: "))
        ope -= 1

        rfile = ProgetosGuardados + '/' + pegar[ope]
        shutil.move(rfile, local)
        print(pegar[ope], "Pego comsucesso!")
        pegar.clear()

    else:
        break