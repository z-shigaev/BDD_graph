import main_win
import plot_canvas as pc
import sys
import numpy as np
import math as mth

from PyQt5 import QtWidgets, QtCore, QtGui

class MainWindow(QtWidgets.QMainWindow, main_win.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowIcon(QtGui.QIcon('main_icon.jpg'))
        # Переменные, содержащие информацию о размерах виджетов графиков
        self.w1_width = self.widget1.frameGeometry().width()/100
        self.w1_height = self.widget1.frameGeometry().height()/100
        self.w2_width = self.widget2.frameGeometry().width()/100
        self.w2_height = self.widget2.frameGeometry().height()/100
        self.w3_width = self.widget3.frameGeometry().width()/100
        self.w3_height = self.widget3.frameGeometry().height()/100
        #
        self.widget1 = pc.PlotCanvas(self.tab1, self.widget1)
        self.widget2 = pc.PlotCanvas(self.tab2, self.widget2)
        self.widget3 = pc.PlotCanvas(self.tab3, self.widget3)

        # Инициализация переменных графиков
        self.g1_par1 = 0
        self.g1_par2 = 0
        self.g1_par3 = 0
        self.g1_min = 0
        self.g1_max = 0
        self.g1_coeff = 0
        #
        self.g2_par1 = 0
        self.g2_par2 = 0
        self.g2_par3 = 0
        self.g2_min = 0
        self.g2_max = 0
        self.g2_coeff = 0
        #
        self.g3_par1 = 0
        self.g3_par2 = 0
        self.g3_par3 = 0
        self.g3_min = 0
        self.g3_max = 0
        self.g3_coeff = 0
        # Обработка нажатий на кнопки
        self.btn_val1.clicked.connect(self.find_value1)
        self.btn_val2.clicked.connect(self.find_value2)
        self.btn_val3.clicked.connect(self.find_value3)
        #
        self.btn_create1.clicked.connect(self.create_plot1)
        self.btn_create2.clicked.connect(self.create_plot2)
        self.btn_create3.clicked.connect(self.create_plot3)



    def resizeEvent(self, event):
        print("Window has been resized")
        QtWidgets.QMainWindow.resizeEvent(self, event)
        self.test()

    def test(self):
        print('Тест пройден!')

    def find_value1(self):
        print(1)
        pass

    def find_value2(self):
        print(2)
        pass

    def find_value3(self):
        print(3)
        pass

    def create_plot1(self):
        print(4)
        pass

    def create_plot2(self):
        print(5)
        pass

    def create_plot3(self):
        print(6)
        pass


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # os.environ["QT_SCALE_FACTOR"] = "1.0"
    #
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение