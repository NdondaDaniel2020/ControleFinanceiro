import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCharts import (QBarCategoryAxis, QBarSet, QChart, QChartView,
                              QStackedBarSeries, QValueAxis)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        # QBarSet Um conjunto de barras contém um valor de dados para cada categoria
        low = QBarSet("Min")
        high = QBarSet("Max")

        # add dados para cada categoria
        low.append([-52, -50, -45.3, -37.0, -25.6, -8.0,
                    -6.0, -11.8, -19.7, -32.8, -43.0, -48.0])
        
        high.append([11.9, 12.8, 18.5, 26.5, 32.0, 34.8,
                     38.2, 34.8, 29.8, 20.4, 15.1, 11.8])

        # QStackedBarSeries e Cada conjunto de barras adicionado à série contribui com um único segmento para cada barra empilhada

        series = QStackedBarSeries()
        series.append(low)  # add conjunto de barras
        series.append(high)  # add conjunto de barras

        # QChart é um QGraphicsWidget que você pode mostrar em um QGraphicsScene . Ele gerencia a representação gráfica de diferentes tipos de séries e outros objetos relacionados ao gráfico, como legendas e eixos.
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Temperaturas recordes em celso")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # as categoria por mes
        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                      "Aug", "Sep", "Oct", "Nov", "Dec"]

        # A classe QBarCategoryAxis adiciona categorias aos eixos de um gráfico
        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        axis_x.setTitleText("Month")
        chart.addAxis(axis_x, Qt.AlignBottom) # add Eixo

        # A classe QValueAxis adiciona valores aos eixos de um gráfico
        axis_y = QValueAxis()
        axis_y.setRange(-52, 52)
        axis_y.setTitleText("Temperature [&deg;C]")
        chart.addAxis(axis_y, Qt.AlignLeft) # add Eixo

        series.attachAxis(axis_x)  # anexar os Eixos
        series.attachAxis(axis_y)  # anexar os Eixos

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom) # alinhamento dos significados de cada cor

        # O QChartView é um widget autônomo que pode exibir gráficos
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing) # QPainter.Antialiasing desenha o grafico

        self.setCentralWidget(chart_view) # add ao widget central

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.resize(600, 300)
    w.show()
    sys.exit(app.exec())