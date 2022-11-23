import requests

requesicao = requests.get("https://economia.awesomeapi.com.br/json/last/EUR-AOA,USD-AOA")

requesicao_json = requesicao.json()
dolar = requesicao_json["USDAOA"]["bid"]
euro = requesicao_json["EURAOA"]["bid"]
# bicons = requesicao_json["BTCBRL"]["bid"]

print("Dolar ", dolar)
print("Euro ", euro)
dolar = int(dolar)
while True:

    dolarmod = float(input(": "))

    #  print(float(dolar)/dolarmod) # de dolar para AOA
    #  print(dolarmod/dolar)  # de AOA para dolar


# print("BitCons", bicons)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
