
from datetime import date



dataAgoara = date.today()

dataAgoara = str(dataAgoara)

ano = ""
mes = ""
dia = ""
for n, c in enumerate(dataAgoara):
    if n < 4:
        ano += c
    if n > 4 and n <7:
        mes += c
    if n > 7:
        dia += c

novadata = f"{dia}/{mes}/{ano}"
print(novadata)
