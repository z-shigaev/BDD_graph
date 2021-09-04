
import random
from PyQt5.QtWidgets import QSizePolicy

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QTableWidgetItem

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np



class Layout(QVBoxLayout):
    def __init__(self, root, x, y):
        super().__init__()
        plt.style.use("seaborn-dark")

        self.figure = plt.figure()
        self.ax1= self.figure.add_subplot(111)
        self.ax1.plot(x, y)
        self.canvas = FigureCanvas(self.figure)
        # self.toolbar = NavigationToolbar(self.canvas, root)
        # self.addWidget(self.toolbar)
        self.addWidget(self.canvas)

    def draw_graph(self, x1, y1):
        try:
            self.figure.clear()
            self.ax2 = self.figure.add_subplot(111)
            self.ax2.plot(x1, y1)
            self.ax2.set_xlabel('Ось X')
            self.ax2.set_ylabel('Ось Y')
            self.ax2.spines['right'].set_visible(False)
            self.ax2.grid(color = 'black', linewidth = 1, linestyle = '--')
            self.canvas.draw()
        except Exception as error:
            print("Исключение " + str(error))



