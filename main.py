from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import pandas as pd


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(749, 566)
        # MainWindow.setStyleSheet("background-color: rgb(210, 233, 252);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setStyleSheet("background-color: rgb(210, 233, 252);")
        self.centralwidget.setObjectName("centralwidget")

        self.line_input = QtWidgets.QLineEdit(self.centralwidget)
        self.line_input.setGeometry(QtCore.QRect(130, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(25)
        self.line_input.setFont(font)
        self.line_input.setObjectName("line_input")
        self.line_input.setStyleSheet("background-color: rgb(255, 170, 127);")

        self.btn_algorithm = QtWidgets.QPushButton(self.centralwidget)
        self.btn_algorithm.setGeometry(QtCore.QRect(320, 520, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(9)
        self.btn_algorithm.setFont(font)
        self.btn_algorithm.setStyleSheet("background-color: rgb(140, 146, 255);\n""")
        self.btn_algorithm.setObjectName("btn_algorithm")
        self.btn_algorithm.clicked.connect(self.start_algorithm)

        self.line_output = QtWidgets.QListView(self.centralwidget)
        self.line_output.setGeometry(QtCore.QRect(10, 70, 731, 441))
        self.line_output.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line_output.setObjectName("line_output")

        self.scroll_box = QtWidgets.QComboBox(self.centralwidget)
        self.scroll_box.setGeometry(QtCore.QRect(70, 520, 231, 31))
        self.scroll_box.setStyleSheet("background-color: rgb(140, 146, 255);")
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(9)
        self.scroll_box.setFont(font)
        self.scroll_box.setStyleSheet("background-color: rgb(140, 146, 255);")
        self.scroll_box.setObjectName("scroll_box")
        self.scroll_box.addItem("Алгоритм обхода в глубину")
        self.scroll_box.addItem("Алгоритм обхода в ширину")
        self.scroll_box.addItem("Алгоритм Дейкстры")
        self.scroll_box.addItem("Алгоритм Флойда")
        self.scroll_box.addItem("Алгоритм Данцига")
        self.scroll_box.addItem("Алгоритм Форда-Фалкерсона")

        self.print_graph = QtWidgets.QPushButton(self.centralwidget)
        self.print_graph.setGeometry(QtCore.QRect(490, 520, 161, 41))
        self.print_graph.setStyleSheet("background-color: rgb(140, 146, 255);")
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.print_graph.setFont(font)
        self.print_graph.setObjectName("print_graph")
        self.print_graph.clicked.connect(self.display_graph)

        self.matrix_input = []
        self.matrix_widget = QtWidgets.QWidget(self.centralwidget)
        self.matrix_widget.setGeometry(QtCore.QRect(500, 70, 241, 441))
        self.matrix_layout = QtWidgets.QGridLayout(self.matrix_widget)

        self.add_matrix = QtWidgets.QPushButton(self.centralwidget)
        self.add_matrix.setGeometry(QtCore.QRect(380, 10, 361, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.add_matrix.setFont(font)
        self.add_matrix.setStyleSheet("background-color: rgb(140, 146, 255);")
        self.add_matrix.setObjectName("add_matrix")
        self.add_matrix.clicked.connect(self.add_row)

        self.print_matrix = QtWidgets.QPushButton(self.centralwidget)
        self.print_matrix.setGeometry(QtCore.QRect(380, 40, 361, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        self.print_matrix.setFont(font)
        self.print_matrix.setStyleSheet("background-color: rgb(140, 146, 255);")
        self.print_matrix.setObjectName("print_matrix")
        self.print_matrix.clicked.connect(self.print_adjacency_matrix)

        self.istok = QtWidgets.QPushButton(self.centralwidget)
        self.istok.setGeometry(QtCore.QRect(20, 10, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.istok.setFont(font)
        self.istok.setStyleSheet("background-color: rgb(140, 146, 255);")
        self.istok.setObjectName("istok")
        self.istok.clicked.connect(self.add_istok)

        self.stok = QtWidgets.QPushButton(self.centralwidget)
        self.stok.setGeometry(QtCore.QRect(20, 40, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        self.stok.setFont(font)
        self.stok.setStyleSheet("background-color: rgb(140, 146, 255);")
        self.stok.setObjectName("stok")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.matrix_input = []
        self.G = nx.Graph()
        self.adjacency_matrix = []
        self.matrix_input_1 = []
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.vershin = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_algorithm.setText(_translate("MainWindow", "Запустить алгоритм"))
        self.print_graph.setText(_translate("MainWindow", "Вывод графа"))
        self.add_matrix.setText(_translate("MainWindow", "Добавить строку матрицы смежности"))
        self.print_matrix.setText(_translate("MainWindow", "Вывести матрицу смежности"))
        self.istok.setText(_translate("MainWindow", "Исток"))
        self.stok.setText(_translate("MainWindow", "Сток"))

    def add_row(self):
        row = self.line_input.text()
        row = row.split()
        self.matrix_input.append(row)
        self.line_input.clear()

    def print_adjacency_matrix(self):
        matrix = QMessageBox()
        matrix.setWindowTitle("Матрица смежности")
        self.matrix_input_1 = []
        for row in self.matrix_input:
            temp_row = [int(column) for column in row]
            self.matrix_input_1.append(temp_row)

        x = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.matrix_input_1])
        matrix.setText(f"{x}")
        matrix.setStandardButtons(QMessageBox.Close)
        matrix.exec_()

    def start_algorithm(self):
        algorithm = self.scroll_box.currentText()
        if algorithm == "Алгоритм обхода в глубину":
            result = self.Search()
            self.show_result(result)
        elif algorithm == "Алгоритм обхода в ширину":
            result = self.breadth_first_search()
            self.show_result(result)

    def Search(self):
        result = [self.vershin]

        def Find(root):
            for new in self.G.neighbors(root):
                if new not in result:
                    result.append(new)
                    Find(new)

        Find(self.vershin)
        return result

    def add_istok(self):
        self.vershin = int(self.line_input.text())
        self.line_input.clear()

    def breadth_first_search(self):
        num_vertices = len(self.matrix_input_1)
        visited = [False] * num_vertices
        result = []

        def bfs(start_vertex):
            queue = []
            queue.append(start_vertex)
            visited[start_vertex] = True

            while queue:
                vertex = queue.pop(0)
                result.append(vertex)

                for neighbor in range(num_vertices):
                    if self.matrix_input_1[vertex][neighbor] == 1 and not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True

        bfs(self.vershin)
        return result

    def display_graph(self):
        self.figure.clear()
        plt.clf()
        self.G = nx.from_numpy_array(np.array(self.matrix_input_1))
        nx.draw(self.G, with_labels=True)
        plt.axis('off')
        layout = QtWidgets.QVBoxLayout(self.line_output)
        layout.addWidget(self.canvas)
        layout.setContentsMargins(0, 0, 0, 0)
        self.canvas.draw_idle()

    def show_result(self, result):
        new_window = QMessageBox()
        new_window.setWindowTitle("Результат алгоритма")
        new_window.setText(str(result))
        new_window.setStandardButtons(QMessageBox.Close)
        new_window.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
