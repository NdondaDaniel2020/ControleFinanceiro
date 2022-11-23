import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json

class RaspangemDadosMoeda():
    def __init__(self):
        self.url = {
            'USD': 'https://www.google.com/search?q=conversor+de+moeda+dolar+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=pDZDY9_WCqmJ9u8PipO24Aw&oq=conversor+de+moeda+do&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQgAQQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCAAQRxDWBBCwAzoHCAAQsAMQQ0oECEEYAEoECEYYAFDjC1ilEmCvLWgBcAF4AIABjwKIAaEGkgEDMi0zmAEAoAEByAEKwAEB&sclient=gws-wiz',
            'EUR': 'https://www.google.com/search?q=conversor+de+moeda+euro+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=_F1DY6zdOcKYhbIPsfSX0AQ&ved=0ahUKEwisy5OHq9T6AhVCTEEAHTH6BUoQ4dUDCA4&uact=5&oq=conversor+de+moeda+euro+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggI6CggAEEcQ1gQQsAM6BggAEB4QBzoFCAAQgAQ6DAgAEIAEEA0QRhCCAkoECEEYAEoECEYYAFDCB1ivI2DRK2gBcAF4AIAB3wOIAaIgkgEFMy05LjKYAQCgAQHIAQjAAQE&sclient=gws-wiz',
            'KWD': 'https://www.google.com/search?q=conversor+de+moeda+dinar+kuwait+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=9mBDY__KArSAi-gP4ZWx-Ao&ved=0ahUKEwj_nYnyrdT6AhU0wAIHHeFKDK8Q4dUDCA4&uact=5&oq=conversor+de+moeda+dinar+kuwait+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQ6CggAEEcQ1gQQsAM6BwgAELADEEM6EgguEMcBENEDEMgDELADEEMYAToGCAAQHhAHOgUIABCABDoICCEQwwQQoAE6CgghEMMEEAoQoAFKBAhBGABKBAhGGABQmwpY4mJgoGpoAXABeACAAYcEiAGULZIBCDMtMTQuMS4xmAEAoAEByAELwAEB2gEECAEYCA&sclient=gws-wiz',
            'BHD': 'https://www.google.com/search?q=conversor+de+moeda+dinar+bahrei+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=GGJDY_CzE4W5sAftg4ygDA&ved=0ahUKEwjwn778rtT6AhWFHOwKHe0BA8QQ4dUDCA4&uact=5&oq=conversor+de+moeda+dinar+bahrei+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBAghEAo6BQgAEKIEOgcIABAeEKIESgQIQRgBSgQIRhgAUJAGWIebAmCRqQJoBHAAeACAAegCiAGEH5IBBDMtMTKYAQCgAQHAAQE&sclient=gws-wiz',
            'OMR': 'https://www.google.com/search?q=conversor+de+moeda+Rial+de+Om%C3%A3+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=JGdDY63cC5f_kwW044f4Aw&ved=0ahUKEwit_r_ks9T6AhWX_6QKHbTxAT8Q4dUDCA4&uact=5&oq=conversor+de+moeda+Rial+de+Om%C3%A3+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogRKBAhBGAFKBAhGGABQjx9Yjx9guiVoAXAAeACAAbQCiAG0ApIBAzMtMZgBAKABAqABAcABAQ&sclient=gws-wiz',
            'JOB': 'https://www.google.com/search?q=conversor+de+moeda+Dinar+da+Jord%C3%A2nia+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=nGhDY-EujPSTBfK2q-AM&ved=0ahUKEwjh7NmXtdT6AhUM-qQKHXLbCswQ4dUDCA4&uact=5&oq=conversor+de+moeda+Dinar+da+Jord%C3%A2nia+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQ6CAgAEKIEELADSgQIQRgBSgQIRhgAUOEkWOEkYKg6aAFwAHgAgAHHAogBxwKSAQMzLTGYAQCgAQKgAQHIAQPAAQE&sclient=gws-wiz',
            'KYD': 'https://www.google.com/search?q=conversor+de+moeda+D%C3%B3lar+Cayman+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=4mhDY4CKNojmsAf_4Ly4BA&ved=0ahUKEwiAg8C5tdT6AhUIM-wKHX8wD0cQ4dUDCA4&uact=5&oq=conversor+de+moeda+D%C3%B3lar+Cayman+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogRKBAhBGAFKBAhGGABQwR9YwR9g-yhoAXAAeACAAd0CiAHdApIBAzMtMZgBAKABAqABAcABAQ&sclient=gws-wiz',
            'GBP': 'https://www.google.com/search?q=conversor+de+Libra+Esterlina+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=BABKY4OwLenjkgWy0p5Q&ved=0ahUKEwiDwqG2_uD6AhXpsaQKHTKpBwoQ4dUDCA4&uact=5&oq=conversor+de+Libra+Esterlina+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABOgoIABBHENYEELADOg0IABDkAhDWBBCwAxgBOgUIABCiBEoECE0YAUoECEEYAEoECEYYAVDUDVirFmDoP2gBcAF4AIABgAOIAesSkgEDMy03mAEAoAEByAENwAEB2gEGCAEQARgJ&sclient=gws-wiz',
            'CFH': 'https://www.google.com/search?q=conversor+de+moeda+Franco+Su%C3%AD%C3%A7o+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=G2pDY8pwgpKwB_eFsdgB&ved=0ahUKEwiK6qrOttT6AhUCCewKHfdCDBsQ4dUDCA4&uact=5&oq=conversor+de+moeda+Franco+Su%C3%AD%C3%A7o+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQ6CggAEEcQ1gQQsANKBAhBGABKBAhGGABQix5Yix5gtyNoAXABeACAAe8CiAHvApIBAzMtMZgBAKABAqABAcgBCMABAQ&sclient=gws-wiz',
            'BTC': 'https://www.google.com/search?q=conversor+de+moeda+bitcoin+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=XWpDY5q4KYT7sAejk6WwCw&oq=conversor+de+moeda+Bit+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQHhAHOgoIABBHENYEELADOggIABAeEAgQB0oECEEYAEoECEYYAFCPXVjtbmDdiQFoAnABeACAAeACiAGCCpIBAzMtNJgBAKABAcgBCMABAQ&sclient=gws-wiz'}  ## tem as URLS onde de sites onde pega as moedas
        self.xpathMoedas = ['//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]',
                            '//*[@id="crypto-updatable_2"]/div[3]/div[2]/span[1]']  ## tem os Xpath dos locais Moedas
        self.xpathGrafic = ['/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[2]/div[2]/div[2]/div/div',
                            '/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[2]/div[2]/div[2]/div/div',
                            '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[3]/div[4]/div[2]/div/div']  ## tem os Xpath dos locais Grafic
        self.unidade = ['USD', 'EUR', 'KWD', 'BHD', 'OMR', 'JOB', 'KYD', 'GBP', 'CFH', 'BTC']  ## as moedas usadas

        self.moedas = {}
        self.grafico = {}
        self.pegarHTML = {}

        option = Options()
        option.headless = True

        self.driver = webdriver.Chrome(options=option)

    def pegarPados(self):
        for uni in self.unidade:
            self.driver.get(self.url[uni])

            try:
                elementM = self.driver.find_element(By.XPATH, self.xpathMoedas[0])
            except:
                elementM = self.driver.find_element(By.XPATH, self.xpathMoedas[1])

            try:
                try:
                    elementG = self.driver.find_element(By.XPATH, self.xpathGrafic[0])
                except:
                    try:
                        elementG = self.driver.find_element(By.XPATH, self.xpathGrafic[1])
                    except:
                        elementG = self.driver.find_element(By.XPATH, self.xpathGrafic[2])
            except:
                pass
            valorMoedas = elementM.text.replace('Kwanza angolano', '')
            self.moedas[uni] = valorMoedas

            self.pegarHTML[uni] = elementG.get_attribute('outerHTML')
        self.driver.quit()
        self.tratarHTML()


    def tratarHTML(self):
        for uni in self.unidade:
            guardarHTML = ''
            filtroHTML = ''
            # repartir o HTML e pegar a tag dos dados
            for html in self.pegarHTML[uni]:
                guardarHTML += html
                if '<path d="M ' in guardarHTML:
                    filtroHTML = guardarHTML
                if html == '>':
                    guardarHTML = ''

            gur_dado = ''
            dadosFiltrados = []
            # repartir a tag com dados  para uma lista com dadso insolados
            for dado in filtroHTML:
                gur_dado += dado
                if dado == 'L':
                    dadosFiltrados.append(gur_dado)
                    gur_dado = ''
            dadosFiltrados.append(gur_dado)

            # eliminar o nao e dados
            dadosFiltrados.insert(0, dadosFiltrados[0][11:])
            dadosFiltrados.insert(-1, dadosFiltrados[-1][:13])
            dadosFiltrados.pop(1)
            dadosFiltrados.pop(-1)

            ultimoFiltro = []
            # eliminar o que nao e dado
            for dado in dadosFiltrados:
                ultimoFiltro.append(dado[1:-2])

            tratamentoList = []
            for d in ultimoFiltro:
                valor = list(d)
                tratamentoList.append(valor)

            valorX = ''
            valorY = ''
            fvalorX = 0.0
            fvalorY = 0.0
            mudaXY = False
            dadosGrafico = []
            for listDados in tratamentoList:
                for dado in listDados:
                    if dado == ' ':
                        mudaXY = True
                    else:
                        if mudaXY == False:
                            valorX += dado
                        if mudaXY == True:
                            valorY += dado
                try:
                    fvalorX = float(valorX)
                    fvalorY = float(valorY)
                except:
                    pass
                dadosGrafico.append((fvalorX, fvalorY))
                valorX = ''
                valorY = ''
                mudaXY = False

            self.grafico[uni] = dadosGrafico


    def pegarDolarUSD(self):
        return self.moedas['USD']

    def pegarEuroEUR(self):
        return self.moedas['EUR']

    def pegarDinarKuwaitKWD(self):
        return self.moedas['KWD']

    def pegarDinarBahreiBHD(self):
        return self.moedas['BHD']

    def pegarOmaniRialOMR(self):
        return self.moedas['OMR']

    def pegarDinarJordaniaJOB(self):
        return self.moeads['JOB']

    def pegaKaymanIslandDollarKYD(self):
        return self.moedas['KYD']

    def pegarLibraEsterLinaBritanicaGBP(self):
        return self.moedas['GBP']

    def pegarFrancoSuicoCFH(self):
        return self.moedas['CFH']

    def pegarBitCoinsBTC(self):
        return self.moedas['BTC']


    def pegarGraficDolarUSD(self):
        return self.grafico['USD']

    def pegarGraficEuroEUR(self):
        return self.grafico['EUR']

    def pegarGraficDinarKuwaitKWD(self):
        return self.grafico['KWD']

    def pegarGraficDinarBahreiBHD(self):
        return self.grafico['BHD']

    def pegarGraficOmaniRialOMR(self):
        return self.grafico['OMR']

    def pegarGraficDinarJordaniaJOB(self):
        return self.grafico['JOB']

    def pegarGraficKaymanIslandDollarKYD(self):
        return self.grafico['KYD']

    def pegarGraficLibraEsterLinaBritanicaGBP(self):
        return self.grafico['GBP']

    def pegarGraficFrancoSuicoCFH(self):
        return self.grafico['CFH']

    def pegarGraficBitCoinsBTC(self):
        return self.grafico['BTC']


def tirarLixo(htmlist):
    inf = ''
    for c in str(htmlist):

        if not c == " ":
            inf += c
        else:
            if 'value' in inf:
                inf = inf[7:-1]
                filtrar = inf
            inf = ""
    return filtrar

def scraping():
    url = {
        'USD': 'https://www.google.com/search?q=conversor+de+moeda+dolar+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=pDZDY9_WCqmJ9u8PipO24Aw&oq=conversor+de+moeda+do&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQgAQQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCAAQRxDWBBCwAzoHCAAQsAMQQ0oECEEYAEoECEYYAFDjC1ilEmCvLWgBcAF4AIABjwKIAaEGkgEDMi0zmAEAoAEByAEKwAEB&sclient=gws-wiz',
        'EUR': 'https://www.google.com/search?q=conversor+de+moeda+euro+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=_F1DY6zdOcKYhbIPsfSX0AQ&ved=0ahUKEwisy5OHq9T6AhVCTEEAHTH6BUoQ4dUDCA4&uact=5&oq=conversor+de+moeda+euro+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggI6CggAEEcQ1gQQsAM6BggAEB4QBzoFCAAQgAQ6DAgAEIAEEA0QRhCCAkoECEEYAEoECEYYAFDCB1ivI2DRK2gBcAF4AIAB3wOIAaIgkgEFMy05LjKYAQCgAQHIAQjAAQE&sclient=gws-wiz',
        'KWD': 'https://www.google.com/search?q=conversor+de+moeda+dinar+kuwait+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=9mBDY__KArSAi-gP4ZWx-Ao&ved=0ahUKEwj_nYnyrdT6AhU0wAIHHeFKDK8Q4dUDCA4&uact=5&oq=conversor+de+moeda+dinar+kuwait+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQ6CggAEEcQ1gQQsAM6BwgAELADEEM6EgguEMcBENEDEMgDELADEEMYAToGCAAQHhAHOgUIABCABDoICCEQwwQQoAE6CgghEMMEEAoQoAFKBAhBGABKBAhGGABQmwpY4mJgoGpoAXABeACAAYcEiAGULZIBCDMtMTQuMS4xmAEAoAEByAELwAEB2gEECAEYCA&sclient=gws-wiz',
        'BHD': 'https://www.google.com/search?q=conversor+de+moeda+dinar+bahrei+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=GGJDY_CzE4W5sAftg4ygDA&ved=0ahUKEwjwn778rtT6AhWFHOwKHe0BA8QQ4dUDCA4&uact=5&oq=conversor+de+moeda+dinar+bahrei+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBAghEAo6BQgAEKIEOgcIABAeEKIESgQIQRgBSgQIRhgAUJAGWIebAmCRqQJoBHAAeACAAegCiAGEH5IBBDMtMTKYAQCgAQHAAQE&sclient=gws-wiz',
        'OMR': 'https://www.google.com/search?q=conversor+de+moeda+Rial+de+Om%C3%A3+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=JGdDY63cC5f_kwW044f4Aw&ved=0ahUKEwit_r_ks9T6AhWX_6QKHbTxAT8Q4dUDCA4&uact=5&oq=conversor+de+moeda+Rial+de+Om%C3%A3+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogRKBAhBGAFKBAhGGABQjx9Yjx9guiVoAXAAeACAAbQCiAG0ApIBAzMtMZgBAKABAqABAcABAQ&sclient=gws-wiz',
        'JOB': 'https://www.google.com/search?q=conversor+de+moeda+Dinar+da+Jord%C3%A2nia+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=nGhDY-EujPSTBfK2q-AM&ved=0ahUKEwjh7NmXtdT6AhUM-qQKHXLbCswQ4dUDCA4&uact=5&oq=conversor+de+moeda+Dinar+da+Jord%C3%A2nia+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQ6CAgAEKIEELADSgQIQRgBSgQIRhgAUOEkWOEkYKg6aAFwAHgAgAHHAogBxwKSAQMzLTGYAQCgAQKgAQHIAQPAAQE&sclient=gws-wiz',
        'KYD': 'https://www.google.com/search?q=conversor+de+moeda+D%C3%B3lar+Cayman+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=4mhDY4CKNojmsAf_4Ly4BA&ved=0ahUKEwiAg8C5tdT6AhUIM-wKHX8wD0cQ4dUDCA4&uact=5&oq=conversor+de+moeda+D%C3%B3lar+Cayman+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogRKBAhBGAFKBAhGGABQwR9YwR9g-yhoAXAAeACAAd0CiAHdApIBAzMtMZgBAKABAqABAcABAQ&sclient=gws-wiz',
        'GBP': 'https://www.google.com/search?q=conversor+de+Libra+Esterlina+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=BABKY4OwLenjkgWy0p5Q&ved=0ahUKEwiDwqG2_uD6AhXpsaQKHTKpBwoQ4dUDCA4&uact=5&oq=conversor+de+Libra+Esterlina+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABOgoIABBHENYEELADOg0IABDkAhDWBBCwAxgBOgUIABCiBEoECE0YAUoECEEYAEoECEYYAVDUDVirFmDoP2gBcAF4AIABgAOIAesSkgEDMy03mAEAoAEByAENwAEB2gEGCAEQARgJ&sclient=gws-wiz',
        'CFH': 'https://www.google.com/search?q=conversor+de+moeda+Franco+Su%C3%AD%C3%A7o+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=G2pDY8pwgpKwB_eFsdgB&ved=0ahUKEwiK6qrOttT6AhUCCewKHfdCDBsQ4dUDCA4&uact=5&oq=conversor+de+moeda+Franco+Su%C3%AD%C3%A7o+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQ6CggAEEcQ1gQQsANKBAhBGABKBAhGGABQix5Yix5gtyNoAXABeACAAe8CiAHvApIBAzMtMZgBAKABAqABAcgBCMABAQ&sclient=gws-wiz',
        'BTC': 'https://www.google.com/search?q=conversor+de+moeda+bitcoin+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=XWpDY5q4KYT7sAejk6WwCw&oq=conversor+de+moeda+Bit+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQHhAHOgoIABBHENYEELADOggIABAeEAgQB0oECEEYAEoECEYYAFCPXVjtbmDdiQFoAnABeACAAeACiAGCCpIBAzMtNJgBAKABAcgBCMABAQ&sclient=gws-wiz'}
    xpath = ['//*[@id="knowledge-currency__updatable-data-column"]/div[3]/div/div[2]/input',
             '//*[@id="crypto-updatable_2"]/div[3]/div[5]/div[2]/input']
    htmlist = {}

    options = Options()
    options.headless = True
    # a por a opção de não aparecer
    driver = webdriver.Chrome(options=options)

    unidade = ['USD', 'EUR', 'KWD', 'BHD', 'OMR', 'JOB', 'KYD', 'GBP', 'CFH', 'BTC']

    for uni in unidade:
        driver.get(url[uni])
        try:
            element = driver.find_element(By.XPATH, xpath[0])
        except:
            element = driver.find_element(By.XPATH, xpath[1])
        valor = tirarLixo(element.get_attribute('outerHTML'))
        htmlist[uni] = valor

    print(htmlist)

def grafico():
    url = {
        'USD': 'https://www.google.com/search?q=conversor+de+moeda+dolar+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=pDZDY9_WCqmJ9u8PipO24Aw&oq=conversor+de+moeda+do&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQgAQQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCAAQRxDWBBCwAzoHCAAQsAMQQ0oECEEYAEoECEYYAFDjC1ilEmCvLWgBcAF4AIABjwKIAaEGkgEDMi0zmAEAoAEByAEKwAEB&sclient=gws-wiz',
        'EUR': 'https://www.google.com/search?q=conversor+de+moeda+euro+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=_F1DY6zdOcKYhbIPsfSX0AQ&ved=0ahUKEwisy5OHq9T6AhVCTEEAHTH6BUoQ4dUDCA4&uact=5&oq=conversor+de+moeda+euro+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggI6CggAEEcQ1gQQsAM6BggAEB4QBzoFCAAQgAQ6DAgAEIAEEA0QRhCCAkoECEEYAEoECEYYAFDCB1ivI2DRK2gBcAF4AIAB3wOIAaIgkgEFMy05LjKYAQCgAQHIAQjAAQE&sclient=gws-wiz',
        'KWD': 'https://www.google.com/search?q=conversor+de+moeda+dinar+kuwait+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=9mBDY__KArSAi-gP4ZWx-Ao&ved=0ahUKEwj_nYnyrdT6AhU0wAIHHeFKDK8Q4dUDCA4&uact=5&oq=conversor+de+moeda+dinar+kuwait+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQ6CggAEEcQ1gQQsAM6BwgAELADEEM6EgguEMcBENEDEMgDELADEEMYAToGCAAQHhAHOgUIABCABDoICCEQwwQQoAE6CgghEMMEEAoQoAFKBAhBGABKBAhGGABQmwpY4mJgoGpoAXABeACAAYcEiAGULZIBCDMtMTQuMS4xmAEAoAEByAELwAEB2gEECAEYCA&sclient=gws-wiz',
        'BHD': 'https://www.google.com/search?q=conversor+de+moeda+dinar+bahrei+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=GGJDY_CzE4W5sAftg4ygDA&ved=0ahUKEwjwn778rtT6AhWFHOwKHe0BA8QQ4dUDCA4&uact=5&oq=conversor+de+moeda+dinar+bahrei+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBAghEAo6BQgAEKIEOgcIABAeEKIESgQIQRgBSgQIRhgAUJAGWIebAmCRqQJoBHAAeACAAegCiAGEH5IBBDMtMTKYAQCgAQHAAQE&sclient=gws-wiz',
        'OMR': 'https://www.google.com/search?q=conversor+de+moeda+Rial+de+Om%C3%A3+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=JGdDY63cC5f_kwW044f4Aw&ved=0ahUKEwit_r_ks9T6AhWX_6QKHbTxAT8Q4dUDCA4&uact=5&oq=conversor+de+moeda+Rial+de+Om%C3%A3+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogRKBAhBGAFKBAhGGABQjx9Yjx9guiVoAXAAeACAAbQCiAG0ApIBAzMtMZgBAKABAqABAcABAQ&sclient=gws-wiz',
        'JOB': 'https://www.google.com/search?q=conversor+de+moeda+Dinar+da+Jord%C3%A2nia+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=nGhDY-EujPSTBfK2q-AM&ved=0ahUKEwjh7NmXtdT6AhUM-qQKHXLbCswQ4dUDCA4&uact=5&oq=conversor+de+moeda+Dinar+da+Jord%C3%A2nia+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQ6CAgAEKIEELADSgQIQRgBSgQIRhgAUOEkWOEkYKg6aAFwAHgAgAHHAogBxwKSAQMzLTGYAQCgAQKgAQHIAQPAAQE&sclient=gws-wiz',
        'KYD': 'https://www.google.com/search?q=conversor+de+moeda+D%C3%B3lar+Cayman+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=4mhDY4CKNojmsAf_4Ly4BA&ved=0ahUKEwiAg8C5tdT6AhUIM-wKHX8wD0cQ4dUDCA4&uact=5&oq=conversor+de+moeda+D%C3%B3lar+Cayman+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogRKBAhBGAFKBAhGGABQwR9YwR9g-yhoAXAAeACAAd0CiAHdApIBAzMtMZgBAKABAqABAcABAQ&sclient=gws-wiz',
        'GBP': 'https://www.google.com/search?q=conversor+de+Libra+Esterlina+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=BABKY4OwLenjkgWy0p5Q&ved=0ahUKEwiDwqG2_uD6AhXpsaQKHTKpBwoQ4dUDCA4&uact=5&oq=conversor+de+Libra+Esterlina+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABOgoIABBHENYEELADOg0IABDkAhDWBBCwAxgBOgUIABCiBEoECE0YAUoECEEYAEoECEYYAVDUDVirFmDoP2gBcAF4AIABgAOIAesSkgEDMy03mAEAoAEByAENwAEB2gEGCAEQARgJ&sclient=gws-wiz',
        'CFH': 'https://www.google.com/search?q=conversor+de+moeda+Franco+Su%C3%AD%C3%A7o+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=G2pDY8pwgpKwB_eFsdgB&ved=0ahUKEwiK6qrOttT6AhUCCewKHfdCDBsQ4dUDCA4&uact=5&oq=conversor+de+moeda+Franco+Su%C3%AD%C3%A7o+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQ6CggAEEcQ1gQQsANKBAhBGABKBAhGGABQix5Yix5gtyNoAXABeACAAe8CiAHvApIBAzMtMZgBAKABAqABAcgBCMABAQ&sclient=gws-wiz',
        'BTC': 'https://www.google.com/search?q=conversor+de+moeda+bitcoin+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=XWpDY5q4KYT7sAejk6WwCw&oq=conversor+de+moeda+Bit+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQHhAHOgoIABBHENYEELADOggIABAeEAgQB0oECEEYAEoECEYYAFCPXVjtbmDdiQFoAnABeACAAeACiAGCCpIBAzMtNJgBAKABAcgBCMABAQ&sclient=gws-wiz'}
    # no primeiro linnk temos DIA/MÊS e no ourto temos os dados da TABELA
    xpath = ['/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[2]/div[2]/div[2]/div/div',
             '/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[2]/div[2]/div[2]/div/div',
             '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[3]/div[4]/div[2]/div/div']
    unidade = ['USD', 'EUR', 'KWD', 'BHD', 'OMR', 'JOB', 'KYD', 'GBP', 'CFH', 'BTC']
    dadosDeGrafico = {}

    options = Options()
    options.headless = True
    # a por a opção de não aparecer
    driver = webdriver.Chrome(options=options)

    for n, uni in enumerate(unidade):

        driver.get(url[uni])
        try:
            element = driver.find_element(By.XPATH, xpath[0])
        except:
            try:
                element = driver.find_element(By.XPATH, xpath[1])
            except:
                element = driver.find_element(By.XPATH, xpath[2])

        grafic = element.get_attribute('outerHTML')

        gur = ''
        dado_grafico = ''
        # repartir o HTML e pegar a tag dos dados
        for gr in grafic:
            gur += gr
            if '<path d="M ' in gur:
                dado_grafico = gur
            if gr == '>':
                gur = ''

        gur_dado = ''
        lista_dado = []
        # repartir a tag com dados  para uma lista com dadso insolados
        for dado in dado_grafico:
            gur_dado += dado
            if dado == 'L':
                lista_dado.append(gur_dado)
                gur_dado = ''
        lista_dado.append(gur_dado)

        # eliminar o nao e dados
        lista_dado.insert(0, lista_dado[0][11:])
        lista_dado.insert(-1, lista_dado[-1][:13])
        lista_dado.pop(1)
        lista_dado.pop(-1)

        listDfinDado = []
        # eliminar o que nao e dado
        for dado in lista_dado:
            listDfinDado.append(dado[1:-2])

        dadosDeGrafico[uni] = listDfinDado
        print(n, listDfinDado, len(listDfinDado))

    driver.quit()
    print(dadosDeGrafico)

def scraping2():
    url = {
        'USD': 'https://www.google.com/search?q=conversor+de+moeda+dolar+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=pDZDY9_WCqmJ9u8PipO24Aw&oq=conversor+de+moeda+do&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQgAQQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCAAQRxDWBBCwAzoHCAAQsAMQQ0oECEEYAEoECEYYAFDjC1ilEmCvLWgBcAF4AIABjwKIAaEGkgEDMi0zmAEAoAEByAEKwAEB&sclient=gws-wiz',
        'EUR': 'https://www.google.com/search?q=conversor+de+moeda+euro+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=_F1DY6zdOcKYhbIPsfSX0AQ&ved=0ahUKEwisy5OHq9T6AhVCTEEAHTH6BUoQ4dUDCA4&uact=5&oq=conversor+de+moeda+euro+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggI6CggAEEcQ1gQQsAM6BggAEB4QBzoFCAAQgAQ6DAgAEIAEEA0QRhCCAkoECEEYAEoECEYYAFDCB1ivI2DRK2gBcAF4AIAB3wOIAaIgkgEFMy05LjKYAQCgAQHIAQjAAQE&sclient=gws-wiz',
        'KWD': 'https://www.google.com/search?q=conversor+de+moeda+dinar+kuwait+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=9mBDY__KArSAi-gP4ZWx-Ao&ved=0ahUKEwj_nYnyrdT6AhU0wAIHHeFKDK8Q4dUDCA4&uact=5&oq=conversor+de+moeda+dinar+kuwait+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQ6CggAEEcQ1gQQsAM6BwgAELADEEM6EgguEMcBENEDEMgDELADEEMYAToGCAAQHhAHOgUIABCABDoICCEQwwQQoAE6CgghEMMEEAoQoAFKBAhBGABKBAhGGABQmwpY4mJgoGpoAXABeACAAYcEiAGULZIBCDMtMTQuMS4xmAEAoAEByAELwAEB2gEECAEYCA&sclient=gws-wiz',
        'BHD': 'https://www.google.com/search?q=conversor+de+moeda+dinar+bahrei+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=GGJDY_CzE4W5sAftg4ygDA&ved=0ahUKEwjwn778rtT6AhWFHOwKHe0BA8QQ4dUDCA4&uact=5&oq=conversor+de+moeda+dinar+bahrei+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBAghEAo6BQgAEKIEOgcIABAeEKIESgQIQRgBSgQIRhgAUJAGWIebAmCRqQJoBHAAeACAAegCiAGEH5IBBDMtMTKYAQCgAQHAAQE&sclient=gws-wiz',
        'OMR': 'https://www.google.com/search?q=conversor+de+moeda+Rial+de+Om%C3%A3+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=JGdDY63cC5f_kwW044f4Aw&ved=0ahUKEwit_r_ks9T6AhWX_6QKHbTxAT8Q4dUDCA4&uact=5&oq=conversor+de+moeda+Rial+de+Om%C3%A3+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogRKBAhBGAFKBAhGGABQjx9Yjx9guiVoAXAAeACAAbQCiAG0ApIBAzMtMZgBAKABAqABAcABAQ&sclient=gws-wiz',
        'JOB': 'https://www.google.com/search?q=conversor+de+moeda+Dinar+da+Jord%C3%A2nia+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=nGhDY-EujPSTBfK2q-AM&ved=0ahUKEwjh7NmXtdT6AhUM-qQKHXLbCswQ4dUDCA4&uact=5&oq=conversor+de+moeda+Dinar+da+Jord%C3%A2nia+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQ6CAgAEKIEELADSgQIQRgBSgQIRhgAUOEkWOEkYKg6aAFwAHgAgAHHAogBxwKSAQMzLTGYAQCgAQKgAQHIAQPAAQE&sclient=gws-wiz',
        'KYD': 'https://www.google.com/search?q=conversor+de+moeda+D%C3%B3lar+Cayman+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=4mhDY4CKNojmsAf_4Ly4BA&ved=0ahUKEwiAg8C5tdT6AhUIM-wKHX8wD0cQ4dUDCA4&uact=5&oq=conversor+de+moeda+D%C3%B3lar+Cayman+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogRKBAhBGAFKBAhGGABQwR9YwR9g-yhoAXAAeACAAd0CiAHdApIBAzMtMZgBAKABAqABAcABAQ&sclient=gws-wiz',
        'GBP': 'https://www.google.com/search?q=conversor+de+Libra+Esterlina+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=BABKY4OwLenjkgWy0p5Q&ved=0ahUKEwiDwqG2_uD6AhXpsaQKHTKpBwoQ4dUDCA4&uact=5&oq=conversor+de+Libra+Esterlina+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQghEKABOgoIABBHENYEELADOg0IABDkAhDWBBCwAxgBOgUIABCiBEoECE0YAUoECEEYAEoECEYYAVDUDVirFmDoP2gBcAF4AIABgAOIAesSkgEDMy03mAEAoAEByAENwAEB2gEGCAEQARgJ&sclient=gws-wiz',
        'CFH': 'https://www.google.com/search?q=conversor+de+moeda+Franco+Su%C3%AD%C3%A7o+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=G2pDY8pwgpKwB_eFsdgB&ved=0ahUKEwiK6qrOttT6AhUCCewKHfdCDBsQ4dUDCA4&uact=5&oq=conversor+de+moeda+Franco+Su%C3%AD%C3%A7o+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEKIEMgUIABCiBDIFCAAQogQ6CggAEEcQ1gQQsANKBAhBGABKBAhGGABQix5Yix5gtyNoAXABeACAAe8CiAHvApIBAzMtMZgBAKABAqABAcgBCMABAQ&sclient=gws-wiz',
        'BTC': 'https://www.google.com/search?q=conversor+de+moeda+bitcoin+para+kwanza&rlz=1C1CHWL_pt-PTAO1018AO1018&ei=XWpDY5q4KYT7sAejk6WwCw&oq=conversor+de+moeda+Bit+para+kwanza&gs_lcp=Cgdnd3Mtd2l6EAEYADIGCAAQHhAHOgoIABBHENYEELADOggIABAeEAgQB0oECEEYAEoECEYYAFCPXVjtbmDdiQFoAnABeACAAeACiAGCCpIBAzMtNJgBAKABAcgBCMABAQ&sclient=gws-wiz'}

    xpath = ['//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]',
             '//*[@id="crypto-updatable_2"]/div[3]/div[2]/span[1]']

    unidade = ['USD', 'EUR', 'KWD', 'BHD', 'OMR', 'JOB', 'KYD', 'GBP', 'CFH', 'BTC']

    option = Options()
    option.headless = True
    moedas = {}
    driver = webdriver.Chrome(options=option)

    for uni in unidade:
        driver.get(url[uni])
        try:
            element = driver.find_element(By.XPATH, xpath[1])
        except:
            element = driver.find_element(By.XPATH, xpath[2])

        valor = element.text.replace('Kwanza angolano', '')
        moedas[uni] = valor

    guardarHTML = ''
    dadosGrafico = ''
    listaDadosGraficos = ''

    # repartir o HTML e pegar a tag dos dados
    for html in pegarHTML[uni]:
        guardarHTML += html
        if '<path d="M ' in guardarHTML:
            dadosGrafico = guardarHTML
        if guardarHTML == '>':
            print(guardarHTML)
            guardarHTML = ''

    # gur_dado = ''
    # lista_dado = []
    # repartir a tag com dados  para uma lista com dadso insolados
    # for dado in dadosGrafico:
    # gur_dado += dado
    # if dado == 'L':
    # lista_dado.append(gur_dado)
    # gur_dado = ''
    # lista_dado.append(gur_dado)

    # eliminar o nao e dados
    # lista_dado.insert(0, lista_dado[0][11:])
    # lista_dado.insert(-1, lista_dado[-1][:13])
    # lista_dado.pop(1)
    # lista_dado.pop(-1)

    # listDfinDado = []
    # eliminar o que nao e dado
    # for dado in lista_dado:
    # listDfinDado.append(dado[1:-2])

    # print(listDfinDado)
    print(moedas)

raspagem = RaspangemDadosMoeda()
raspagem.pegarPados()
dadosGrafico = raspagem.pegarGraficEuroEUR()

print(dadosGrafico)

