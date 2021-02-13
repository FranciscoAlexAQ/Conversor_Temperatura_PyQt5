from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JanelaPrincipal(object):
    def setupUi(self, JanelaPrincipal):
        JanelaPrincipal.setObjectName("JanelaPrincipal")
        JanelaPrincipal.resize(339, 465)
        JanelaPrincipal.setLayoutDirection(QtCore.Qt.LeftToRight)
        JanelaPrincipal.setAutoFillBackground(False)
        JanelaPrincipal.setStyleSheet("BACKGROUND-COLOR: rgb(0, 85, 127)")
        self.centralwidget = QtWidgets.QWidget(JanelaPrincipal)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setStyleSheet("red;")
        self.centralwidget.setObjectName("centralwidget")
        self.campos_celsius = QtWidgets.QLineEdit(self.centralwidget)
        self.campos_celsius.setGeometry(QtCore.QRect(100, 140, 181, 31))
        self.campos_celsius.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.campos_celsius.setAutoFillBackground(False)
        self.campos_celsius.setStyleSheet("background-color: lightgray;\n"
"border: none")
        self.campos_celsius.setInputMask("")
        self.campos_celsius.setCursorPosition(0)
        self.campos_celsius.setAlignment(QtCore.Qt.AlignCenter)
        self.campos_celsius.setReadOnly(False)
        self.campos_celsius.setObjectName("campos_celsius")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(60, 50, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.titulo.setFont(font)
        self.titulo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.titulo.setStyleSheet("color: rgb(255, 255, 255)\n"
"")
        self.titulo.setObjectName("titulo")
        self.celsius = QtWidgets.QLabel(self.centralwidget)
        self.celsius.setGeometry(QtCore.QRect(10, 140, 81, 31))
        self.celsius.setStyleSheet("color: rgb(255, 255, 255)")
        self.celsius.setObjectName("celsius")
        self.campo_fahrenheit = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_fahrenheit.setAlignment(QtCore.Qt.AlignCenter)
        self.campo_fahrenheit.setEnabled(True)
        self.campo_fahrenheit.setGeometry(QtCore.QRect(100, 190, 181, 31))
        self.campo_fahrenheit.setStyleSheet("background-color: lightgray;\n"
"border: none")
        self.campo_fahrenheit.setReadOnly(True)
        self.campo_fahrenheit.setObjectName("campo_fahrenheit")
        self.fahrenheit = QtWidgets.QLabel(self.centralwidget)
        self.fahrenheit.setGeometry(QtCore.QRect(10, 190, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.fahrenheit.setFont(font)
        self.fahrenheit.setStyleSheet("color: rgb(255, 255, 255)")
        self.fahrenheit.setObjectName("fahrenheit")
        self.btn_converter = QtWidgets.QPushButton(self.centralwidget)
        self.btn_converter.clicked.connect(lambda: self.calcular())
        self.btn_converter.setGeometry(QtCore.QRect(100, 260, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_converter.setFont(font)
        self.btn_converter.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black; \n"
"")
        self.btn_converter.setObjectName("btn_converter")
        self.btn_converter_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_converter_2.clicked.connect(lambda: self.resetar())
        self.btn_converter_2.setGeometry(QtCore.QRect(100, 310, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_converter_2.setFont(font)
        self.btn_converter_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: black")
        self.btn_converter_2.setObjectName("btn_converter_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(100, 100, 82, 17))
        self.radioButton.setStyleSheet("color: white")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(200, 100, 82, 17))
        self.radioButton_2.setStyleSheet("color: white")
        self.radioButton_2.setObjectName("radioButton_2")
        JanelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(JanelaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 339, 21))
        self.menubar.setObjectName("menubar")
        JanelaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(JanelaPrincipal)
        self.statusbar.setObjectName("statusbar")
        JanelaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(JanelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(JanelaPrincipal)

    def retranslateUi(self, JanelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        JanelaPrincipal.setWindowTitle(_translate("JanelaPrincipal", "MainWindow"))
        self.titulo.setText(_translate("JanelaPrincipal", "CONVERSOR DE TEMPERATURA"))
        self.celsius.setText(_translate("JanelaPrincipal", "TEMPERATURA"))
        self.fahrenheit.setText(_translate("JanelaPrincipal", "RESULTADO"))
        self.btn_converter.setText(_translate("JanelaPrincipal", "CONVERTER"))
        self.btn_converter_2.setText(_translate("JanelaPrincipal", "RESETAR"))
        self.radioButton.setText(_translate("JanelaPrincipal", "CELSIUS"))
        self.radioButton_2.setText(_translate("JanelaPrincipal", "FAHRENHEIT"))

    def calcular(self):
        if self.radioButton.isChecked():
            if self.campos_celsius.text().isnumeric():
                temperatura = float(self.campos_celsius.text()) * 9 / 5 + 32
                self.campo_fahrenheit.setText(str(temperatura) + '°F')
            elif ',' in self.campos_celsius.text():
                temperatura = self.campos_celsius.text().replace(',', '.')
                temperaturaFinal = float(temperatura) * 9 / 5 + 32
                self.campo_fahrenheit.setText(str(temperaturaFinal) + '°F')
            elif '.' in self.campos_celsius.text():
                temperatura = self.campos_celsius.text().replace('.', '.')
                temperaturaFinal = float(temperatura) * 9 / 5 + 32
                self.campo_fahrenheit.setText(str(temperaturaFinal) + '°F')
            else:
                self.campo_fahrenheit.setText('Valor inválido!')
        elif self.radioButton_2.isChecked():
            if self.campos_celsius.text().isnumeric():
                temperatura = (float(self.campos_celsius.text()) - 32) * 5 / 9
                self.campo_fahrenheit.setText(str(temperatura) + '°C')
            elif ',' in self.campos_celsius.text():
                temperatura = self.campos_celsius.text().replace(',', '.')
                temperaturaFinal = (float(temperatura) - 32) * 5 / 9
                self.campo_fahrenheit.setText(str(temperaturaFinal) + '°C')
            elif '.' in self.campos_celsius.text():
                temperatura = self.campos_celsius.text().replace('.', '.')
                temperaturaFinal = (float(temperatura) - 32) * 5 / 9
                self.campo_fahrenheit.setText(str(temperaturaFinal) + '°C')
            else:
                self.campo_fahrenheit.setText('Valor inválido')   
        else:
            self.campo_fahrenheit.setText('Selecione um modo')

    def resetar(self):
        self.campos_celsius.setText('')
        self.campo_fahrenheit.setText('')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    JanelaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_JanelaPrincipal()
    ui.setupUi(JanelaPrincipal)
    JanelaPrincipal.show()
    sys.exit(app.exec_())
