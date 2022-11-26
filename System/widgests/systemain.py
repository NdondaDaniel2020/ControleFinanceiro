import json

from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from packeg.custom_grips import CustomGrip
from packeg.circular_progress import CircularProgress
# from System.widgests.ui_SystemMW import Ui_MainWindow
from System.widgests.packeg.database import database
from ui_SystemSC import Ui_SplashCreen
from ui_SystemMW import Ui_MainWindowMW
from System.widgests.packeg.Criptografia import criptografar

from time import sleep
from datetime import date
import sys
import cv2
import pyttsx3
import pyaudio
from vosk import Model, KaldiRecognizer


# variavel global
UsuiarioGlobal = ''
CONT = 0
HAARCASCADES = '../../haarcascades/haarcascade_frontalface_default.xml'
CLASSIFICADORLBPH = '../../classificador/classificadorLBPH.0.1.yml'
NOMEUSER = ''
MNW = 0
PEGARaRQUIVO = False
PEGARaUDIO = 0
# temos dois bugs por enquanto no lin au clicar e ao navegar
PEGARaUDIO = 0

class SplashCreen(QMainWindow):

    def __init__(self):
        # antes de carregar a interface vamos por carregar o algoritimo de reconhecimento
        try:
            self.ClassificadorDeVideo = cv2.CascadeClassifier(HAARCASCADES)  # metodo reponsavel para focar no rosto
            self.Fonte = cv2.FONT_HERSHEY_COMPLEX_SMALL  # definir fonty do reconhecimento
            self.Reconhecedor = cv2.face.LBPHFaceRecognizer_create()  # metodo reponsavelo por conpara as imagens do reconhecidor com a que e pega na camera
            self.Reconhecedor.read(CLASSIFICADORLBPH)  # pegar a base de dados de imagns
            self.Redimencionar = True # ele vai dizer se no reconhecimento qunado o resultado sair se vai
            # redimencionar a tela ou não
        except:
            quit()
            pass

        sleep(2)  #paramos 1 segundo para nao atrapalhar na performace da Ui
        # inicio da interfaceGrafica
        QMainWindow.__init__(self)
        self.sc = Ui_SplashCreen()
        self.sc.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)  # este comando é responsavel por eliminar a barra de titulo
        self.setAttribute(Qt.WA_TranslucentBackground)  # este comando é responsavel por tornar o fundo transparente

        # chamando a class que controla a base de dados

        self.database = database("ControloFinaceiro.db")
        self.senhaUltimoUser = ''
        self.nomeDoUsuario = ''    ## ele será Usado para o main window
        self.VerificarUltimoUser()

        # lista ficticia de usuario e suas senhas
        # criados para um teste sera substituido por um database
        self.listaUsuarios = list()
        self.listaSenha = list()
        self.listaAcesso = list()
        self.ListaUsuarioInBD()

        # Nesta zona do cod  mudei o local ou a transparencia dos objetos para fazer ele aparecerem com animação
        self.sc.Nome.setGeometry(20, 230, 170, 20)
        self.sc.TrocaDeUsuario.setStyleSheet("""
                            QPushButton{
                            color:rgba(255, 255, 255, 0);
                            background-color: rgba(170, 0, 255, 0);
                            border-radius:5px;
                            }
                            QPushButton:hover{
                            color:#ffffff;
                            background-color: rgb(149, 0, 223);
                            border-radius:5px;
                            }
                            QPushButton:pressed{
                            color:#ffffff;
                            background-color: rgb(170, 0, 255);
                            border-radius:5px;
                            }
                            QToolTip{
                            background-color: rgb(170, 85, 255);
                            border-radius:3px;
                            border:3px solid rgb(255, 255, 255);
                            }
                            """)
        self.sc.senhaIncorreta.close()
        self.sc.camera.close()
        self.sc.criadoPor.close()
        self.sc.data.close()
        self.sc.fechar_1.close()
        self.sc.versao.close()
        self.sc.login.setStyleSheet("border-radius: 15px; ")
        self.sc.senhaIncorreta.close()

        # zona opacity close
        self.logoPrincipal_opacityt = QGraphicsOpacityEffect(self.sc.logoPrincipal)
        self.logoPrincipal_opacityt.setOpacity(0)
        self.sc.logoPrincipal.setGraphicsEffect(self.logoPrincipal_opacityt)

        self.logoA_opacity = QGraphicsOpacityEffect(self.sc.logo)
        self.sc.logo.setGraphicsEffect(self.logoA_opacity)

        self.sc.Nome.setGeometry(10, 250, 170, 20)
        self.sc.senhaIncorreta.close()
        self.sc.senhaIncorreta_2.close()
        self.sc.senhaIncorreta_3.close()
        self.atraso = False

        # variaveis de obj
        self.senha_login_name = 0
        self.passwor2Cont = 0
        self.passwor1Cont = 0
        # para mover a SplashScreen
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.sc.page_central.mouseMoveEvent = moveWindow
        self.sc.page_login.mouseMoveEvent = moveWindow
        self.sc.page_webCam.mouseMoveEvent = moveWindow
        # este é um objeto  criado com cod cricle progress bar
        self.progress = CircularProgress()
        self.progress.width = 228
        self.progress.height = 228
        self.progress.value = 0
        self.progress.setFixedSize(self.progress.width, self.progress.height)
        self.progress.move(110, 4)
        self.progress.font_size = 12
        self.progress.progress_width = 2
        self.progress.ad_shadow(True)
        self.progress.setParent(self.sc.centro)
        self.progress.progress_color = 0xFFFFFF
        self.progress.text_color = 0xFFFFFF
        self.progress.show()

        # removendo falha na igm
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.sc.CentralFrame.setGraphicsEffect(self.shadow)

        # zona da conecção dos botões com as suas funções
        self.sc.fechar_1.clicked.connect(self.close)
        self.sc.fechar_2.clicked.connect(self.close)
        self.sc.fechar_3.clicked.connect(self.close)

        self.sc.troca.clicked.connect(self.senha_animatio_complet)
        self.sc.senha.returnPressed.connect(self.confirma_senha)
        self.sc.TrocaDeUsuario.clicked.connect(self.troca_usuario)
        self.sc.camera.clicked.connect(self.troca_usuario)

        self.sc.password.returnPressed.connect(self.confirma_senha_name)
        self.sc.login_btn.clicked.connect(self.confirma_senha_name)

        self.sc.sengup.clicked.connect(self.animationSingUp)
        self.sc.login_btn_singup.clicked.connect(self.animationSingUp)

        self.sc.password2.returnPressed.connect(self.singup)
        self.sc.singup_singup.clicked.connect(self.singup)

        # zona do timer
        self.progressCircleTimer = QTimer()
        self.progressCircleTimer.timeout.connect(self.circulaProgreValue)

        self.senha_anaiticTimer = QTimer()
        self.senha_anaiticTimer.timeout.connect(lambda: self.senha_analitic(len(self.sc.senha.text())))

        self.nomeloginTimer = QTimer()
        self.nomeloginTimer.timeout.connect(lambda: self.namelogin(len(self.sc.email_login.text())))

        self.passwordTimer = QTimer()
        self.passwordTimer.timeout.connect(lambda: self.passworveri(len(self.sc.password.text())))

        self.emailsingupTimer = QTimer()
        self.emailsingupTimer.timeout.connect(lambda: self.emailsingup(len(self.sc.email_singup.text())))

        self.password1Timer = QTimer()
        self.password1Timer.timeout.connect(lambda: self.passwor1(len(self.sc.password1.text())))

        self.password2Timer = QTimer()
        self.password2Timer.timeout.connect(lambda: self.passwor2(len(self.sc.password2.text())))

        self.openAnalisingTimer = QTimer()
        self.openAnalisingTimer.timeout.connect(self.openAnalising)

        self.fecharWebcamTimer = QTimer()
        self.fecharWebcamTimer.timeout.connect(self.fecharWebcam)

        self.show()  # mostrar a app

        QTimer.singleShot(10, lambda: self.progressCircleTimer.start())  # inicialisaçãa do Timer com um controlador de
        # tempo
        QTimer.singleShot(6000, lambda: self.AnimatioOpacity())
        QTimer.singleShot(6100, lambda: self.OpenResize())  # funcão com documentação. está com controlador de tempo
        # esta é uma das formas de corrigir o erro de aimagem mudar de posição só
        #QTimer.singleShot(2500, lambda: self.opacityLabel())
        QTimer.singleShot(7500, lambda: self.TestWebCam())

    # responsael pela animação do circupal progres Bar e as outras animation
    def circulaProgreValue(self):
        """
        esta funcão é responsavel pelo aumento do valor do progressbar
        """
        global CONT

        self.progress.set_Value(CONT)

        if CONT >= 100:
            # remover o logo e o progress bar
            self.progress.close()

        if CONT == 95:
            self.sc.criadoPor.setStyleSheet("color: rgba(255, 255, 255, 0)")
            self.sc.data.setStyleSheet("""
                       <html><head/><body><p><span style=" color: rgba(220, 187, 255, 0);">data:  </span><span style=
                       " color:#c297ff;"/><span style=" color: rgba(255, 255, 255, 0);">28/06/2022</span></p></body></html>""")
            self.sc.camera.setStyleSheet(f"""background-color: rgba(170, 0, 255, 0;border-radius:10px;""")
            self.sc.versao.setStyleSheet(f"color: rgba(255, 255, 255, 0)")
            self.sc.fechar_1.setStyleSheet(f""" background-color: rgba(170, 0, 255, 0);border-radius:10px;""")

            self.sc.versao.show()
            self.sc.fechar_1.show()
            self.sc.camera.show()
            self.sc.criadoPor.show()
            self.sc.data.show()

        if CONT >= 95:
            contc = (CONT - 95) * 10
            self.sc.criadoPor.setStyleSheet(f"color: rgba(255, 255, 255, {str(contc)})")
            self.sc.versao.setStyleSheet(f"color: rgba(255, 255, 255, {str(contc)})")
            self.sc.data.setStyleSheet(f"""
                                   <html><head/><body><p><span style=" color: rgba(220, 187, 255, {str(contc)});">
                                   data:  </span><span style=" color:#c297ff;"/><span style=" color: rgba(255, 255, 255,
                                   {str(contc)});">28/06/2022</span></p></body></html>""")
            self.sc.TrocaDeUsuario.setStyleSheet(f"""
                               color:rgba(255, 255, 255, {str(contc)});
                               background-color: rgba(170, 0, 255, {str(contc)});
                               border-radius:5px;""")
            self.sc.camera.setStyleSheet(f"""background-color: rgb(170, 85, 255,{str(contc)});border-radius:10px;""")
            self.sc.fechar_1.setStyleSheet(f"""background-color: rgb(170, 85, 255, {str(contc)});border-radius:10px;""")

        if CONT >= 110:
            conn = (CONT - 90) + 2
            self.sc.Nome.setGeometry(20, 227 - conn, 170, 20)

        if CONT == 120:
            self.progressCircleTimer.stop()
            self.sc.camera.setStyleSheet("""QToolButton:hover{background-color: rgb(150, 76, 228);border-radius:10px;}
            QToolButton:pressed{background-color: rgb(170, 85, 255);border-radius:10px;}""")
            self.sc.fechar_1.setStyleSheet("""QToolButton:hover{background-color: rgb(150, 76, 228);border-radius:10px;}
            QToolButton:pressed{background-color: rgb(170, 85, 255);border-radius:10px;}""")
            self.sc.TrocaDeUsuario.setStyleSheet("""QPushButton{
                                                                color:#ffffff;
                                                                background-color: rgb(150, 76, 228);
                                                                border-radius:5px;
                                                                }
                                                                QPushButton:hover{
                                                                color:#ffffff;
                                                                background-color: rgb(141, 72, 215);
                                                                border-radius:5px;
                                                                }
                                                                QPushButton:pressed{
                                                                color:#ffffff;
                                                                background-color: rgb(150, 76, 228);
                                                                border-radius:5px;
                                                                }
                                                                QToolTip{
                                                                background-color: rgb(170, 85, 255);
                                                                border-radius:3px;
                                                                border:3px solid rgb(255, 255, 255);
                                                                }}""")
            CONT = 0

        CONT += 1

    # responsavel pela aniamção do da opacidade
    def AnimatioOpacity(self):

        self.logoPAnimatio = QPropertyAnimation(self.logoPrincipal_opacityt, b'opacity')
        self.logoPAnimatio.setStartValue(0)
        self.logoPAnimatio.setEndValue(1)
        self.logoPAnimatio.setDuration(300)

        self.logoAAnimation = QPropertyAnimation(self.logoA_opacity, b'opacity')
        self.logoAAnimation.setStartValue(0.7)
        self.logoAAnimation.setEndValue(0)
        self.logoAAnimation.setDuration(300)

        self.group_animation = QParallelAnimationGroup()
        self.group_animation.addAnimation(self.logoAAnimation)
        self.group_animation.addAnimation(self.logoPAnimatio)
        self.group_animation.start()

        # esta é uma das formas de corrigir o erro de aimagem mudar de posição só
        QTimer.singleShot(500, lambda:print())
        self.logoPrincipal_opacityt = QGraphicsOpacityEffect(self.sc.logoPrincipal)
        self.logoPrincipal_opacityt.setOpacity(0.9)
        self.sc.logoPrincipal.setGraphicsEffect(self.logoPrincipal_opacityt)

    # evento responsavel por pegar a posição da tela paramover a janela
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # responsavel pela animação que abri o splash Screen
    def OpenResize(self):
        """
        OpenResize
        este metodo e responsavel pela animacao de abrir a zona de senha
        """
        tamanho_atual = self.sc.CentralFrame.height()
        i = 0
        f = 0
        if tamanho_atual <= 250:
            i = 210
            f = 350
        else:
            i = 350
            f = 210

        self.animation = QPropertyAnimation(self.sc.CentralFrame, b'minimumHeight')
        self.animation.setStartValue(i)
        self.animation.setEndValue(f)
        self.animation.setDuration(1000)
        self.animation.setEasingCurve(QEasingCurve.InOutBack)
        self.animation.start()

    # este metodo resolve o bag do QGraphicsOpacityEffect
    def opacityLabel(self):
        self.shadowLabel = QGraphicsDropShadowEffect(self)
        self.shadowLabel.setBlurRadius(15)
        self.shadowLabel.setXOffset(0)
        self.shadowLabel.setYOffset(0)
        self.shadowLabel.setColor(QColor(0, 0, 0, 0))
        self.sc.logoPrincipal.setGraphicsEffect(self.shadowLabel)

    # animação pela animação que muda a camera e LineEdit
    def senha_animatio_complet(self):
        QTimer.singleShot(200, lambda: self.animation_senha())
        QTimer.singleShot(200, lambda: self.corrigi_bug())
        QTimer.singleShot(2000, lambda: self.closeEndOpenAnalisi())

    # este é reponavel pela aniamçao da opacidade
    def animation_senha(self):

            self.senha_opacity = QGraphicsOpacityEffect(self.sc.senha)
            self.senha_opacity.setOpacity(0.9)
            self.sc.senha.setGraphicsEffect(self.senha_opacity)

            posicao_atual = self.sc.senha.pos().x()

            oi = 0
            of = 0

            if posicao_atual == 210:
                po1 = QPoint(210, 25)
                po2 = QPoint(100, 25)
                oi = 0.9
                of = 0
                lpoi = QPoint(165, 5)
                lpof = QPoint(230, 5)
                self.sc.troca.setText('Usar Password')
                self.sc.senha.setText('')
                self.sc.senha.setStyleSheet("""
                QLineEdit{background-color: rgb(160, 80, 240);
                border:1px solid rgb(230, 187, 255);border-radius:5px;
                color: rgb(208, 208, 208)}
                QLineEdit:hover{background-color: rgb(170, 0, 255);
                border:2px solid rgb(230, 187, 255);border-radius:5px;}
                QLineEdit:focus{background-color: rgb(130, 0, 195);
                border:2px solid rgb(230, 187, 255);border-radius:5px;
                color: rgb(230, 187, 255);}""")
                self.sc.senhaIncorreta.close()
            else:
                self.sc.senha.setStyleSheet("""
                                            QLineEdit{
                                            background-color: rgb(150, 76, 228);
                                            border:1px solid rgb(230, 187, 255);
                                            border-radius:5px;
                                            color: rgb(208, 208, 208)}
                                            QLineEdit:hover{
                                            background-color: rgb(141, 72, 215);
                                            border:2px solid rgb(230, 187, 255);
                                            border-radius:5px;}
                                            QLineEdit:focus{
                                            background-color: rgb(134, 69, 208);
                                            border:2px solid rgb(230, 187, 255);
                                            border-radius:5px;
                                            color: rgb(230, 187, 255);}""")
                self.sc.senhaIncorreta.close()
                self.sc.senha.setText('')
                po2 = QPoint(210, 30)
                po1 = QPoint(100, 30)
                oi = 0
                of = 0.9
                lpof = QPoint(165, 10)
                lpoi = QPoint(230, 10)
                self.sc.troca.setText('Usar Face id')

            self.senha_pos = QPropertyAnimation(self.sc.senha, b'pos')
            self.senha_pos.setStartValue(po1)
            self.senha_pos.setEndValue(po2)
            self.senha_pos.setDuration(300)
            self.senha_pos.setEasingCurve(QEasingCurve.InOutBack)

            self.senha_opacity = QPropertyAnimation(self.senha_opacity, b'opacity')
            self.senha_opacity.setStartValue(oi)
            self.senha_opacity.setEndValue(of)
            self.senha_opacity.setDuration(300)

            self.logocam_animatio = QPropertyAnimation(self.sc.logoCamera, b'pos')
            self.logocam_animatio.setStartValue(lpoi)
            self.logocam_animatio.setEndValue(lpof)
            self.logocam_animatio.setEasingCurve(QEasingCurve.InOutBack)
            self.logocam_animatio.setDuration(300)

            self.anima_goup_senha = QParallelAnimationGroup()
            self.anima_goup_senha.addAnimation(self.senha_pos)
            self.anima_goup_senha.addAnimation(self.senha_opacity)
            self.anima_goup_senha.addAnimation(self.logocam_animatio)
            self.anima_goup_senha.start()

    # corrigis o bug daa animação da troca de senha e face id
    def corrigi_bug(self):
        self.senha_dropShadow = QGraphicsDropShadowEffect(self.sc.senha)
        self.senha_dropShadow.setBlurRadius(15)
        self.senha_dropShadow.setXOffset(0)
        self.senha_dropShadow.setYOffset(0)
        self.senha_dropShadow.setColor(QColor(0, 0, 0, 0))
        if not self.sc.senha.pos().x() == 210:
            self.sc.senha.setGraphicsEffect(self.senha_dropShadow)

    # verifica se a senha do do ultimo utilizador está certa ou não quando ele volta para entrar
    def confirma_senha(self):  # neste metodo fata addd o metodo que mostra a janela
        global UsuiarioGlobal
        senha_ultimo_user = criptografar(self.sc.senha.text())
        if senha_ultimo_user == self.senhaUltimoUser:
            self.sc.senha.setStyleSheet("""
            background-color: rgb(150, 76, 228);
            color: rgb(208, 208, 208);
            border:2px solid rgb(85, 255, 127);
            border-radius:5px;""")
            id = self.identificarUltimoUsuario(self.sc.NameEmp.text())
            self.inserirUltimoUserInBD(id)
            UsuiarioGlobal = self.nomeDoUsuario
            QTimer.singleShot(30, lambda: self.OpenResize())
            QTimer.singleShot(750, lambda: self.mainWindowMethod())
            QTimer.singleShot(1000, lambda: self.close())

        else:
            self.sc.senhaIncorreta.show()
            self.senha_atual = len(self.sc.senha.text())
            self.sc.senha.setStyleSheet("""
                       background-color: rgb(150, 76, 228);
                       border:2px solid rgb(255, 0, 0);
                       color: rgb(208, 208, 208);
                       border-radius:5px;""")
            QTimer.singleShot(50, lambda: self.sc.senha.setGeometry(208, self.sc.senha.pos().y(), 130, 25))
            QTimer.singleShot(100, lambda: self.sc.senha.setGeometry(212, self.sc.senha.pos().y(), 130, 25))
            QTimer.singleShot(150, lambda: self.sc.senha.setGeometry(208, self.sc.senha.pos().y(), 130, 25))
            QTimer.singleShot(200, lambda: self.sc.senha.setGeometry(212, self.sc.senha.pos().y(), 130, 25))
            QTimer.singleShot(250, lambda: self.sc.senha.setGeometry(208, self.sc.senha.pos().y(), 130, 25))
            QTimer.singleShot(300, lambda: self.sc.senha.setGeometry(212, self.sc.senha.pos().y(), 130, 25))
            QTimer.singleShot(350, lambda: self.sc.senha.setGeometry(210, self.sc.senha.pos().y(), 130, 25))
            QTimer.singleShot(350, lambda: self.senha_anaiticTimer.start())

    # este metodo e responsavel pala cor voltar ao normal Quando erra a senha
    def senha_analitic(self, n):

        if n != self.senha_atual:
            self.sc.senha.setStyleSheet("""QLineEdit{
                                            background-color: rgb(150, 76, 228);
                                            border:1px solid rgb(230, 187, 255);
                                            border-radius:5px;
                                            color: rgb(208, 208, 208)}
                                            QLineEdit:hover{
                                            background-color: rgb(141, 72, 215);
                                            border:2px solid rgb(230, 187, 255);
                                            border-radius:5px;}
                                            QLineEdit:focus{
                                            background-color: rgb(134, 69, 208);
                                            border:2px solid rgb(230, 187, 255);
                                            border-radius:5px;
                                            color: rgb(230, 187, 255);};}""")
            self.senha_anaiticTimer.stop()
            self.sc.senhaIncorreta.close()

    # este metod e responsavel animação e troca de pagina
    def troca_usuario(self):

        if not self.sc.CentralFrame.height() == 250:
            QTimer.singleShot(10, lambda: self.OpenResize())

        name = self.sender().objectName()

        if name == 'TrocaDeUsuario':
            QTimer.singleShot(50, lambda: self.sc.stackedWidget_4.setCurrentWidget(self.sc.page_login))
        elif name == "camera":
            self.Redimencionar = False
            self.sc.label_2.close()
            self.sc.faceid_login_2.close()
            QTimer.singleShot(50, lambda: self.sc.stackedWidget_4.setCurrentWidget(self.sc.page_webCam))

    # responsavel pela confirmação do email e da senha do usuario que quer mudar de utilizador
    def confirma_senha_name(self):
        global UsuiarioGlobal
        nomeConst = ''
        id = 0
        senhaConst = ''
        user = False

        nome_pego = self.sc.email_login.text()
        for n, nome in enumerate(self.listaUsuarios):

            if nome == nome_pego:
                nomeConst = nome
                id = n
                user = True
                break
            else:
                if n == len(self.listaUsuarios) - 1:
                    self.sc.email_login.setStyleSheet("""background-color:rgb(134, 69, 208);
                                                  border:2px solid rgb(255, 0, 0);
                                                  color: rgb(208, 208, 208);
                                                  border-radius:5px;
                                                  padding-left:3px;""")
                    self.tamanhoNomeat = len(self.sc.email_login.text())
                    QTimer.singleShot(200, lambda: self.nomeloginTimer.start())

        if user:
            senha = criptografar(self.sc.password.text())

            if senha == self.listaSenha[id]:
                self.sc.password.setStyleSheet("""
                            background-color: #8200c3;
                            color: rgb(208, 208, 208);
                            border:2px solid rgb(85, 255, 127);
                            border-radius:5px;""")
                self.sc.email_login.setStyleSheet("""
                            background-color: #8200c3;
                            color: rgb(208, 208, 208);
                            border:2px solid rgb(85, 255, 127);
                            border-radius:5px;""")
                self.inserirUltimoUserInBD(str(id+1))
                UsuiarioGlobal = self.listaUsuarios[id]
                QTimer.singleShot(200, lambda: self.mainWindowMethod())
                QTimer.singleShot(500, lambda: self.close())
            else:
                self.passwordConst = len(self.sc.password.text())
                self.sc.password.setStyleSheet("""background-color:rgb(134, 69, 208);
                                                  border:2px solid rgb(255, 0, 0);
                                                  color: rgb(208, 208, 208);
                                                  border-radius:5px;
                                                  padding-left:3px;""")
                self.passwordTimer.start()
                # self.sc.senhaIncorreta_2.show()

    # este metodo e responsavel pala cor voltar ao normal Quando erra a senha
    def namelogin(self, n):

        if n != self.tamanhoNomeat:
            self.sc.email_login.setStyleSheet("""QLineEdit{
                                                    background-color: rgb(150, 76, 228);
                                                    border:1px solid rgb(230, 187, 255);
                                                    border-radius:5px;
                                                    color: rgb(208, 208, 208);
                                                    padding-left:3px;}
                                                    QLineEdit:hover{
                                                    background-color: rgb(141, 72, 215);
                                                    border:2px solid rgb(230, 187, 255);
                                                    border-radius:5px;}
                                                    QLineEdit:focus{
                                                    background-color: rgb(134, 69, 208);
                                                    border:2px solid rgb(230, 187, 255);
                                                    border-radius:5px;
                                                    color: rgb(230, 187, 255);}""")
            self.nomeloginTimer.stop()

    # este metodo e responsavel pala cor voltar ao normal Quando erra a senha
    def passworveri(self, n):

        if n != self.passwordConst:
            self.sc.password.setStyleSheet("""QLineEdit{
                                            background-color: rgb(150, 76, 228);
                                            border:1px solid rgb(230, 187, 255);
                                            border-radius:5px;
                                            color: rgb(208, 208, 208);
                                            padding-left:3px;}
                                            QLineEdit:hover{
                                            background-color: rgb(141, 72, 215);
                                            border:2px solid rgb(230, 187, 255);
                                            border-radius:5px;}
                                            QLineEdit:focus{
                                            background-color: rgb(134, 69, 208);
                                            border:2px solid rgb(230, 187, 255);
                                            border-radius:5px;
                                            color: rgb(230, 187, 255);}""")
            self.passwordTimer.stop()
            self.sc.senhaIncorreta_2.close()

    # este metodo é responsavel pela animação da troca pelo singup
    def animationSingUp(self):

        btn = self.sender().objectName()
        self.sc.email_login.setText('')
        self.sc.password.setText('')
        self.sc.password1.setText('')
        self.sc.password2.setText('')
        self.sc.email_singup.setText('')

        if btn == 'sengup':
            li = 241
            lf = 0
            si = 0
            sf = 241
            self.sc.email_singup.setStyleSheet("""
                                                QLineEdit{
                                                background-color: rgb(150, 76, 228);
                                                border:1px solid rgb(230, 187, 255);
                                                border-radius:5px;
                                                color: rgb(208, 208, 208);
                                                padding-left:3px;}
                                                QLineEdit:hover{
                                                background-color: rgb(141, 72, 215);
                                                border:2px solid rgb(230, 187, 255);
                                                border-radius:5px;}
                                                QLineEdit:focus{
                                                background-color: rgb(134, 69, 208);
                                                border:2px solid rgb(230, 187, 255);
                                                border-radius:5px;
                                                color: rgb(230, 187, 255);}""")
            self.sc.email_login.setStyleSheet("""QLineEdit{
                                                background-color: rgb(150, 76, 228);
                                                border:1px solid rgb(230, 187, 255);
                                                border-radius:5px;
                                                color: rgb(208, 208, 208);
                                                padding-left:3px;}
                                                QLineEdit:hover{
                                                background-color: rgb(141, 72, 215);
                                                border:2px solid rgb(230, 187, 255);
                                                border-radius:5px;}
                                                QLineEdit:focus{
                                                background-color: rgb(134, 69, 208);
                                                border:2px solid rgb(230, 187, 255);
                                                border-radius:5px;
                                                color: rgb(230, 187, 255);}""")
            # self.sc.poucosCaracter.close()
        elif btn == 'login_btn_singup':
            self.sc.email_singup.setStyleSheet("""QLineEdit{
                background-color: rgb(150, 76, 228);
                border:1px solid rgb(230, 187, 255);
                border-radius:5px;
                color: rgb(208, 208, 208);
                padding-left:3px;}
                QLineEdit:hover{
                background-color: rgb(141, 72, 215);
                border:2px solid rgb(230, 187, 255);
                border-radius:5px;}
                QLineEdit:focus{
                background-color: rgb(134, 69, 208);
                border:2px solid rgb(230, 187, 255);
                border-radius:5px;
                color: rgb(230, 187, 255);}""")
            self.sc.email_login.setStyleSheet("""QLineEdit{
                                            background-color: rgb(150, 76, 228);
                                            border:1px solid rgb(230, 187, 255);
                                            border-radius:5px;
                                            color: rgb(208, 208, 208);
                                            padding-left:3px;}
                                            QLineEdit:hover{
                                            background-color: rgb(141, 72, 215);
                                            border:2px solid rgb(230, 187, 255);
                                            border-radius:5px;}
                                            QLineEdit:focus{
                                            background-color: rgb(134, 69, 208);
                                            border:2px solid rgb(230, 187, 255);
                                            border-radius:5px;
                                            color: rgb(230, 187, 255);}""")
            # self.sc.poucosCaracter.close()
            li = 0
            lf = 241
            si = 241
            sf = 0

        self.loginAnimation = QPropertyAnimation(self.sc.login, b'minimumWidth')
        self.loginAnimation.setStartValue(li)
        self.loginAnimation.setEndValue(lf)
        self.loginAnimation.setDuration(300)
        self.loginAnimation.setEasingCurve(QEasingCurve.InOutCirc)

        self.singupAnimtion = QPropertyAnimation(self.sc.singup, b'minimumWidth')
        self.singupAnimtion.setStartValue(si)
        self.singupAnimtion.setEndValue(sf)
        self.singupAnimtion.setDuration(300)
        self.singupAnimtion.setEasingCurve(QEasingCurve.InOutCirc)

        self.group_animation_login = QParallelAnimationGroup()
        self.group_animation_login.addAnimation(self.loginAnimation)
        self.group_animation_login.addAnimation(self.singupAnimtion)
        self.group_animation_login.start()

    # responsavel pela entrada de novos usuarios
    def singup(self):
        global UsuiarioGlobal

        if len(self.sc.email_singup.text()) < 3:
            self.sc.email_singup.setStyleSheet("""background-color: rgb(150, 76, 228);
                                                border:2px solid rgb(227, 0, 58);
                                                border-radius:5px;
                                                color: rgb(208, 208, 208);
                                                padding-left:3px;""")
            self.emailsingupCont = len(self.sc.email_singup.text())
            QTimer.singleShot(100, lambda: self.emailsingupTimer.start())

        newUser = self.IsNewUser(self.sc.email_singup.text())

        if newUser:
            if self.sc.password1.text() == '':
                self.sc.password1.setStyleSheet("""background-color: rgb(150, 76, 228);
                                                                border:2px solid rgb(227, 0, 58);
                                                                border-radius:5px;
                                                                color: rgb(208, 208, 208);
                                                                padding-left:3px;""")
                self.passwor1Cont = len(self.sc.password1.text())
                QTimer.singleShot(300, lambda: self.password1Timer.start())
            else:
                if self.sc.password1.text() != self.sc.password2.text():
                    self.sc.password2.setStyleSheet("""background-color: rgb(150, 76, 228);
                                                        border:2px solid rgb(227, 0, 58);
                                                        border-radius:5px;
                                                        color: rgb(208, 208, 208);
                                                        padding-left:3px;""")
                    self.sc.senhaIncorreta_3.show()
                    self.passwor2Cont = len(self.sc.password2.text())
                    QTimer.singleShot(300, lambda: self.password2Timer.start())
                else:
                    senha = criptografar(self.sc.password2.text())
                    self.database.connect_database()
                    self.database.executarComand(f"""
                    INSERT INTO Usuario (nome, password, admin) values ('{self.sc.email_singup.text()}','{senha}', 'F')
                                                    """)
                    self.database.close_connection_database()

                    self.inserirUltimoUserInBD(self.contarRegistrosTabelaUser())
                    UsuiarioGlobal = self.sc.email_singup.text()

                    self.sc.password1.setStyleSheet("""
                                                background-color: #8200c3;
                                                color: rgb(208, 208, 208);
                                                border:2px solid rgb(85, 255, 127);
                                                border-radius:5px;""")
                    self.sc.password2.setStyleSheet("""
                                                background-color: #8200c3;
                                                color: rgb(208, 208, 208);
                                                border:2px solid rgb(85, 255, 127);
                                                border-radius:5px;""")
                    self.sc.email_singup.setStyleSheet("""
                                                background-color: #8200c3;
                                                color: rgb(208, 208, 208);
                                                border:2px solid rgb(85, 255, 127);
                                                border-radius:5px;""")

                    self.mainWindowMethod()
                    self.close()
        else:
            self.sc.email_singup.setStyleSheet("""background-color: rgb(150, 76, 228);
                                                            border:2px solid rgb(227, 0, 58);
                                                            border-radius:5px;
                                                            color: rgb(208, 208, 208);
                                                            padding-left:3px;""")
            self.emailsingupCont = len(self.sc.email_singup.text())
            QTimer.singleShot(100, lambda: self.emailsingupTimer.start())

    # este metodo e responsavel pala cor voltar ao normal Quando erra a senha
    def emailsingup(self, n):

        if n != self.emailsingupCont:
            self.sc.email_singup.setStyleSheet("""QLineEdit{
                                                background-color: rgb(150, 76, 228);
                                                border:1px solid rgb(230, 187, 255);
                                                border-radius:5px;
                                                color: rgb(208, 208, 208);
                                                padding-left:3px;}
                                                QLineEdit:hover{
                                                background-color: rgb(141, 72, 215);
                                                border:2px solid rgb(230, 187, 255);
                                                border-radius:5px;}
                                                QLineEdit:focus{
                                                background-color: rgb(134, 69, 208);
                                                border:2px solid rgb(230, 187, 255);
                                                border-radius:5px;
                                                color: rgb(230, 187, 255);}""")
            self.emailsingupTimer.stop()

    # este metodo e responsavel pala cor voltar ao normal Quando erra a senha
    def passwor1(self, n):

        if n != self.passwor1Cont:
            self.sc.password1.setStyleSheet("""QLineEdit{
                                                background-color: rgb(150, 76, 228);
                                                border:1px solid rgb(230, 187, 255);
                                                border-radius:5px;
                                                color: rgb(208, 208, 208);
                                                padding-left:3px;}
                                                QLineEdit:hover{
                                                background-color: rgb(141, 72, 215);
                                                border:2px solid rgb(230, 187, 255);
                                                border-radius:5px;}
                                                QLineEdit:focus{
                                                background-color: rgb(134, 69, 208);
                                                border:2px solid rgb(230, 187, 255);
                                                border-radius:5px;
                                                color: rgb(230, 187, 255);}""")
            self.password1Timer.stop()

    # este metodo e responsavel pala cor voltar ao normal Quando erra a senha
    def passwor2(self, n):

        if n != self.passwor2Cont:
            self.sc.password2.setStyleSheet("""QLineEdit{
                                                background-color: rgb(150, 76, 228);
                                                border:1px solid rgb(230, 187, 255);
                                                border-radius:5px;
                                                color: rgb(208, 208, 208);
                                                padding-left:3px;}
                                                QLineEdit:hover{
                                                background-color: rgb(141, 72, 215);
                                                border:2px solid rgb(230, 187, 255);
                                                border-radius:5px;}
                                                QLineEdit:focus{
                                                background-color: rgb(134, 69, 208);
                                                border:2px solid rgb(230, 187, 255);
                                                border-radius:5px;
                                                color: rgb(230, 187, 255);}""")
            self.password2Timer.stop()
            self.sc.senhaIncorreta_3.close()

    # este metodo é responsavel por testar se existe uma WebCam
    def TestWebCam(self):
        """
        este metodo ele analisa se a seu tem uma webcam no seu pc
        """
        global CLASSIFICADORLBPH, HAARCASCADES

        self.webCam = cv2.VideoCapture(0)

        if self.webCam.isOpened():
            self.webCam.set(3, 320)
            self.webCam.set(4, 240)

            self.sc.camera.setToolTip("WebCamON")
            self.sc.camera_2.setToolTip("WebCamON")

    # este metodo é responsavel pelo reconhecimento facial
    def openAnalising(self):
        global CONT, NOMEUSER

        connect, frameImg = self.webCam.read()

        if connect:
            imagem = cv2.cvtColor(frameImg, cv2.COLOR_BGR2RGB)
            cinzaImg = cv2.cvtColor(frameImg, cv2.COLOR_BGR2GRAY)

            detect = self.ClassificadorDeVideo.detectMultiScale(cinzaImg)
            for (x, y, l, a) in detect:
                imagem = cv2.rectangle(imagem, (x, y), (x+l, y+a), (22, 22, 22), 1)
                faceImg = cv2.resize(cinzaImg[y:y + a, x:x + l], (100, 100))

                iden, conf = self.Reconhecedor.predict(faceImg)

                fontColor = (170, 85, 255)

                if iden == 1:
                    name = 'Daniel'
                elif iden == 0:
                    name = 'Desconhecido'
                else:
                    name = 'outro'

                CONT += 1

                if CONT > 60 and iden == 1:
                    NOMEUSER = name
                    self.fecharWebcamTimer.start()
                    self.sc.logoCamera.setPixmap(QPixmap(u"../img/Instagram_90_openv_px.png"))
                    self.inserirUltimoUserInBD(1)
                    fontColor = (85, 255, 127)
                    if not self.sc.CentralFrame.height() == 250 and self.Redimencionar:#########################
                        QTimer.singleShot(30, lambda: self.OpenResize())###
                        QTimer.singleShot(900, lambda: self.mainWindowMethod())
                        QTimer.singleShot(1000, lambda: self.close())
                    else:
                        QTimer.singleShot(400, lambda: self.mainWindowMethod())
                        QTimer.singleShot(5000, lambda: self.close())

                if CONT > 60 and iden == 0:
                    NOMEUSER = name
                    self.sc.logoCamera.setPixmap(QPixmap(u"../img/Instagram_90_offpx.png"))
                    fontColor = (255, 0, 0)
                    y = self.sc.logoCamera.pos().y()
                    ####### criar uma sequencial group animation
                    QTimer.singleShot(50, lambda: self.sc.logoCamera.setGeometry(230, y, 81, 91))
                    QTimer.singleShot(100, lambda: self.sc.logoCamera.setGeometry(233, y, 81, 91))
                    QTimer.singleShot(150, lambda: self.sc.logoCamera.setGeometry(230, y, 81, 91))
                    QTimer.singleShot(200, lambda: self.sc.logoCamera.setGeometry(227, y, 81, 91))
                    QTimer.singleShot(250, lambda: self.sc.logoCamera.setGeometry(230, y, 81, 91))
                    QTimer.singleShot(300, lambda: self.sc.logoCamera.setGeometry(233, y, 81, 91))
                    QTimer.singleShot(350, lambda: self.sc.logoCamera.setGeometry(230, y, 81, 91))
                    QTimer.singleShot(400, lambda: self.sc.logoCamera.setPixmap(
                        QPixmap(u"../img/Instagram_90px.png")))
                    CONT = 0
                    # fontColor = (170, 85, 255)

                cv2.putText(imagem, name, (x, y + (a+30)), self.Fonte, 1, fontColor)

            height, width, channel = imagem.shape
            step = channel * width
            qImag = QImage(imagem.data, width, height, step, QImage.Format_RGB888)
            self.sc.WebCam.setPixmap(QPixmap.fromImage(qImag))

    # pega a posição  do incon da cametra e e do alineEdit da senha
    def closeEndOpenAnalisi(self):

        pos_atual = self.sc.senha.pos().x()

        if not pos_atual == 210:
            if not self.openAnalisingTimer.isActive():
                self.atraso = True
                QTimer.singleShot(2000, lambda: self.openAnalisingTimer.start())
        else:
            QTimer.singleShot(20, lambda: self.fecharWebcamTimer.start())

    # este metodo é responsavel por encerrar o reconhecimento
    def fecharWebcam(self):
        if self.openAnalisingTimer.isActive() and self.atraso:
            self.openAnalisingTimer.stop()
            self.webCam.release()
            self.fecharWebcamTimer.stop()

    def ListaUsuarioInBD(self):
        self.database.connect_database()
        registroDados = self.database.executarFetchall(f"SELECT * FROM Usuario")
        self.database.close_connection_database()

        for tupla in registroDados:
            for n, dado in enumerate(tupla):
                if n == 1:
                    self.listaUsuarios.append(dado)
                if n == 2:
                    self.listaSenha.append(dado)
                if n == 3:
                    self.listaAcesso.append(dado)

    # este metodo é respposavel por mostrar a tela principal
    def mainWindowMethod(self):
        self.mainWindow = MainwindowSC()
    # este metodo e esponsaver por verificar o ultimo usuario e lhe facilitar em por apana a senha
    def VerificarUltimoUser(self):
        nomeUltimoUser = ''
        ultimasenha = ''
        self.database.connect_database()
        dados = self.database.executarFetchall("""
        SELECT UltimoUsuario.idUltimo, Usuario.nome, Usuario.password FROM UltimoUsuario JOIN Usuario  ON UltimoUsuario.UltimoUsuario = Usuario.id
        """)
        self.database.close_connection_database()
        for dado in dados:
            for n, d in enumerate(dado):
                if n == 1:
                    nomeUltimoUser = d
                if n == 2:
                    ultimasenha = d
        self.senhaUltimoUser = ultimasenha
        self.sc.NameEmp.setText(nomeUltimoUser)
        self.nomeDoUsuario = nomeUltimoUser

    # este metodo envia o nome  e a senha do ultimo usuario
    def inserirUltimoUserInBD(self, id):
        # data e o id do ultimo usuario
        dataHoje = date.today()
        self.database.connect_database()
        self.database.executarComand(f"INSERT INTO UltimoUsuario (Data, UltimoUsuario)values('{dataHoje}','{id}')")
        self.database.close_connection_database()

    # este metodo e responsavel pro contar o numero de registro (tuplas na base de dados)
    def contarRegistrosTabelaUser(self):

        self.database.connect_database()
        registro = self.database.executarFetchall("SELECT * FROM Usuario")
        self.database.close_connection_database()

        return str(len(registro)+1)

    # este metodo e responvael por saber a posição no ultimo usuario
    def identificarUltimoUsuario(self, nome):
        self.database.connect_database()
        listDados = self.database.executarFetchall(f"SELECT * FROM Usuario")
        self.database.close_connection_database()

        id = 0
        for dados in listDados:
            cont = 0
            for n, dado in enumerate(dados):
                cont += 1
                if n == 0:
                    id = dado

                if n == 1:
                    if dado == nome:
                        return id
                        break
                    else:
                        id = 0

        return id

    # este metodo e para saber se o nome do novo usuario ja existe
    def IsNewUser(self, userNome):
        self.database.connect_database()
        self.database.connect_database()
        usuario = self.database.executarFetchall("SELECT * FROM Usuario")
        self.database.connect_database()
        newuser = True
        for user in usuario:
            for n, use in enumerate(user):

                if n == 1:
                    if use == userNome:
                        newuser = False
        return newuser




class MainwindowSC(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindowMW()
        self.ui.setupUi(self)

        self.move(140, 15)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMinimumSize(1117, 712)
        self.toobtn = True

        self.eventoConnect()

        self.ui.minimisar.clicked.connect(lambda: self.showMinimized())
        self.ui.NormalMax.clicked.connect(lambda: self.MaxMin())
        self.ui.fechar.clicked.connect(lambda: quit())

        self.ui.settings.clicked.connect(self.leftmenu)
        self.ui.double_up.clicked.connect(self.scrollAreaAnimat)
        self.ui.web_btn.clicked.connect(self.areaClick)
        self.ui.help_btn.clicked.connect(self.areaClick)
        self.ui.setting_btn.clicked.connect(self.areaClick)
        self.ui.coins_btn.clicked.connect(self.areaClick)
        self.ui.setting_user_btn.clicked.connect(self.areaClick)
        self.ui.editTest.clicked.connect(self.areaClick)
        self.ui.perfil_btn.clicked.connect(self.areaClick)
        self.ui.web_btn_2.clicked.connect(self.areaClick)
        self.ui.Home.clicked.connect(self.areaClick)
        self.ui.GoogleFinance_btl.clicked.connect(self.areaClick)
        self.ui.YahooFinance_btn.clicked.connect(self.areaClick)

        self.ui.investing_btn.clicked.connect(self.areaClick)
        self.ui.BLHL_btn.clicked.connect(self.areaClick)
        self.ui.Infomaney_btn.clicked.connect(self.areaClick)
        self.ui.Dinherama_btn.clicked.connect(self.areaClick)
        self.ui.CMEgroup_btn.clicked.connect(self.areaClick)
        self.ui.Economia_btn.clicked.connect(self.areaClick)
        self.ui.help_btnF_2.clicked.connect(self.areaClick)

        # responsavel por abrir salvar e criar arquivos
        self.ui.save.clicked.connect(self.editArq)
        self.ui.open.clicked.connect(self.editArq)
        self.ui.update.clicked.connect(self.navegWeb)
        self.ui.arrow_left.clicked.connect(self.navegWeb)
        self.ui.arrow_right.clicked.connect(self.navegWeb)
        self.ui.voz_btn.clicked.connect(self.captacaoAudio)


        self.ui.LineUrl.returnPressed.connect(lambda: self.loandEx(self.ui.LineUrl.text()))
        self.ui.pesquisar_btn.clicked.connect(lambda: self.loandEx(self.ui.LineUrl.text()))

        # ler texto
        self.ui.toolButton.clicked.connect(self.areaClick)
        self.toobtn = False

        self.left = CustomGrip(self, Qt.LeftEdge, True)
        self.right = CustomGrip(self, Qt.RightEdge, True)
        self.top = CustomGrip(self, Qt.TopEdge, True)
        self.bottom = CustomGrip(self, Qt.BottomEdge, True)

        self.show() # mostrar janela

        self.TimerFont = QTimer()
        self.TimerFont.timeout.connect(lambda: self.tamanhoFont())

        self.timerHistorico = QTimer()
        self.timerHistorico.timeout.connect(lambda: self.pegarURLcriarHistorico())
        # asad
        self.repAudioTimer = QTimer()
        self.repAudioTimer.timeout.connect(lambda: self.repAudio())

        self.listaURL = []
        # conectar com metodo textChanged para a aconversao  de moeda
        self.ui.bitcoin_LEdit.textChanged.connect(self.bitcoin_LEditTextChanged)
        self.ui.bitcoin_aoa_LEdit.textChanged.connect(self.bitcoin_aoa_LEditTextChanged)
        self.ui.DK_LEdit.textChanged.connect(self.DK_LEditTextChanged)
        self.ui.DK_aoa_LEdit.textChanged.connect(self.DK_aoa_LEditTextChanged)
        self.ui.DB_LEdit.textChanged.connect(self.DB_LEditTextChanged)
        self.ui.DB_aoa_LEdit.textChanged.connect(self.DB_aoa_LEditTextChanged)
        self.ui.RO_LEdit.textChanged.connect(self.RO_LEditTextChanged)
        self.ui.RO_aoa_LEdit.textChanged.connect(self.RO_aoa_LEditTextChanged)
        self.ui.DJ_LEdit.textChanged.connect(self.DJ_LEditTextChanged)
        self.ui.DJ_aoa_LEdit.textChanged.connect(self.DJ_aoa_LEditTextChanged)
        self.ui.DC_LEdit.textChanged.connect(self.DC_LEditTextChanged)
        self.ui.DC_aoa_LEdit.textChanged.connect(self.DC_aoa_LEditTextChanged)
        self.ui.LE_LEdit.textChanged.connect(self.LE_LEditTextChanged)
        self.ui.LE_aoa_LEdit.textChanged.connect(self.LE_aoa_LEditTextChanged)
        self.ui.E_LEdit.textChanged.connect(self.E_LEditTextChanged)
        self.ui.E_aoa_LEdit.textChanged.connect(self.E_aoa_LEditTextChanged)
        self.ui.FS_LEdit.textChanged.connect(self.FS_LEditTextChanged)
        self.ui.FS_aoa_LEdit.textChanged.connect(self.FS_aoa_LEditTextChanged)
        self.ui.DNA_LEdit.textChanged.connect(self.DNA_LEditTextChanged)
        self.ui.DNA_aoa_LEdit.textChanged.connect(self.DNA_aoa_LEditTextChanged)



    # pega a posicao global
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        self.dragPosScroll = self.ui.scrollArea.horizontalScrollBar().value()
        self.dragPosScroll2 = self.ui.scrollArea_6.horizontalScrollBar().value()
        self.dragPosScrollV = self.ui.scrollArea_4.verticalScrollBar().value()

    # eventos e coneccoes
    def eventoConnect(self):
        ##################################
        # EVENTO PARA MOVER A JANELA
        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()

                if self.cursor().pos().y() <= 5:
                    self.MaxMin()
                event.accept()

        # EVENTO PARA MAXIMIZAR E NORMALIZAR A JANELA
        def mouseDoubleClickEvent(event):
            if event.type() == QEvent.MouseButtonDblClick:
                self.MaxMin()

        self.ui.barraTitulo.mouseMoveEvent = moveWindow  # MOVER JANELA
        self.ui.barraTitulo.mouseDoubleClickEvent = mouseDoubleClickEvent  # MAXIMIZA E MINIMIZAR A JANELA

        #############################################################################
        # TOSD OS EVENTOS A BAIXO SAO EVENTOS DE CLICK DO FRAMES DE TECNOLOGIA

        def GoogleFinanceMousePressEvent(event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.simpficaLond(self.ui.page_Extras, 0, "https://www.google.com/finance/?hl=pt")

        def YahooFinanceMousePressEvent(event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.simpficaLond(self.ui.page_Extras, 0, "https://finance.yahoo.com/")

        def InvestingMousePressEvent(event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.simpficaLond(self.ui.page_Extras, 0, """https://www.investing.com/""")

        def BLHLMousePressEvent(event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.simpficaLond(self.ui.page_Extras, 0, "https://www.nutsaboutmoney.com/investing/hargreaves-lansdown-alternatives")

        def InfomaneyMousePressEvent(event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.simpficaLond(self.ui.page_Extras, 0, "https://www.infomoney.com.br/")

        def DinheramaMousePressEvent(event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.simpficaLond(self.ui.page_Extras, 0, "https://dinheirama.com/")

        def CMEgroupMousePressEvent(event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.simpficaLond(self.ui.page_Extras, 0, "https://www.cmegroup.com/")

        def EconomiaMousePressEvent(event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.simpficaLond(self.ui.page_Extras, 0, "https://www.dropbox.com/")

        def AndroidMousePressEvent(event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.simpficaLond(self.ui.page_Extras, 0, "https://www.android.com/")

        def HelpMousePressEvent(event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.simpficaLond(self.ui.page_Extras, 0, "https://dinheirama.com/")


        self.ui.frame_GoogleFinance.mousePressEvent = GoogleFinanceMousePressEvent
        self.ui.GoogleFinance_lbl.mousePressEvent = GoogleFinanceMousePressEvent
        self.ui.frame_YahooFinance.mousePressEvent = YahooFinanceMousePressEvent
        self.ui.YahooFinance_lbl.mousePressEvent = YahooFinanceMousePressEvent
        self.ui.frame_Investing.mousePressEvent = InvestingMousePressEvent
        self.ui.Investing_lbl.mousePressEvent = InvestingMousePressEvent
        self.ui.frame_BLHL.mousePressEvent = BLHLMousePressEvent
        self.ui.BLHL_lbl.mousePressEvent = BLHLMousePressEvent
        self.ui.frame_Infomaney.mousePressEvent = InfomaneyMousePressEvent
        self.ui.Infomaney_lbl.mousePressEvent = InfomaneyMousePressEvent
        self.ui.frame_Dinherama.mousePressEvent = DinheramaMousePressEvent
        self.ui.Dinherama_lbl.mousePressEvent = DinheramaMousePressEvent
        self.ui.frame_CMEgroup.mousePressEvent = CMEgroupMousePressEvent
        self.ui.CMEgroup_lbl.mousePressEvent = CMEgroupMousePressEvent
        self.ui.frame_Economia.mousePressEvent = EconomiaMousePressEvent
        self.ui.Economia_lbl.mousePressEvent = EconomiaMousePressEvent
        self.ui.frame_Helpe.mousePressEvent = HelpMousePressEvent
        self.ui.help_lbl.mousePressEvent = HelpMousePressEvent

       #######################################################################
        # evento responsavel por mover o scroll pelos frmames

        self.scrollPrimary = 0
        self.cursorPrimary = 0
        self.logCursor = True
        self.dragPosScroll = self.ui.scrollArea.horizontalScrollBar().value()
        def moveScroll(event: QMouseEvent):
            if event.buttons() == Qt.LeftButton:
                if self.cursorPrimary == 0 and self.logCursor == True:
                    self.cursorPrimary = self.cursor().pos().x()
                    self.logCursor = False

                valor = (self.cursor().pos().x() - (self.cursorPrimary + self.scrollPrimary))
                self.ui.scrollArea.horizontalScrollBar().setValue(self.dragPosScroll - valor)
                event.accept()

        def releasecroll(event: QMouseEvent):
            if event.type() == QEvent.MouseButtonRelease:
                self.cursorPrimary = 0
                self.logCursor = True
                self.scrollPrimary = self.ui.scrollArea.horizontalScrollBar().value()
                event.accept()

        # conectcoes responsavel por mover o scroll pelos frmames
        self.ui.frame_GoogleFinance.mouseMoveEvent = moveScroll
        self.ui.frame_GoogleFinance.mouseReleaseEvent = releasecroll

        self.ui.frame_CMEgroup.mouseMoveEvent = moveScroll
        self.ui.frame_CMEgroup.mouseReleaseEvent = releasecroll

        self.ui.frame_YahooFinance.mousePressEvent = moveScroll
        self.ui.frame_YahooFinance.mouseReleaseEvent = releasecroll

        self.ui.frame_Helpe.mousePressEvent = moveScroll
        self.ui.frame_Helpe.mouseReleaseEvent = releasecroll

        self.ui.frame_raspberry.mouseMoveEvent = moveScroll
        self.ui.frame_raspberry.mouseReleaseEvent = releasecroll

        self.ui.frame_Economia.mouseMoveEvent = moveScroll
        self.ui.frame_Economia.mouseReleaseEvent = releasecroll

        self.ui.frame_Dinherama.mouseMoveEvent = moveScroll
        self.ui.frame_Dinherama.mouseReleaseEvent = releasecroll

        self.ui.frame_Infomaney.mouseMoveEvent = moveScroll
        self.ui.frame_Infomaney.mouseReleaseEvent = releasecroll

        self.ui.frame_BLHL.mouseMoveEvent = moveScroll
        self.ui.frame_BLHL.mouseReleaseEvent = releasecroll

        self.ui.frame_Investing.mouseMoveEvent = moveScroll
        self.ui.frame_Investing.mouseReleaseEvent = releasecroll

        self.ui.frame_MarcaTech.mouseMoveEvent = moveScroll
        self.ui.frame_MarcaTech.mouseReleaseEvent = releasecroll

        ########################################################
        ##### scroll das configuaracoes #######################

        #### evento responsavel por mover o scroll pelos frmames

        self.scrollPrimary2 = 0
        self.cursorPrimary2 = 0
        self.logCursor2 = True
        self.dragPosScroll2 = self.ui.scrollArea_6.horizontalScrollBar().value()

        def moveScroll2(event: QMouseEvent):
            if event.buttons() == Qt.LeftButton:
                if self.cursorPrimary2 == 0 and self.logCursor2 == True:
                    self.cursorPrimary2 = self.cursor().pos().x()
                    self.logCursor2 = False
                valor = (self.cursor().pos().x() - (self.cursorPrimary2))
                self.ui.scrollArea_6.horizontalScrollBar().setValue(self.dragPosScroll2 - valor)
                event.accept()

        def releasecroll2(event: QMouseEvent):
            if event.type() == QEvent.MouseButtonRelease:
                self.cursorPrimary2 = 0
                self.logCursor2 = True
                self.scrollPrimary2 = self.ui.scrollArea_6.horizontalScrollBar().value()
                event.accept()

        self.ui.frame_Browsin_history.mouseMoveEvent = moveScroll2
        self.ui.frame_Browsin_history.mouseReleaseEvent = releasecroll2

        self.ui.frame_opening_history.mouseMoveEvent = moveScroll2
        self.ui.frame_opening_history.mouseReleaseEvent = releasecroll2

        self.ui.frame_user_list.mouseMoveEvent = moveScroll2
        self.ui.frame_user_list.mouseReleaseEvent = releasecroll2

        self.ui.frame_password_faceId.mouseMoveEvent = moveScroll2
        self.ui.frame_password_faceId.mouseReleaseEvent = releasecroll2
        # faltam dois historicoa

        ################################################################
        ################### mover os scroll verticamente  ##############


        self.scrollPrimary = 0
        self.cursorPrimary = 0
        self.logCursor = True
        self.dragPosScroll = self.ui.scrollArea_4.verticalScrollBar().value()
        def moveScrollV(event: QMouseEvent):
            if event.buttons() == Qt.LeftButton:
                if self.cursorPrimary == 0 and self.logCursor == True:
                    self.cursorPrimary = self.cursor().pos().y()
                    self.logCursor = False

                valor = (self.cursor().pos().y() - (self.cursorPrimary+self.scrollPrimary))
                self.ui.scrollArea_4.verticalScrollBar().setValue(self.dragPosScroll - valor)
                event.accept()

        def releasecrollV(event: QMouseEvent):
            if event.type() == QEvent.MouseButtonRelease:
                self.cursorPrimary = 0
                self.logCursor = True
                self.scrollPrimary = self.ui.scrollArea_4.verticalScrollBar().value()
                event.accept()

        self.ui.frame_scrollBTC.mouseMoveEvent = moveScrollV
        self.ui.frame_scrollBTC.mouseReleaseEvent = releasecrollV
        self.ui.frame_scrollCHF.mouseMoveEvent = moveScrollV
        self.ui.frame_scrollCHF.mouseReleaseEvent = releasecrollV
        self.ui.frame_scrollEUR.mouseMoveEvent = moveScrollV
        self.ui.frame_scrollEUR.mouseReleaseEvent = releasecrollV
        self.ui.frame_scrollGBP.mouseMoveEvent = moveScrollV
        self.ui.frame_scrollGBP.mouseReleaseEvent = releasecrollV
        self.ui.frame_scrollJOD.mouseMoveEvent = moveScrollV
        self.ui.frame_scrollJOD.mouseReleaseEvent = releasecrollV
        self.ui.frame_scrollKWD.mouseMoveEvent = moveScrollV
        self.ui.frame_scrollKWD.mouseReleaseEvent = releasecrollV
        self.ui.frame_scrollKYD.mouseMoveEvent = moveScrollV
        self.ui.frame_scrollKYD.mouseReleaseEvent = releasecrollV
        self.ui.frame_scrollOMR.mouseMoveEvent = moveScrollV
        self.ui.frame_scrollOMR.mouseReleaseEvent = releasecrollV
        self.ui.frame_scrollUSD.mouseMoveEvent = moveScrollV
        self.ui.frame_scrollUSD.mouseReleaseEvent = releasecrollV
        self.ui.frame_scrollBHD.mouseMoveEvent = moveScrollV
        self.ui.frame_scrollBHD.mouseReleaseEvent = releasecrollV


        # metodo responsavel por maximizar e minimizar

    def MaxMin(self):
        global MNW

        if MNW == 0:

            self.ui.primeiro_container.setStyleSheet("""background-color: rgb(170, 85, 255);border-radius:0px;""")
            self.ui.linha.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:0px;")
            self.ui.frame_central.setStyleSheet("background-color: rgb(170, 85, 255);border-radius:0px;")

            self.showMaximized()
            MNW = 1

            icon = QIcon()
            icon.addFile(u"../img/24x24/cil-window-restore.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.NormalMax.setIcon(icon)
            self.ui.scrollArea.setStyleSheet("QscrolAir{background-color: rgb(85, 255, 255);}"
                                             "QFrame{border-radius:15px;}")
            self.top.hide()
            self.bottom.hide()
            self.left.hide()
            self.right.hide()



        else:
            self.ui.linha.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:15px;")
            self.ui.primeiro_container.setStyleSheet("""background-color: rgb(170, 85, 255);border-radius:15px;""")
            self.ui.frame_central.setStyleSheet("background-color: rgb(170, 85, 255);border-radius:15px;")

            self.showNormal()
            MNW = 0

            self.top.show()
            self.bottom.show()
            self.left.show()
            self.right.show()

            icon = QIcon()
            icon.addFile(u"../img/24x24/cil-media-stop.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.NormalMax.setIcon(icon)

    # ativa o ajust da janela
    def resizeEvent(self, event):
        self.resizeGrips()

    # metodo responsavel pelo ajuste da janela
    def resizeGrips(self):
        self.left.setGeometry(0, 10, 10, self.height())
        self.right.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top.setGeometry(0, 0, self.width(), 10)
        self.bottom.setGeometry(0, self.height() - 10, self.width(), 10)

    # metodo que anima o menu lateral
    def leftmenu(self):
        tamnho_atual = self.ui.left_menu.width()

        i = 0
        f = 0
        if tamnho_atual == 8:
            i = 8
            f = 200
            icon = QIcon()
            icon.addFile(u"../img/24x24/cil-x-f.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.settings.setIcon(icon)
        else:
            i = 200
            f = 8
            icon = QIcon()
            icon.addFile(u"../img/24x24/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.settings.setIcon(icon)

        self.leftmenuAnimation = QPropertyAnimation(self.ui.left_menu, b'minimumWidth')
        self.leftmenuAnimation.setStartValue(i)
        self.leftmenuAnimation.setEndValue(f)
        self.leftmenuAnimation.setDuration(400)
        self.leftmenuAnimation.setEasingCurve(QEasingCurve.InOutCubic)
        self.leftmenuAnimation.start()

    # a metodo que anima o tec zone
    def scrollAreaAnimat(self):
        tamanho_atual = self.ui.scrollArea.height()


        if tamanho_atual == 0:
            ai = 0
            af = 107
            i = 0
            f = 105
            icon = QIcon()
            icon.addFile(u"../img/24x24/cil-chevron-double-down-alt.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.double_up.setIcon(icon)
            self.ui.double_up.setIconSize(QSize(50, 40))

        else:
            i = 105
            f = 0
            ai = 107
            af = 0
            icon = QIcon()
            icon.addFile(u"../img/24x24/cil-chevron-double-up-alt.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.double_up.setIcon(icon)
            self.ui.double_up.setIconSize(QSize(25, 25))

        self.scrollAreaAnimaton = QPropertyAnimation(self.ui.scrollArea, b'minimumHeight')
        self.scrollAreaAnimaton.setStartValue(i)
        self.scrollAreaAnimaton.setEndValue(f)
        self.scrollAreaAnimaton.setDuration(400)
        self.scrollAreaAnimaton.setEasingCurve(QEasingCurve.InOutCirc)
        self.scrollAreaAnimaton.start()

        self.scrollframeAreaAnimaton = QPropertyAnimation(self.ui.frame_MarcaTech, b'minimumHeight')
        self.scrollframeAreaAnimaton.setStartValue(ai)
        self.scrollframeAreaAnimaton.setEndValue(af)
        self.scrollframeAreaAnimaton.setDuration(400)
        self.scrollframeAreaAnimaton.setEasingCurve(QEasingCurve.InOutCirc)
        self.scrollframeAreaAnimaton.start()

    # e o metodo responsavelo elas funcoes dos clicke
    def areaClick(self):
        name_btn = self.sender().objectName()

        if name_btn == 'web_btn' or name_btn == 'web_btn_2':
            self.simpficaLond(self.ui.page_web, 0)
        elif name_btn == 'help_btn':
            self.simpficaLond(self.ui.page_Extras, 0)
        elif name_btn == 'GoogleFinance_btl':
            self.simpficaLond(self.ui.page_Extras, 0, "https://www.google.com/finance/?hl=pt")
        elif name_btn == 'YahooFinance_btn':
            self.simpficaLond(self.ui.page_Extras, 0, "https://finance.yahoo.com/")
        elif name_btn == 'Investing_btn':
            self.simpficaLond(self.ui.page_Extras, 0, """https://www.investing.com/""")
        elif name_btn == 'BLHL_btn':
            self.simpficaLond(self.ui.page_Extras, 0, "https://www.nutsaboutmoney.com/investing/hargreaves-lansdown-alternatives")
        elif name_btn == 'Infomaney_btn':
            self.simpficaLond(self.ui.page_Extras, 0, "https://www.infomoney.com.br/")
        elif name_btn == 'Dinherama_btn':
            self.simpficaLond(self.ui.page_Extras, 0, "https://dinheirama.com/")
        elif name_btn == 'CMEgroup_btn':
            self.simpficaLond(self.ui.page_Extras, 0, "https://www.cmegroup.com/")
        elif name_btn == 'Economia_btn':
            self.simpficaLond(self.ui.page_Extras, 0, "https://www.dropbox.com/")
        elif name_btn == 'raspberry_btn':
            self.simpficaLond(self.ui.page_Extras, 0, "https://www.raspberrypi.org/")
        elif name_btn == 'help_btnF_2':
            self.simpficaLond(self.ui.page_Extras, 0, "https://www.thesource.ca/en-ca")##############################
        elif name_btn == 'perfil_btn':
            self.simpficaLond(self.ui.page_perfil)
            self.fontAnimation(0)
        elif name_btn == 'setting_btn':
            self.simpficaLond(self.ui.page_perfil, 0)
        elif name_btn == 'coins_btn':
            self.animationProgressB()
            self.simpficaLond(self.ui.page_CoinsQuote, 0)
        elif name_btn == 'setting_user_btn':
            self.simpficaLond(self.ui.page_perfil, 0)
        elif name_btn == 'editTest':
            self.simpficaLond(self.ui.page_edit, 1)
        elif name_btn == 'Home':
            self.simpficaLond(self.ui.page_Home, 0)
        elif name_btn == 'toolButton':

            # este codigo mida o icon do leitor
            if self.toobtn:
                icon15 = QIcon()
                icon15.addFile(u"../img/24x24/cil-volume-off.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.toolButton.setIcon(icon15)
                self.toobtn = False
                self.engine.stop()
            else:
                icon15 = QIcon()
                icon15.addFile(u"../img/24x24/cil-volume-high.png", QSize(), QIcon.Normal, QIcon.Off)
                self.ui.toolButton.setIcon(icon15)
                self.toobtn = True
                QTimer.singleShot(100, lambda: self.lerText(self.ui.plainTextEdit.toPlainText()))


    # metodo que anima o frame onde esta o regulador de font
    def fontAnimation(self, n):

        if n == 0:
            tamanho = self.ui.editTestFrame.height()
            if not tamanho == 0:
                self.frameFont = QPropertyAnimation(self.ui.editTestFrame, b'maximumHeight')
                self.frameFont.setStartValue(30)
                self.frameFont.setEndValue(0)
                self.frameFont.setDuration(400)
                self.frameFont.setEasingCurve(QEasingCurve.InOutCirc)
                self.frameFont.start()
        else:
            tamanho = self.ui.editTestFrame.height()

            if tamanho == 0:
                self.TimerFont.start()
                i = 0
                f = 30
            else:
                self.TimerFont.stop()
                i = 30
                f = 0

            self.frameFont = QPropertyAnimation(self.ui.editTestFrame, b'maximumHeight')
            self.frameFont.setStartValue(i)
            self.frameFont.setEndValue(f)
            self.frameFont.setDuration(400)
            self.frameFont.setEasingCurve(QEasingCurve.InOutCirc)
            self.frameFont.start()

    # metodo responsavel por aumentar e diminuir o tamanho da font
    def tamanhoFont(self):
        font = QFont()
        font.setPointSize(15+int(self.ui.horizontalSlider.value()))
        self.ui.plainTextEdit.setFont(font)

    #  lond e o metodo que carrega o segundo webBroeser navegagor
    def loand(self, inputURL):
        url = QUrl.fromUserInput(inputURL)

        if url.isValid():
            self.ui.webEngineView_2.load(url)

    #  lond e o metodo que carrega o primeiro navegagor
    def loandEx(self, inputURL):
        url = QUrl.fromUserInput(inputURL)
        if url.isValid():
            self.ui.webEngineView.load(url)
            self.timerHistorico.start()

    # este metodo simplifica o processamento web e a troca de pagina
    def simpficaLond(self, page=None, n=0, url=''):

        if url != "":
            self.loand(url)
            self.ui.stackedWidget.setCurrentWidget(page)
            self.fontAnimation(n)
        else:
            self.ui.stackedWidget.setCurrentWidget(page)
            self.fontAnimation(n)

    # metodo que abri , salva, e cria um arquivo de texto para as suas escritas
    def editArq(self):
        global PEGARaRQUIVO
        name_button = self.sender().objectName()

        if not PEGARaRQUIVO:
            if name_button == "save":
                if self.ui.save.text() == "New":
                    # criar u arquivo
                    arquivNew = QFileDialog.getOpenFileUrls(self, self.tr("Creat File"), self.tr("Text (*.txt)"))
                else:
                    saveArq = QFileDialog.getSaveFileName(self, self.tr("Save File"),"",self.tr("Text (*.txt)"))
                    # se nao ter um aberto , criar um
                    if not saveArq[0] == "":
                        with open(saveArq[0], 'w') as file:
                            file.write(self.ui.plainTextEdit.toPlainText())

            else:
                openArq = QFileDialog.getOpenFileNames(parent=self, caption=self.tr('Open File'),
                                                       filter=self.tr('Text fole (*.txt)'))

                if not openArq[0] == "":
                    with open(openArq[0][0], 'r') as file:
                        self.ui.plainTextEdit.setPlainText(file.read())

     # navegar na web
    def navegWeb(self):
        objname = self.sender().objectName()

        if objname == "arrow_left":
            self.ui.webEngineView.history().back()
        elif objname == "arrow_right":
            self.ui.webEngineView.history().forward()
        elif objname == "update":
            self.ui.webEngineView.reload()

    # este metodo e respnsavel por passar as urls na barra de link
    def pegarURLcriarHistorico(self):

        if len(self.listaURL) == 0:
            self.listaURL.append(self.ui.webEngineView.history().currentItem().url().url())
        else:
            if self.listaURL[-1] != self.ui.webEngineView.history().currentItem().url().url():
                self.listaURL.append(self.ui.webEngineView.history().currentItem().url().url())
                self.ui.LineUrl.setText(self.ui.webEngineView.history().currentItem().url().url())

    # este metodo le text 0
    def lerText(self, text):
        text = str(text)
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.engine.say(text)
        self.engine.runAndWait()

        icon15 = QIcon()
        icon15.addFile(u"../img/24x24/cil-volume-off.png", QSize(), QIcon.Normal, QIcon.Off)
        QTimer.singleShot(100,lambda:self.ui.toolButton.setIcon(icon15))
        self.toobtn = False

######## tentar um ouro reconhecedor de voz
    # este metodo e esponsavel por ppegar a voz
    def captacaoAudio(self):
        model = Model('model')
        self.rec = KaldiRecognizer(model, 14000)

        pyaud = pyaudio.PyAudio()
        self.stream = pyaud.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
        self.stream.start_stream()
        QTimer.singleShot(300, lambda: self.repAudioTimer.start())

    # repeticao do pegar audio
    def repAudio(self):
        global PEGARaUDIO
        data = self.stream.read(8000)
        if len(data) == 0 or PEGARaUDIO == 5:
            self.repAudioTimer.stop()
        if self.rec.AcceptWaveform(data):
            result = self.rec.Result()
            result = json.loads(result)
            if result is not None:
                text = result['text']
            PEGARaUDIO += 1

    def animationProgressB(self):

        self.progBrarAnimation1 = QPropertyAnimation(self.ui.progressBar_1, b'value')
        self.progBrarAnimation1.setStartValue(0)
        self.progBrarAnimation1.setDuration(600)
        self.progBrarAnimation1.setEndValue(100)
        self.progBrarAnimation1.setEasingCurve(QEasingCurve.InOutCirc)

        self.progBrarAnimation2 = QPropertyAnimation(self.ui.progressBar_2, b'value')
        self.progBrarAnimation2.setStartValue(0)
        self.progBrarAnimation2.setDuration(600)
        self.progBrarAnimation2.setEndValue(100)
        self.progBrarAnimation2.setEasingCurve(QEasingCurve.InOutCirc)

        self.progBrarAnimation3 = QPropertyAnimation(self.ui.progressBar_3, b'value')
        self.progBrarAnimation3.setStartValue(0)
        self.progBrarAnimation3.setDuration(600)
        self.progBrarAnimation3.setEndValue(100)
        self.progBrarAnimation3.setEasingCurve(QEasingCurve.InOutCirc)

        self.progBrarAnimation4 = QPropertyAnimation(self.ui.progressBar_4, b'value')
        self.progBrarAnimation4.setStartValue(0)
        self.progBrarAnimation4.setDuration(600)
        self.progBrarAnimation4.setEndValue(100)
        self.progBrarAnimation4.setEasingCurve(QEasingCurve.InOutCirc)

        self.progBrarAnimation5 = QPropertyAnimation(self.ui.progressBar_5, b'value')
        self.progBrarAnimation5.setStartValue(0)
        self.progBrarAnimation5.setDuration(600)
        self.progBrarAnimation5.setEndValue(100)
        self.progBrarAnimation5.setEasingCurve(QEasingCurve.InOutCirc)

        self.progBrarAnimation6 = QPropertyAnimation(self.ui.progressBar_6, b'value')
        self.progBrarAnimation6.setStartValue(0)
        self.progBrarAnimation6.setDuration(600)
        self.progBrarAnimation6.setEndValue(100)
        self.progBrarAnimation6.setEasingCurve(QEasingCurve.InOutCirc)

        self.progBrarAnimation7 = QPropertyAnimation(self.ui.progressBar_7, b'value')
        self.progBrarAnimation7.setStartValue(0)
        self.progBrarAnimation7.setDuration(600)
        self.progBrarAnimation7.setEndValue(100)
        self.progBrarAnimation7.setEasingCurve(QEasingCurve.InOutCirc)

        self.progBrarAnimation8 = QPropertyAnimation(self.ui.progressBar_8, b'value')
        self.progBrarAnimation8.setStartValue(0)
        self.progBrarAnimation8.setDuration(600)
        self.progBrarAnimation8.setEndValue(100)
        self.progBrarAnimation8.setEasingCurve(QEasingCurve.InOutCirc)

        self.progBrarAnimation9 = QPropertyAnimation(self.ui.progressBar_9, b'value')
        self.progBrarAnimation9.setStartValue(0)
        self.progBrarAnimation9.setDuration(600)
        self.progBrarAnimation9.setEndValue(100)
        self.progBrarAnimation9.setEasingCurve(QEasingCurve.InOutCirc)

        self.progBrarAnimation10 = QPropertyAnimation(self.ui.progressBar_10, b'value')
        self.progBrarAnimation10.setStartValue(0)
        self.progBrarAnimation10.setDuration(600)
        self.progBrarAnimation10.setEndValue(100)
        self.progBrarAnimation10.setEasingCurve(QEasingCurve.InOutCirc)

        self.group_pb_animation = QParallelAnimationGroup()
        self.group_pb_animation.addAnimation(self.progBrarAnimation1)
        self.group_pb_animation.addAnimation(self.progBrarAnimation2)
        self.group_pb_animation.addAnimation(self.progBrarAnimation3)
        self.group_pb_animation.addAnimation(self.progBrarAnimation4)
        self.group_pb_animation.addAnimation(self.progBrarAnimation5)
        self.group_pb_animation.addAnimation(self.progBrarAnimation6)
        self.group_pb_animation.addAnimation(self.progBrarAnimation7)
        self.group_pb_animation.addAnimation(self.progBrarAnimation8)
        self.group_pb_animation.addAnimation(self.progBrarAnimation9)
        self.group_pb_animation.addAnimation(self.progBrarAnimation10)
        self.group_pb_animation.start()

####### OS METODOS A BAIXO SERAM METODOS DE QUE CONFIGURARAM AS CONVERCOES DE MOEDA #####
    # crie um metod que ira receber o valores de apis

    def bitcoin_LEditTextChanged(self, s):

        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS * 8482783.07:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.bitcoin_aoa_LEdit.setText(conversao)
        except:
                pass

    def bitcoin_aoa_LEditTextChanged(self, s):

        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS/8482783.07:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.bitcoin_LEdit.setText(conversao)
        except:
                pass

    def DK_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS * 138973:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.DK_aoa_LEdit.setText(conversao)
        except:
                pass

    def DK_aoa_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS / 138973:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.DK_LEdit.setText(conversao)
        except:

                pass

    def DB_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS * 1389.73:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.DB_aoa_LEdit.setText(conversao)
        except:
                pass

    def DB_aoa_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS / 1389.73:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.DB_LEdit.setText(conversao)
        except:
            pass

    def RO_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS * 1113.22:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.RO_aoa_LEdit.setText(conversao)
        except:
            pass

    def RO_aoa_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS / 1113.22:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.RO_LEdit.setText(conversao)
        except:
            pass

    def DJ_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS * 604.49:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.DJ_aoa_LEdit.setText(conversao)
        except:
            pass

    def DJ_aoa_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS / 604.49:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.DJ_LEdit.setText(conversao)
        except:
            pass

    def DC_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS * 514.50:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.DC_aoa_LEdit.setText(conversao)
        except:
            pass

    def DC_aoa_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS / 514.50:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.DC_LEdit.setText(conversao)
        except:
            pass

    def LE_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS * 493.30:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.LE_aoa_LEdit.setText(conversao)
        except:
            pass

    def LE_aoa_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS / 493.30:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.LE_LEdit.setText(conversao)
        except:
            pass

    def E_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS * 426.57:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.E_aoa_LEdit.setText(conversao)
        except:
            pass

    def E_aoa_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS /426.57:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.E_LEdit.setText(conversao)
        except:
            pass

    def FS_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS * 436.79:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.FS_aoa_LEdit.setText(conversao)
        except:
            pass

    def FS_aoa_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS / 436.79:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.FS_LEdit.setText(conversao)
        except:
            pass

    def DNA_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS * 428.58:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.DNA_aoa_LEdit.setText(conversao)
        except:
            pass

    def DNA_aoa_LEditTextChanged(self, s):
        try:
            s = self.tirarPontoValor(s)
            intS = float(s.replace(',', '.'))
            conversao = str(f"{intS / 428.58:.2f}")
            conversao = self.porPontoValor(conversao)
            self.ui.DNA_LEdit.setText(conversao)
        except:
            pass

    def porPontoValor(self, conversao):

        conversaoAx = ''
        conversao = conversao.replace('.', ',')
        conversao = list(conversao)
        if len(conversao) >= 7 and len(conversao) <= 9:
            conversao.insert(-6, ".")
        elif len(conversao) >= 10 and len(conversao) <= 12:
            conversao.insert(-6, ".")
            conversao.insert(-10, ".")
        elif len(conversao) >= 13 and len(conversao) <= 15:
            conversao.insert(-6, ".")
            conversao.insert(-10, ".")
            conversao.insert(-14, ".")
        elif len(conversao) >= 16 and len(conversao) <= 18:
            conversao.insert(-6, ".")
            conversao.insert(-10, ".")
            conversao.insert(-14, ".")
            conversao.insert(-18, ".")
        elif len(conversao) >= 19 and len(conversao) <= 21:
            conversao.insert(-6, ".")
            conversao.insert(-10, ".")
            conversao.insert(-14, ".")
            conversao.insert(-18, ".")
            conversao.insert(-22, ".")
        elif len(conversao) >= 22 and len(conversao) <= 24:
            conversao.insert(-6, ".")
            conversao.insert(-10, ".")
            conversao.insert(-14, ".")
            conversao.insert(-18, ".")
            conversao.insert(-22, ".")
            conversao.insert(-26, ".")
        elif len(conversao) >= 25 and len(conversao) <= 27:
            conversao.insert(-6, ".")
            conversao.insert(-10, ".")
            conversao.insert(-14, ".")
            conversao.insert(-18, ".")
            conversao.insert(-22, ".")
            conversao.insert(-26, ".")
            conversao.insert(-30, ".")
        elif len(conversao) >= 27 and len(conversao) <= 30:
            conversao.insert(-6, ".")
            conversao.insert(-10, ".")
            conversao.insert(-14, ".")
            conversao.insert(-18, ".")
            conversao.insert(-22, ".")
            conversao.insert(-26, ".")
            conversao.insert(-30, ".")
            conversao.insert(-34, ".")
        elif len(conversao) >= 31 and len(conversao) <= 33:
            conversao.insert(-6, ".")
            conversao.insert(-10, ".")
            conversao.insert(-14, ".")
            conversao.insert(-18, ".")
            conversao.insert(-22, ".")
            conversao.insert(-26, ".")
            conversao.insert(-30, ".")
            conversao.insert(-34, ".")
            conversao.insert(-38, ".")
        elif len(conversao) >= 34 and len(conversao) <= 36:
            conversao.insert(-6, ".")
            conversao.insert(-10, ".")
            conversao.insert(-14, ".")
            conversao.insert(-18, ".")
            conversao.insert(-22, ".")
            conversao.insert(-26, ".")
            conversao.insert(-30, ".")
            conversao.insert(-34, ".")
            conversao.insert(-38, ".")
            conversao.insert(-42, ".")
        elif len(conversao) >= 37 and len(conversao) <= 40:
            conversao.insert(-6, ".")
            conversao.insert(-10, ".")
            conversao.insert(-14, ".")
            conversao.insert(-18, ".")
            conversao.insert(-22, ".")
            conversao.insert(-26, ".")
            conversao.insert(-30, ".")
            conversao.insert(-34, ".")
            conversao.insert(-38, ".")
            conversao.insert(-42, ".")
            conversao.insert(-46, ".")

        for c in conversao:
            conversaoAx += c

        return conversaoAx

    def tirarPontoValor(self, valor):

        saida = ''
        anlz = False
        valor = list(valor)
        pre = 0
        for n, c in enumerate(valor):

            if n == 0:
                if c == ".":
                    saida = "ERROR"
                else:
                    saida += c
            else:

                if c == ".":
                    pre += 4

                if c == ",":
                    pre += 3

                if valor.count("."):
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

        return saida


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashCreen()
    sys.exit(app.exec())

##            for itens in self.ui.webEngineView.page().history().items():
##                print(itens.url())