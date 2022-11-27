self.stackedWidget = SlidingStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(159, 80, 239);\n"
        "border-top-left-radius:10px;\n"
        "border-bottom-left-radius:10px;")


if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        window = QMainWindow()
        ui = Ui_MainWindowMW()
        ui.setupUi(window)
        window.show()
        sys.exit(app.exec())
