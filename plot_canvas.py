
import random
from PyQt5.QtWidgets import QSizePolicy

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QTableWidgetItem

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
#from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np



class Layout(QVBoxLayout):
    def __init__(self, root, x, y):
        super().__init__()
        plt.style.use("seaborn-dark")

        self.figure = plt.figure()
        self.ax1 = self.figure.add_subplot(211)
        self.ax1.plot(x, y)
        self.ax2 = self.figure.add_subplot(223)
        self.ax3 = self.figure.add_subplot(224)
        self.canvas = FigureCanvas(self.figure)
        # self.toolbar = NavigationToolbar(self.canvas, root)
        # self.addWidget(self.toolbar)
        self.addWidget(self.canvas)

    def draw_graph(self, x1, y1):
        try:
            xlabel = 8
            ylabel = 8
            xlabelpad = 0
            ylabelpad = xlabelpad
            #
            self.figure.clear()
            #
            self.ax1 = self.figure.add_subplot(211)
            self.ax2 = self.figure.add_subplot(223)
            self.ax3 = self.figure.add_subplot(224)
            #
            self.ax1.plot(x1, y1)
            #
            #self.ax1.xaxis.set_major_locator(ticker.MultipleLocator(2))
            #self.ax1.xaxis.set_minor_locator(ticker.MultipleLocator(1))
            #self.ax1.yaxis.set_major_locator(ticker.MultipleLocator(50))
            #self.ax1.yaxis.set_minor_locator(ticker.MultipleLocator(10))
            #
            self.ax1.tick_params(labelsize=6)
            self.ax1.set_xlabel('Ось X', fontsize=xlabel, labelpad=xlabelpad)
            self.ax1.set_ylabel('Ось Y', fontsize=ylabel, labelpad=ylabelpad)
            self.ax1.spines['right'].set_visible(False)
            self.ax1.grid(color='black', linewidth=1, linestyle='--')
            #
            #self.ax1.plot(x1, y1)
            self.ax2.tick_params(labelsize=6)
            self.ax2.set_xlabel('Ось X', fontsize=xlabel, labelpad=xlabelpad)
            self.ax2.set_ylabel('Ось Y', fontsize=ylabel, labelpad=ylabelpad)
            self.ax2.spines['right'].set_visible(False)
            self.ax2.grid(color='black', linewidth=1, linestyle='--')
            #
            #self.ax1.plot(x1, y1)
            self.ax3.tick_params(labelsize=6)
            self.ax3.set_xlabel('Ось X', fontsize=xlabel, labelpad=xlabelpad)
            self.ax3.set_ylabel('Ось Y', fontsize=ylabel, labelpad=ylabelpad)
            self.ax3.spines['right'].set_visible(False)
            self.ax3.grid(color='black', linewidth=1, linestyle='--')
            self.canvas.draw()
        except Exception as error:
            print("Поймано исключение " + str(error))



