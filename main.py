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
        #self.widget1 = pc.PlotCanvas(self.tab1, self.widget1)
        #self.widget2 = pc.PlotCanvas(self.tab2, self.widget2)
        #self.widget3 = pc.PlotCanvas(self.tab3, self.widget3)
        self.x = []
        self.y = []
        self.widget1_layout = pc.Layout(self.widget1, self.x, self.y)
        self.widget1.setLayout(self.widget1_layout)
        self.widget2_layout = pc.Layout(self.widget2, self.x, self.y)
        self.widget2.setLayout(self.widget2_layout)
        self.widget3_layout = pc.Layout(self.widget3, self.x, self.y)
        self.widget3.setLayout(self.widget3_layout)
#        self.widget2_layout = pc.Layout(self.widget2)
#        self.widget2.setLayout(self.widget2_layout)
#        self.widget3_layout = pc.Layout(self.widget3)
#        self.widget3.setLayout(self.widget3_layout)

        # Инициализация переменных графиков
        self.g1_par1 = 0
        self.g1_par2 = 0
        self.g1_par3 = 0
        self.g1_min = 0
        self.g1_max = 0
        self.g1_coeff = 0
        self.g1_step = 0
        self.x1 = []
        self.y1 = []
        #
        self.g2_par1 = 0
        self.g2_par2 = 0
        self.g2_par3 = 0
        self.g2_min = 0
        self.g2_max = 0
        self.g2_coeff = 0
        self.g2_step = 0
        self.x2 = []
        self.y2 = []
        #
        self.g3_par1 = 0
        self.g3_par2 = 0
        self.g3_par3 = 0
        self.g3_min = 0
        self.g3_max = 0
        self.g3_coeff = 0
        self.g3_step = 0
        self.x3 = []
        self.y3 = []
        #
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
        val = self.dSB_arg1.value()
        i = 0
        j = -1
        for m in self.x1:
            i = i + 1
            if m == val:
                j = i
                break
        if j == -1:
            self.lE_val1.setText(" Ошибка! ")
        else:
            self.lE_val1.setText(str(self.y1[j-1]))


        print(1)
        pass

    def find_value2(self):
        val = self.dSB_arg2.value()
        i = 0
        j = -1
        for m in self.x2:
            i = i + 1
            if m == val:
                j = i
                break
        if j == -1:
            self.lE_val2.setText(" Ошибка! ")
        else:
            self.lE_val2.setText(str(self.y2[j-1]))
        print(2)
        pass

    def find_value3(self):
        val = self.dSB_arg3.value()
        i = 0
        j = -1
        for m in self.x3:
            i = i + 1
            if m == val:
                j = i
                break
        if j == -1:
            self.lE_val3.setText(" Ошибка! ")
        else:
            self.lE_val3.setText(str(self.y3[j-1]))
        print(3)
        pass

    def create_plot1(self):
        self.g1_par1 = self.dSB_par11.value()
        self.g1_par2 = self.dSB_par12.value()
        self.g1_par3 = self.dSB_par13.value()
        self.g1_min = self.dSB_min1.value()
        self.g1_max = self.dSB_max1.value()
        self.g1_coeff = self.dSB_coeff1.value()
        self.g1_step = self.dSB_step1.value()
        if self.g1_min == self.g1_max:
            pass
        else:
            if self.g1_step == 0:
                pass
            else:
                self.x = np.arange(self.g1_min, self.g1_max, self.g1_step)
                self.y = []
                for m in self.x:
                    a = m ** 2
                    self.y.append(a)
                self.widget1_layout.draw_graph(self.x, self.y)
                self.x1 = self.x
                self.y1 = self.y
                print(4)
                pass



    def create_plot2(self):
        self.g2_par1 = self.dSB_par21.value()
        self.g2_par2 = self.dSB_par22.value()
        self.g2_par3 = self.dSB_par23.value()
        self.g2_min = self.dSB_min2.value()
        self.g2_max = self.dSB_max2.value()
        self.g2_coeff = self.dSB_coeff2.value()
        self.g2_step = self.dSB_step2.value()
        if self.g2_min == self.g2_max:
            pass
        else:
            if self.g2_step == 0:
                pass
            else:
                self.x = np.arange(self.g2_min, self.g2_max, self.g2_step)
                self.y = []
                for m in self.x:
                    a = m ** 3
                    self.y.append(a)
                self.widget2_layout.draw_graph(self.x, self.y)
                self.x2 = self.x
                self.y2 = self.y
                print(5)
                pass



    def create_plot3(self):
        self.g3_par1 = self.dSB_par31.value()
        self.g3_par2 = self.dSB_par32.value()
        self.g3_par3 = self.dSB_par33.value()
        self.g3_min = self.dSB_min3.value()
        self.g3_max = self.dSB_max3.value()
        self.g3_coeff = self.dSB_coeff3.value()
        self.g3_step = self.dSB_step3.value()
        if self.g3_min == self.g3_max:
            pass
        else:
            if self.g3_step == 0:
                pass
            else:
                self.x = np.arange(self.g3_min, self.g3_max, self.g3_step)
                self.y = []
                for m in self.x:
                    a = m ** 4
                    self.y.append(a)
                self.widget3_layout.draw_graph(self.x, self.y)
                self.x3 = self.x
                self.y3 = self.y
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