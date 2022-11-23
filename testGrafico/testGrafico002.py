
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter, QPen
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import QChart, QChartView, QPieSeries


class TestChart(QMainWindow):

    def __init__(self):
        super().__init__()

        # A classe QPieSeries apresenta dados em gráficos de pizza
        self.series = QPieSeries()

        # add as partes que faram parte do grafico
        self.series.append('Jane', 1)
        self.series.append('Joe', 2)
        self.series.append('Andy', 3)
        self.series.append('Barbara', 4)
        self.series.append('Axel', 5)

        # Uma série de pizza consiste em fatias definidas como QPieSliceobjetos. As fatias podem ter qualquer valor, pois o QPieSeriesobjeto calcula a porcentagem de uma fatia comparada com a soma de todas as fatias da série para determinar o tamanho real da fatia no gráfico.

        self.slice = self.series.slices()[0] # os valores sao responsaveis pelo valor que saiu
        self.slice.setExploded() # faz o selecionado sair um pouco fora
        self.slice.setLabelVisible() # aumenta sua visiblidade
        self.slice.setPen(QPen(Qt.darkGreen, 2)) #pinta as borda s de a cor dentro do pen no casoa a acima e verde
        self.slice.setBrush(Qt.green) # pinta o interior do selecionado

        # QChart é um QGraphicsWidget que você pode mostrar em um QGraphicsScene . Ele gerencia a representação gráfica de diferentes tipos de séries e outros objetos relacionados ao gráfico, como legendas e eixos.
        self.chart = QChart()
        self.chart.addSeries(self.series) # add a serie no quadro
        self.chart.setTitle('Simple piechart example') #responsavel peo titulo
        self.chart.setAnimationOptions(QChart.SeriesAnimations) # responsavel pela aniamacao
        self.chart.legend().hide() # esconde os nomes de cada parate pa pizza
        
        
        # O QChartView é um widget autônomo que pode exibir gráficos
        self._chart_view = QChartView(self.chart)
        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(self._chart_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = TestChart()
    window.show()
    window.resize(440, 300)

    sys.exit(app.exec())