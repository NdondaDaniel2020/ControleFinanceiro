from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCharts import QChart, QChartView, QBarCategoryAxis, QBarSeries, QBarSet, QValueAxis

from packeg.custom_grips import CustomGrip
from packeg.circular_progress import CircularProgress
from packeg.Criptografia import criptografar
from packeg.chart import Chart
from packeg.database import database
from ui_SystemSC import Ui_SplashCreen
from ui_SystemMW import Ui_MainWindowMW
from ui_Movimentação import Movimentacao
from ui_barraCategoria import BarraCategoria
from ui_barraMovimentação import BarraMovimentacao
from ui_HistoricoEntradaSaida import HistoricoEntradaSaida

from time import sleep
from datetime import date
import sys
import cv2

# variavel global
UsuiarioGlobal = ''
CONT = 0
HAARCASCADES = '../haarcascades/haarcascade_frontalface_default.xml'
CLASSIFICADORLBPH = '../classificador/classificadorLBPH.0.1.yml'
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
            self.Redimencionar = True  # ele vai dizer se no reconhecimento qunado o resultado sair se vai
            # redimencionar a tela ou não
        except:
            quit()
            pass

        sleep(2)  # paramos 1 segundo para nao atrapalhar na performace da Ui
        # inicio da interfaceGrafica
        QMainWindow.__init__(self)
        self.sc = Ui_SplashCreen()
        self.sc.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)  # este comando é responsavel por eliminar a barra de titulo
        self.setAttribute(Qt.WA_TranslucentBackground)  # este comando é responsavel por tornar o fundo transparente

        # chamando a class que controla a base de dados

        self.database = database("ControleFinanceiro.db")
        self.senhaUltimoUser = ''
        self.nomeDoUsuario = ''  ## ele será Usado para o main window
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

        # atributos de obj
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
        QTimer.singleShot(5000, lambda: self.AnimatioOpacity())
        QTimer.singleShot(5500, lambda: self.OpenResize())  # funcão com documentação. está com controlador de tempo
        # esta é uma das formas de corrigir o erro de aimagem mudar de posição só
        # QTimer.singleShot(2500, lambda: self.opacityLabel())
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
        QTimer.singleShot(500, lambda: print())
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
                self.inserirUltimoUserInBD(str(id + 1))
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
                    self.database.disconnect_database()

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
                imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (22, 22, 22), 1)
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
                    if not self.sc.CentralFrame.height() == 250 and self.Redimencionar:  #########################
                        QTimer.singleShot(30, lambda: self.OpenResize())  ###
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

                cv2.putText(imagem, name, (x, y + (a + 30)), self.Fonte, 1, fontColor)

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
        self.database.disconnect_database()

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
        self.database.disconnect_database()
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
        self.database.disconnect_database()

    # este metodo e responsavel pro contar o numero de registro (tuplas na base de dados)
    def contarRegistrosTabelaUser(self):

        self.database.connect_database()
        registro = self.database.executarFetchall("SELECT * FROM Usuario")
        self.database.disconnect_database()

        return str(len(registro) + 1)

    # este metodo e responvael por saber a posição no ultimo usuario
    def identificarUltimoUsuario(self, nome):
        self.database.connect_database()
        listDados = self.database.executarFetchall(f"SELECT * FROM Usuario")
        self.database.disconnect_database()

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
        global NOMEUSER
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindowMW()
        self.ui.setupUi(self)

        self.move(126, 35)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setMinimumSize(1095, 695)
        self.setGeometry(126, 35, 1095, 695)
        self.toobtn = True

        self.historicoEntradaCont = 0
        self.hitoricoSaidaCont = 0

        self.database = database("ControleFinanceiro")
        self.dataAtual = self.pegarData()
        self.analizarUltimasTranzacoes()
        self.novaMovimentacao = Movimentacao()
        self.analizeEntradaSaidaValores()
        self.adicionaCategoriaPlanoContasBusca()
        self.adicionarCategoriaAutomatic()
        self.informacoesUser()
        self.eventoConnect()

        self.ui.minimisar.clicked.connect(lambda: self.showMinimized())
        self.ui.NormalMax.clicked.connect(lambda: self.MaxMin())
        self.ui.fechar.clicked.connect(lambda: quit())

        self.ui.settings.clicked.connect(self.leftmenu)
        self.ui.movimentacao_btn3.clicked.connect(self.areaClick)
        self.ui.fluxodecaixa.clicked.connect(self.areaClick)
        self.ui.perfil_btn.clicked.connect(self.areaClick)
        self.ui.movimentacao_btn.clicked.connect(self.areaClick)
        self.ui.movimentacao_btn2.clicked.connect(self.areaClick)
        self.ui.Home.clicked.connect(self.areaClick)
        self.ui.frame_user_list_btn.clicked.connect(self.areaClick)
        self.ui.categoria_btn.clicked.connect(self.areaClick)

        self.novaMovimentacao.mov.movimentar.clicked.connect(self.ValorNomvaMovimentacao)
        self.ui.novaMovimentacao.clicked.connect(self.showMovimentacao)
        self.ui.buscar.clicked.connect(self.buscar)
        self.ui.planoContasBusca.currentTextChanged.connect(self.selectCategoriaBuscador)
        self.buscarCategoria = 0
        self.ui.planoContasBuscaFluxo.currentTextChanged.connect(self.PegarValorTotCategoria)

        self.ui.salvarAlteracao.clicked.connect(self.alterarNomeSenha)
        self.ui.salvarAlteracao_2.clicked.connect(self.AdicionarCategoriaNaUI)
        self.ui.editFotho.clicked.connect(self.editArq)
        self.ui.exit.clicked.connect(self.exit)

        self.analizeValorConst = 0
        self.analizeValorTime = QTimer()
        self.analizeValorTime.timeout.connect(lambda: self.analizeValor(len(self.novaMovimentacao.mov.valor.text())))

        self.analizeNomeConst = 0
        self.analizeNomeTime = QTimer()
        self.analizeNomeTime.timeout.connect(lambda: self.analizeNome(len(self.novaMovimentacao.mov.nome.text())))

        self.analizeTranzecaoConst = 0
        self.analizeTranzecaoTime = QTimer()
        self.analizeTranzecaoTime.timeout.connect(
            lambda: self.analizeTranzacao(len(self.novaMovimentacao.movimentarNome)))



        self.left = CustomGrip(self, Qt.LeftEdge, True)
        self.right = CustomGrip(self, Qt.RightEdge, True)
        self.top = CustomGrip(self, Qt.TopEdge, True)
        self.bottom = CustomGrip(self, Qt.BottomEdge, True)

        self.adicionandoGraficoDinamico()
        self.graficodeDados()
        self.graficoCategoria()

        self.show()  # mostrar janela

    # pega a posicao global
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        self.dragPosScrollHome = self.ui.scrollArea_Home.horizontalScrollBar().value()
        self.dragPosScroll2 = self.ui.scrollArea_6.horizontalScrollBar().value()

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

        def mousePressEventUserPerfil(event):
            if event.buttons() == Qt.LeftButton:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_perfil)
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_perfilUsuario)

        self.ui.frame_user_perfil.mousePressEvent = mousePressEventUserPerfil

        def mousePressEventCategoriaBtn(event):
            if event.buttons() == Qt.LeftButton:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_perfil)
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_Categoria)

        self.ui.frame_CategoriaBtn.mousePressEvent = mousePressEventCategoriaBtn

        def mousePressEvent(event):
            if event.buttons() == Qt.LeftButton:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_ControleFinanceiro)

        self.ui.frame_movimentacao.mousePressEvent = mousePressEvent

        #### evento responsavel por mover o scroll pelos frmames ####

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

        self.ui.frame_opening_history.mouseMoveEvent = moveScroll2
        self.ui.frame_opening_history.mouseReleaseEvent = releasecroll2

        self.ui.frame_CategoriaBtn.mouseMoveEvent = moveScroll2
        self.ui.frame_CategoriaBtn.mouseReleaseEvent = releasecroll2

        self.ui.frame_user_perfil.mouseMoveEvent = moveScroll2
        self.ui.frame_user_perfil.mouseReleaseEvent = releasecroll2

        self.ui.frame_password_faceId.mouseMoveEvent = moveScroll2
        self.ui.frame_password_faceId.mouseReleaseEvent = releasecroll2

        ####################################################################################


        #### evento responsavel por mover o scroll pelos frmames ####

        self.scrollPrimary = 0
        self.cursorPrimary = 0
        self.logCursor = True
        self.dragPosScrollHome = self.ui.scrollArea_Home.horizontalScrollBar().value()

        def moveScrollAreaHome(event: QMouseEvent):
            if event.buttons() == Qt.LeftButton:
                if self.cursorPrimary == 0 and self.logCursor == True:
                    self.cursorPrimary = self.cursor().pos().x()
                    self.logCursor = False
                valor = (self.cursor().pos().x() - (self.cursorPrimary))
                self.ui.scrollArea_Home.horizontalScrollBar().setValue(self.dragPosScrollHome - valor)
                event.accept()

        def releaseScrollAreaHome(event: QMouseEvent):
            if event.type() == QEvent.MouseButtonRelease:
                self.cursorPrimary = 0
                self.logCursor = True
                self.scrollPrimary = self.ui.scrollArea_Home.horizontalScrollBar().value()
                event.accept()

        self.ui.frame_movimentacao.mouseMoveEvent = moveScrollAreaHome
        self.ui.frame_movimentacao.mouseReleaseEvent = releaseScrollAreaHome

        self.ui.frame_207.mouseMoveEvent = moveScrollAreaHome
        self.ui.frame_207.mouseReleaseEvent = releaseScrollAreaHome

        self.ui.frame_user_list_3.mouseMoveEvent = moveScrollAreaHome
        self.ui.frame_user_list_3.mouseReleaseEvent = releaseScrollAreaHome

        self.ui.frame_210.mouseMoveEvent = moveScrollAreaHome
        self.ui.frame_210.mouseReleaseEvent = releaseScrollAreaHome


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
        iqr = 0
        fqr = 0
        if tamnho_atual == 8:
            i = 8
            f = 200
            iqr = 0
            fqr = 192
            icon = QIcon()
            icon.addFile(u"../img/24x24/cil-x-f.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.settings.setIcon(icon)
        else:
            i = 200
            f = 8
            iqr = 192
            fqr = 0
            icon = QIcon()
            icon.addFile(u"../img/24x24/cil-settings.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.settings.setIcon(icon)

        self.leftmenuAnimation = QPropertyAnimation(self.ui.left_menu, b'minimumWidth')
        self.leftmenuAnimation.setStartValue(i)
        self.leftmenuAnimation.setEndValue(f)
        self.leftmenuAnimation.setDuration(600)
        self.leftmenuAnimation.setEasingCurve(QEasingCurve.InOutCubic)

        self.qranimation = QPropertyAnimation(self.ui.frame_zoneQR, b'minimumWidth')
        self.qranimation.setStartValue(iqr)
        self.qranimation.setEndValue(fqr)
        self.qranimation.setDuration(600)
        self.qranimation.setEasingCurve(QEasingCurve.InOutCubic)

        self.dataAnimation = QPropertyAnimation(self.ui.data, b'minimumWidth')
        self.dataAnimation.setStartValue(iqr)
        self.dataAnimation.setEndValue(fqr)
        self.dataAnimation.setDuration(600)
        self.dataAnimation.setEasingCurve(QEasingCurve.InOutCubic)

        self.criadoAnimation = QPropertyAnimation(self.ui.criadoPor, b'minimumWidth')
        self.criadoAnimation.setStartValue(iqr)
        self.criadoAnimation.setEndValue(fqr)
        self.criadoAnimation.setDuration(600)
        self.criadoAnimation.setEasingCurve(QEasingCurve.InOutCubic)

        self.grounpLeft = QParallelAnimationGroup()
        self.grounpLeft.addAnimation(self.leftmenuAnimation)
        self.grounpLeft.addAnimation(self.qranimation)
        self.grounpLeft.addAnimation(self.dataAnimation)
        self.grounpLeft.addAnimation(self.criadoAnimation)
        self.grounpLeft.start()

    # e o metodo responsavelo elas funcoes dos clicke
    def areaClick(self):
        name_btn = self.sender().objectName()

        if name_btn == 'movimentacao_btn' or name_btn == 'movimentacao_btn2' or name_btn == 'movimentacao_btn3':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_ControleFinanceiro)
        elif name_btn == 'perfil_btn' or name_btn == 'frame_user_list_btn':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_perfil)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_perfilUsuario)
        elif name_btn == 'categoria_btn':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_perfil)
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_Categoria)
        elif name_btn == 'fluxodecaixa':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_FluxodeCaixa)
        elif name_btn == 'Home':
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_Home)

    #  lond e o metodo que carrega o segundo webBroeser navegagor
    def loand(self, inputURL):
        url = QUrl.fromUserInput(inputURL)

        if url.isValid():
            self.ui.webEngineView_2.load(url)

    # este metodo e responsavel por add  o grafico na interface na HOME page
    def adicionandoGraficoDinamico(self):
        chart = Chart()
        # chart.setTitle("Dados de todas entradas saidas")
        chart.legend().hide()
        chart.setAnimationOptions(QChart.AllAnimations)
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.ui.verticalLayout_graficoMain.addWidget(chart_view)

    # grafico FluxoDe caixa
    def graficodeDados(self):
        self.database.connect_database()
        valorMaximo = self.database.executarFetchone("select max(valor) FROM MovimentacaoFinanceira")
        listaDados = self.database.executarFetchall("""select valor, tranzacao from  MovimentacaoFinanceira;""")

        self.database.disconnect_database()

        entrada = []
        saida = []

        for dados in listaDados:

            if dados[1] == 'entrada':
                entrada.append(dados[0])
            else:
                saida.append(dados[0])

        self.set_0 = QBarSet("Entrada")
        self.set = QBarSet("Sida")

        self.set_0.append(entrada)
        self.set.append(saida)

        self.set_0.setColor(QColor(85, 255, 127))
        self.set.setColor(QColor(255, 0, 0))

        self.series = QBarSeries()
        self.series.append(self.set_0)
        self.series.append(self.set)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Simple barchart example")
        self.chart.setAnimationOptions(QChart.SeriesAnimations)

        self.categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categories)
        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setRange(0, valorMaximo[0])
        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.ui.verticalLayout_GraficoDados.addWidget(self._chart_view)

    # este metodo e responsavel por por a categoia no planoContasBusca
    def adicionaCategoriaPlanoContasBusca(self):
        self.ui.planoContasBusca.setPlaceholderText("Planos de contas")
        self.database = database("ControleFinanceiro")
        self.database.connect_database()
        dados = self.database.executarFetchall("SELECT * FROM Categoria")
        self.database.disconnect_database()

        self.ui.planoContasBusca.addItem("")
        self.ui.planoContasBusca.setItemText(0, QCoreApplication.translate("Form", " ", None))
        self.ui.planoContasBuscaFluxo.addItem("")
        self.ui.planoContasBuscaFluxo.setItemText(0, QCoreApplication.translate("Form", " ", None))

        for dado in dados:
            self.ui.planoContasBusca.addItem("")
            self.ui.planoContasBusca.setItemText(dado[0], QCoreApplication.translate("Form", dado[1], None))
            self.ui.planoContasBuscaFluxo.addItem("")
            self.ui.planoContasBuscaFluxo.setItemText(dado[0], QCoreApplication.translate("Form", dado[1], None))

    # este metodo é reponsavelo pela movimentação
    def showMovimentacao(self):
        self.novaMovimentacao.show()

    # est6e metodo e responsavel por pegar data
    def pegarData(self):

        dataAgoara = date.today()

        return str(dataAgoara)

    # este e um tetodo tesponsavel por contar as Movimentações financeiras
    def contarMovimentacao(self):
        self.database.connect_database()
        dados = self.database.executarFetchall("SELECT * FROM MovimentacaoFinanceira")
        self.database.disconnect_database()

        conta = len(dados)
        return conta + 1

    # este metodo e responsavel por enviar do
    # dados em forma de tabelas na interface na zona de movimentação finaceira
    def enviarDadosEmMovimentacaoFinaceira(self, codigo=0, titulo='', valor='', tranzacao='', categoria=''):
        self.barraMovimentacao = BarraMovimentacao()
        self.barraMovimentacao2 = BarraMovimentacao()
        if codigo == 0:
            codigo = self.contarMovimentacao()

        if titulo != "" and valor != "" and tranzacao != "" and categoria != "":
            valor2 = self.porPontoValor(valor)
            self.barraMovimentacao.setValues(codigo, self.dataAtual, categoria, titulo, valor2, tranzacao)
            self.ui.verticalLayout_ScrolNovaTranzacao.insertWidget(codigo - 1,
                                                                   self.barraMovimentacao.bm.pequenoHistoricoEntrada)
            self.ui.verticalLayout_fluxo.insertWidget(codigo - 1, self.barraMovimentacao2.bm.pequenoHistoricoEntrada)
            self.novaMovimentacao.close()
            self.historicoMovimentacao(titulo, valor, tranzacao)
            ncategoria = self.encontraIndeceCategoria(categoria)
            self.database.connect_database()
            self.database.executarComand(f"""
            INSERT INTO MovimentacaoFinanceira (data, categoria, nome, valor, tranzacao)
            values ('{self.dataAtual}', '{ncategoria}', '{titulo}', '{valor}', '{tranzacao}')""")
            self.database.disconnect_database()
            self.analizeEntradaSaidaValores()
            self.novaMovimentacao.mov.nome.setText("")
            self.novaMovimentacao.mov.valor.setText("")

    # este metodo mostra ajanela de movimentação
    def ValorNomvaMovimentacao(self):
        nome = self.novaMovimentacao.mov.nome.text()
        valor = self.novaMovimentacao.mov.valor.text()
        tranzacao = self.novaMovimentacao.movimentarNome
        categoria = self.novaMovimentacao.categoria

        passNome = False
        passValor = False
        passTarnzacao = False
        passCategoria = False

        if nome == "" or nome == " ":
            self.novaMovimentacao.mov.nome.setStyleSheet("""background-color: rgb(170, 85, 255);
                                                                                         border-radius:5px;
                                                                                         color: rgb(255, 0, 0);
                                                                                         padding-left:5px;""")
            self.analizeNomeConst = len(str(valor))
            self.analizeNomeTime.start()
        else:
            passNome = True

        if valor.isnumeric():
            passValor = True
        else:
            self.novaMovimentacao.mov.valor.setStyleSheet("""background-color: rgb(170, 85, 255);
                                                             border-radius:5px;
                                                             color: rgb(255, 0, 0);
                                                             padding-left:5px;""")
            self.analizeValorConst = len(str(valor))
            self.analizeValorTime.start()

        if tranzacao == "":
            self.novaMovimentacao.alerta(True)
        else:
            passTarnzacao = True

        if categoria == "":
            self.novaMovimentacao.alertaCategoria()
        else:
            passCategoria = True

        if passCategoria == passTarnzacao == passValor == passNome:
            self.enviarDadosEmMovimentacaoFinaceira(0, nome, valor, tranzacao, categoria)

    ##### estes tres metodos abaixo são verificadores  do tamanho de STR ####
    def analizeValor(self, n):
        if n != self.analizeValorConst:
            self.novaMovimentacao.mov.valor.setStyleSheet("""
            background-color: rgb(170, 85, 255);
            border-radius: 5px;
            color: rgb(255, 255, 255);
            padding-left: 5px;""")
            self.analizeValorTime.stop()

    def analizeNome(self, n):
        if n != self.analizeNomeConst:
            self.novaMovimentacao.mov.nome.setStyleSheet("""
              background-color: rgb(170, 85, 255);
              border-radius: 5px;
              color: rgb(255, 255, 255);
              padding-left: 5px;""")
            self.analizeNomeTime.stop()

    def analizeTranzacao(self, n):
        if n != self.analizeTranzecaoConst:
            self.novaMovimentacao.mov.entrada.setStyleSheet("""
              QPushButton{
background-color: rgb(170, 85, 255);
border-radius: 5px;
color: rgb(85, 255, 127);
}

QPushButton:hover{
background-color: rgb(165, 82, 247);
border-radius: 5px;
}

QPushButton:pressed{
background-color: rgb(170, 85, 255);
border-radius: 5px;
}""")
            self.novaMovimentacao.mov.saida.setStyleSheet("""
                         QPushButton{
background-color: rgb(170, 85, 255);
border-radius: 5px;
	color: rgb(255, 0, 0);
}

QPushButton:hover{
background-color: rgb(165, 82, 247);
border-radius: 5px;
}

QPushButton:pressed{
background-color: rgb(170, 85, 255);
border-radius: 5px;
};""")
            self.analizeNomeTime.stop()

    # este metodo analiza todas as tranzções e insere os dados  nas tabelas antes de mostrar a janela
    def analizarUltimasTranzacoes(self):
        self.database.connect_database()
        dadosMovimentacoesFinceiras = self.database.executarFetchall("SELECT * FROM MovimentacaoFinanceira")
        self.database.disconnect_database()

        for n, dados in enumerate(dadosMovimentacoesFinceiras):
            self.barraMovimentacao = BarraMovimentacao()
            self.barraMovimentacao2 = BarraMovimentacao()
            categoria = self.encontraIndeceCategoria(dados[2])
            valor = self.porPontoValor(dados[4])
            self.barraMovimentacao.setValues(dados[0], dados[1], categoria, dados[3], str(valor) + ",00", dados[5])
            self.barraMovimentacao2.setValues(dados[0], dados[1], categoria, dados[3], str(valor) + ",00", dados[5])
            self.ui.verticalLayout_ScrolNovaTranzacao.insertWidget(n, self.barraMovimentacao.bm.pequenoHistoricoEntrada)
            self.ui.verticalLayout_fluxo.insertWidget(n, self.barraMovimentacao2.bm.pequenoHistoricoEntrada)
            self.historicoMovimentacao(dados[3], dados[4], dados[5])

    # este metodo soma dodas as entradas e saidas para por no
    # quandro de total de entradas e saida nas movimentações e Home
    def analizeEntradaSaidaValores(self):
        self.database.connect_database()
        totalEntradas = self.database.executarFetchall("""
        SELECT SUM(valor) FROM MovimentacaoFinanceira where tranzacao=='entrada';""")
        totalSaidas = self.database.executarFetchall("""
        SELECT SUM(valor) FROM MovimentacaoFinanceira where tranzacao=='saida';
        """)
        self.database.disconnect_database()

        valorTotal = int(totalEntradas[0][0]) - int(totalSaidas[0][0])

        totalPercentual = int(totalEntradas[0][0]) + int(totalSaidas[0][0])

        percentualEntrada = round((int(totalEntradas[0][0]) * 100) / totalPercentual, 2)
        percentualEntrada = str(percentualEntrada) + "%"

        percentualSaida = round((int(totalSaidas[0][0]) * 100) / totalPercentual, 2)
        percentualSaida = str(percentualSaida) + "%"

        totalEntradas = self.porPontoValor(totalEntradas[0][0])
        totalSaidas = self.porPontoValor(totalSaidas[0][0])
        valorTotal = self.porPontoValor(valorTotal)

        totalEntradas = "Kz " + str(totalEntradas) + ",00"
        totalSaidas = "Kz " + str(totalSaidas) + ",00"
        valorTotal = "Kz " + str(valorTotal) + ",00"

        self.ui.percentualEntrada.setText(percentualEntrada)
        self.ui.percentualSaida.setText(percentualSaida)

        self.ui.totalEntrada.setText(totalEntradas)
        self.ui.totalSaida.setText(totalSaidas)
        self.ui.valorTotal.setText(valorTotal)

        self.ui.homeTotalEntrada.setText(totalEntradas)
        self.ui.homeTotalSaidas.setText(totalSaidas)
        self.ui.homeValorTotal.setText(valorTotal)

        self.ui.totalEntradaFluxo.setText(totalEntradas)
        self.ui.totalSaidaFluxo.setText(totalSaidas)
        self.ui.valorTotalFluxo.setText(valorTotal)

    # este metodo pega o indece e pega a categoria correspondente ao indice
    def encontraIndeceCategoria(self, busca):
        self.database.connect_database()
        lista = self.database.executarFetchall("SELECT * FROM Categoria")
        self.database.disconnect_database()
        saida = ''
        if type(busca) == int:
            for itens in lista:
                if itens[0] == busca:
                    saida = itens[1]
        else:
            for itens in lista:
                if itens[1] == busca:
                    saida = itens[0]

        return saida

        # add o widget do historico de movimentação

    # este metodo põe ponto nos valores para ter uma facil leitura dos dados
    def porPontoValor(self, conversao):
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

    # este metodo e reponsavel por adicionar o historico de tranzação
    def historicoMovimentacao(self, nome, valor, tranzacao):
        historicoEntradaSaida = HistoricoEntradaSaida()

        valor = self.porPontoValor(valor)
        if tranzacao == "entrada":
            historicoEntradaSaida.setEntrada(nome, self.dataAtual, "Kz " + str(valor) + ",00")
            self.ui.verticalLayout_ZonaEntrada.insertWidget(self.historicoEntradaCont,
                                                            historicoEntradaSaida.hes.pequenoHistoricoEntrada)
            self.historicoEntradaCont += 1
        else:
            historicoEntradaSaida.setSaida(nome, self.dataAtual, "Kz " + str(valor) + ",00")
            self.ui.verticalLayout_zonaSaida.insertWidget(self.hitoricoSaidaCont,
                                                          historicoEntradaSaida.hes.pequenoHistoricoSaida)
            self.hitoricoSaidaCont += 1

    # estemetodo  seleciona a categoria e converte no seu indece
    def selectCategoriaBuscador(self, categoria):
        categoria = self.encontraIndeceCategoria(categoria)
        self.buscarCategoria = categoria

    # pegava o valor total por categoria
    def PegarValorTotCategoria(self, categoria):
        self.database.connect_database()
        listaDados = self.database.executarFetchall("""select categoria,nome, sum(valor), tranzacao from
          MovimentacaoFinanceira GROUP by categoria order by categoria""")
        self.database.disconnect_database()

        categoria = self.encontraIndeceCategoria(categoria)

        valor = 0
        for dados in listaDados:
            if dados[0] == categoria:
                valor = dados[2]

        self.ui.totalCategoria.setText("Kz " + str(valor) + ",00")

    # este metodo converte o modelo de data
    def converterModeloData(self, data):
        dia = data[0:2]
        mes = data[3:5]
        ano = data[6:10]
        data = ano + "-" + mes + "-" + dia
        return data

    # este metodo e responsavel por fazer a busca dos dados de movimenção
    def buscar(self):
        select = 'SELECT * FROM MovimentacaoFinanceira '

        if "" != self.buscarCategoria != 0:
            select += f"WHERE categoria = '{str(self.buscarCategoria)}'"

        if self.ui.dataMovimentacaofim.text() != '01/01/2010':
            if self.ui.dataMovimentacaoInicio.text() == self.ui.dataMovimentacaofim.text():
                if self.buscarCategoria == 0:
                    data = self.converterModeloData(self.ui.dataMovimentacaoInicio.text())
                    select += f" WHERE data = '{data}'"
                else:
                    data = self.converterModeloData(self.ui.dataMovimentacaoInicio.text())
                    select += f" AND data = '{data}'"
            else:
                if self.buscarCategoria == 0:
                    data1 = self.converterModeloData(self.ui.dataMovimentacaoInicio.text())
                    data2 = self.converterModeloData(self.ui.dataMovimentacaofim.text())
                    select += f" WHERE data BETWEEN '{data1}' AND '{data2}'"
                else:
                    data1 = self.converterModeloData(self.ui.dataMovimentacaoInicio.text())
                    data2 = self.converterModeloData(self.ui.dataMovimentacaofim.text())
                    select += f" AND data BETWEEN '{data1}' AND '{data2}'"

        if not self.ui.codigoBusca.text() == "":
            select = f"SELECT * from MovimentacaoFinanceira where id = '{self.ui.codigoBusca.text()}';"

        self.database.connect_database()
        dados = self.database.executarFetchall(select)
        self.database.disconnect_database()

        for objeto in self.ui.scrollAreaWidgetContents_3.findChildren(QFrame):
            objeto.close()

        for n, dado in enumerate(dados):
            self.barraMovimentacao = BarraMovimentacao()
            categoria = self.encontraIndeceCategoria(dado[2])
            valor = self.porPontoValor(dado[4])
            self.barraMovimentacao.setValues(dado[0], dado[1], categoria, dado[3], str(valor) + ",00", dado[5])
            self.ui.verticalLayout_ScrolNovaTranzacao.insertWidget(n, self.barraMovimentacao.bm.pequenoHistoricoEntrada)

    def alterarNomeSenha(self):
        nome = self.ui.mudaNome.text()
        senha = self.ui.mudaSenha.text()
        self.database.connect_database()
        id = self.database.executarFetchall("SELECT UltimoUsuario from UltimoUsuario;")
        id = id[-1][0]
        senha = criptografar(senha)
        descricao = self.database.executarFetchone(f"select descricao from Usuario where id = '{id}';")
        descricao = descricao[0]
        self.ui.descricao.setText(descricao)
        self.database.executarComand(f"UPDATE Usuario set nome = '{nome}' and password = '{senha}' where id = '{id}';")
        self.database.disconnect_database()

    # metodo que abri, salva, e cria um arquivo de texto para as suas escritas
    def editArq(self):

        openArq = QFileDialog.getOpenFileNames(parent=self, caption=self.tr('Guard'),
                                               filter=self.tr('img file (*.png *.jpeg *.jpg *.PNG *.JPG) '))

        url = str(openArq[0][0])
        icon21 = QIcon()
        icon21.addFile(url, QSize(), QIcon.Normal, QIcon.Off)
        self.ui.perfifEdit.setIcon(icon21)
        self.ui.perfifEdit.setIconSize(QSize(144, 154))

        icon20 = QIcon()
        icon20.addFile(url, QSize(), QIcon.Normal, QIcon.Off)
        self.ui.fotoPerfil.setIcon(icon20)
        self.ui.fotoPerfil.setIconSize(QSize(107, 118))

        self.database.connect_database()
        id = self.database.executarFetchall("SELECT UltimoUsuario from UltimoUsuario;")
        id = id[-1][0]
        self.database.executarComand(f"update Usuario set LinkFoto = '{url}' where id = '{id}';")
        self.database.disconnect_database()

    # adiconar categoria no BD e na interface
    def AdicionarCategoriaNaUI(self):
        barraCategoria = BarraCategoria()
        if self.ui.mudaNome_2.text() != '':
            if not self.ui.mudaNome_2.text().isnumeric():
                self.database.connect_database()
                n = self.database.executarFetchone("SELECT count(*) from categoria")
                n = n[0]
                self.database.executarComand(f"INSERT INTO categoria (nome) VALUES ('{self.ui.mudaNome_2.text()}')")
                self.database.disconnect_database()
                barraCategoria.setValores(self.ui.mudaNome_2.text())
                self.categoria.append(self.ui.mudaNome_2.text())
                self.axis_x.append(self.categoria)
                self.ui.verticalLayout_22.insertWidget(n, barraCategoria.bc.pequenoHistoricoEntrada)
                self.ui.mudaNome_2.setText("")

                self.ui.planoContasBuscaFluxo.clear()
                self.adicionaCategoriaPlanoContasBusca()
                self.novaMovimentacao.clearCategoria()
                self.novaMovimentacao.getAgenCategoria()

    # Volatar na tela de Login
    def exit(self):
        self.hide()
        self.hitoricoSaidaCont = SplashCreen()
        self.close()

    # este metodo inseri as informacões do usuario no perfil
    def informacoesUser(self):
        global NOMEUSER
        self.ui.userName.setText(NOMEUSER)

        self.database.connect_database()
        nUser = self.database.executarFetchone("SELECT count(*) from Usuario;")
        nUser = nUser[0]
        id = self.database.executarFetchall("SELECT UltimoUsuario from UltimoUsuario;")
        id = id[-1][0]
        descricao, linkFoto = self.database.executarFetchone("""
        select descricao, LinkFoto from Usuario WHERE id='1'
        """)
        self.database.disconnect_database()

        self.ui.descricao.setText(descricao)
        self.ui.TotalUser.setText(str(nUser))

        self.ui.dataPerfil.setText(self.pegarData())
        self.ui.data.setText(f'''<html><head/><body><p><span style=" color:#dcbbff;">date: 
        </span><span style=" color:#ffffff;">{self.pegarData()}</span></p></body></html>''')

        icon20 = QIcon()
        icon20.addFile(linkFoto, QSize(), QIcon.Normal, QIcon.Off)
        self.ui.fotoPerfil.setIcon(icon20)
        self.ui.fotoPerfil.setIconSize(QSize(107, 118))

        icon21 = QIcon()
        icon21.addFile(linkFoto, QSize(), QIcon.Normal, QIcon.Off)
        self.ui.perfifEdit.setIcon(icon21)
        self.ui.perfifEdit.setIconSize(QSize(144, 154))

    # decubrir valor maximo
    def valorMaximo(self, valor):
        maximo = 0
        for n, v in enumerate(valor):
            if n == 0:
                maximo = v
            else:
                if v > maximo:
                    maximo = 0
        return maximo

    # grafico de categoria
    def graficoCategoria(self):

        self.database.connect_database()
        listaValores = self.database.executarFetchall("""select categoria, sum(valor) from  MovimentacaoFinanceira group by categoria""")
        listaCategoria = self.database.executarFetchall("""select nome from  categoria""")
        self.database.disconnect_database()

        self.categoria = []
        listaValor = []
        auxiliar = []

        for dado in listaValores:
            listaValor.append(dado[1])
            self.categoria.append(self.encontraIndeceCategoria(dado[0]))

        for lA in listaCategoria:
            auxiliar.append(lA[0])

        for valor in auxiliar:
            if self.categoria.count(valor) == 0:
                self.categoria.append(valor)

        self.set = QBarSet("")

        valorMaximo = self.valorMaximo(listaValores[1])

        self.set.append(listaValor)
        self.set.setColor(QColor(170, 85, 255))

        self.series = QBarSeries()
        self.series.append(self.set)

        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)

        self.axis_x = QBarCategoryAxis()
        self.axis_x.append(self.categoria)

        self.axis_x.setLabelsColor(QColor(170, 85, 255))

        self.chart.addAxis(self.axis_x, Qt.AlignBottom)
        self.series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setLabelsColor(QColor(170, 85, 255))
        self.axis_y.setRange(0, valorMaximo)

        self.chart.addAxis(self.axis_y, Qt.AlignLeft)
        self.series.attachAxis(self.axis_y)

        self.chart.legend().setVisible(False)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.ui.verticalLayout_GraficoCategoria.addWidget(self._chart_view)

    # adiciona barra de categoria automaticamente
    def adicionarCategoriaAutomatic(self):
        self.database.connect_database()
        listaCetgoria = self.database.executarFetchall("SELECT * FROM Categoria")
        self.database.disconnect_database()

        for categoria in listaCetgoria:
            barraCategoria = BarraCategoria()
            barraCategoria.setValores(categoria[1])
            self.ui.verticalLayout_22.insertWidget(categoria[0]-1, barraCategoria.bc.pequenoHistoricoEntrada)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashCreen()
    sys.exit(app.exec())
