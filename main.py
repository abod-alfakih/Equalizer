from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
from powerbar import PowerBar
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.axes_grid import make_axes_locatable
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
            self.timer = QtCore.QTimer()
            self.timer.setInterval(17)
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(1200, 900)
            self.mw = MainWindow
            MainWindow.setStyleSheet("background-color: rgb(100, 100, 100);")
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
            self.gridLayout.setObjectName("gridLayout")
            self.verticalLayout_2 = QtWidgets.QVBoxLayout()
            self.verticalLayout_2.setObjectName("verticalLayout_2")
            self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
            self.tabWidget.setStyleSheet("alternate-background-color: rgb(0, 0, 0);\n"
                                         "gridline-color: rgb(98, 98, 98);\n"
                                         "\n"
                                         "border-right-color: rgb(255, 0, 0);\n"
                                         "gridline-color: rgb(122, 122, 122);\n"
                                         "")

            self.tabWidget.setObjectName("tabWidget")
            self.tab = QtWidgets.QWidget()
            self.tab.setObjectName("tab")
            self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
            self.gridLayout_2.setObjectName("gridLayout_2")
            self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_4.setObjectName("horizontalLayout_4")
            self.LoadButton = QtWidgets.QPushButton(self.tab)

            self.LoadButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                          "color: rgb(85, 170, 255)")
            self.LoadButton.setObjectName("LoadButton")
            self.verticalLayout_2.addLayout(self.horizontalLayout_4)

            # self.equalizer = EqualizerBar(10,
            #                               ['#0C0786', '#40039C', '#6A00A7', '#8F0DA3', '#B02A8F', '#CA4678', '#E06461',
            #                                '#F1824C', '#FCA635', '#FCCC25', '#EFF821'])

            self.powerbar = PowerBar(["#909090", "#888888", "#808080", "#787878", "#707070", "#696969", "#686868",
                                      "#606060", "#585858", "#505050", "#484848", "#404040", "#383838", "#303030",
                                      "#282828", "#202020", "#181818", "#101010"])

            self.horizontalLayout_4.addWidget(self.LoadButton)
            self.PlayButton = QtWidgets.QPushButton(self.tab)
            self.PlayButton.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                            "color: rgb(85, 170, 255);")
            self.PlayButton.setObjectName("PlayButton")
            self.horizontalLayout_4.addWidget(self.PlayButton)

            self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
            self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_5.setObjectName("horizontalLayout_5")
            self.verticalLayout = QtWidgets.QVBoxLayout()
            self.verticalLayout.setObjectName("verticalLayout")
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName("horizontalLayout")
            self.DrumsSlider = QtWidgets.QSlider(self.tab)
            self.DrumsSlider.setStyleSheet("QSlider::handle:horizontal {background-color: black;}")
            self.DrumsSlider.setOrientation(QtCore.Qt.Horizontal)
            self.DrumsSlider.setObjectName("DrumsSlider")
            self.DrumsSlider.setMinimum(0)
            self.DrumsSlider.setValue(1)
            self.DrumsSlider.setMaximum(10)
            self.horizontalLayout.addWidget(self.DrumsSlider)
            self.toolButton = QtWidgets.QToolButton(self.tab)
            self.toolButton.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("dr1.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.toolButton.setIcon(icon)
            self.toolButton.setObjectName("toolButton")

            self.horizontalLayout.addWidget(self.toolButton)
            self.verticalLayout.addLayout(self.horizontalLayout)
            self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_2.setObjectName("horizontalLayout_2")
            self.ViolinSlider = QtWidgets.QSlider(self.tab)
            self.ViolinSlider.setStyleSheet("QSlider::handle:horizontal {background-color: black;}")
            self.ViolinSlider.setOrientation(QtCore.Qt.Horizontal)
            self.ViolinSlider.setObjectName("ViolinSlider")
            self.horizontalLayout_2.addWidget(self.ViolinSlider)
            self.ViolinSlider.setMinimum(0)
            self.ViolinSlider.setValue(1)
            self.ViolinSlider.setMaximum(10)
            self.toolButton_4 = QtWidgets.QToolButton(self.tab)
            self.toolButton_4.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("VAILON.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.toolButton_4.setIcon(icon)
            self.toolButton_4.setObjectName("toolButton_4")
            self.horizontalLayout_2.addWidget(self.toolButton_4)
            self.verticalLayout.addLayout(self.horizontalLayout_2)
            self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_3.setObjectName("horizontalLayout_3")
            self.FluteSlider = QtWidgets.QSlider(self.tab)
            self.FluteSlider.setMinimum(0)
            self.FluteSlider.setValue(1)
            self.FluteSlider.setMaximum(10)
            self.FluteSlider.setStyleSheet("QSlider::handle:horizontal {background-color: black;}")
            self.FluteSlider.setOrientation(QtCore.Qt.Horizontal)
            self.FluteSlider.setObjectName("FluteSlider")
            self.horizontalLayout_3.addWidget(self.FluteSlider)
            self.toolButton_5 = QtWidgets.QToolButton(self.tab)
            self.toolButton_5.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("FLUTE.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.toolButton_5.setIcon(icon)
            self.toolButton_5.setObjectName("toolButton_5")
            self.horizontalLayout_3.addWidget(self.toolButton_5)
            self.verticalLayout.addLayout(self.horizontalLayout_3)
            self.horizontalLayout_5.addLayout(self.verticalLayout)
            self.SignalView = pg.PlotWidget(self.tab)
            self.SignalView.setStyleSheet("background-color:rgb(0, 0, 0)")
            self.SignalView.setObjectName("SignalView")

            self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_7.setObjectName("horizontalLayout_7")

            self.PianoSlider = QtWidgets.QSlider(self.tab)
            self.PianoSlider.setStyleSheet("QSlider::handle:horizontal {background-color: black;}")
            self.PianoSlider.setOrientation(QtCore.Qt.Horizontal)
            self.PianoSlider.setObjectName("PianoSlider")
            self.PianoSlider.setMinimum(0)
            self.PianoSlider.setValue(1)
            self.PianoSlider.setMaximum(10)
            self.horizontalLayout_7.addWidget(self.PianoSlider)
            self.toolButton_7 = QtWidgets.QToolButton(self.tab)
            self.toolButton_7.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("PIANO.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.toolButton_7.setIcon(icon)
            self.toolButton_7.setObjectName("toolButton_7")
            self.horizontalLayout_7.addWidget(self.toolButton_7)
            self.verticalLayout.addLayout(self.horizontalLayout_7)

            self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
            self.horizontalLayout_8.setObjectName("horizontalLayout_8")

            self.XylophoneSlider = QtWidgets.QSlider(self.tab)
            self.XylophoneSlider.setStyleSheet("QSlider::handle:horizontal {background-color: black;}")
            self.XylophoneSlider.setOrientation(QtCore.Qt.Horizontal)
            self.XylophoneSlider.setObjectName("XylophoneSlider")
            self.horizontalLayout_8.addWidget(self.XylophoneSlider)
            self.XylophoneSlider.setMinimum(0)
            self.XylophoneSlider.setValue(1)
            self.XylophoneSlider.setMaximum(10)
            self.toolButton_8 = QtWidgets.QToolButton(self.tab)
            self.toolButton_8.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("Xylophone.png"), QtGui.QIcon.Normal,
                           QtGui.QIcon.Off)
            self.toolButton_8.setIcon(icon)
            self.toolButton_8.setObjectName("toolButton_8")
            self.horizontalLayout_8.addWidget(self.toolButton_8)
            self.verticalLayout.addLayout(self.horizontalLayout_8)



            self.verticalLayout_2.addWidget(self.SignalView)
            plt.style.use('dark_background')
            self.figure = Figure()
            self.axes = self.figure.add_subplot(2, 1, 1)
            self.axes1 = self.figure.add_subplot(2, 1, 2)
            self.axes.set_xlabel('Time')
            self.axes.set_ylabel('Frequency')
            self.axes1.set_xlabel('Frequency')
            self.axes1.set_ylabel('Spectral Power')
            self.divider = make_axes_locatable(self.axes)
            self.norm = mpl.colors.Normalize(vmin=0, vmax=10)
            self.c_bar_ax = self.divider.append_axes('right', size='5%', pad=0.25)
            self.canvas = FigureCanvas(self.figure)
            self.figure.tight_layout()
            self.verticalLayout_2.addWidget(self.canvas)
            self.horizontalLayout_5.addLayout(self.verticalLayout_2)
            self.horizontalLayout_5.setStretch(0, 10)
            self.horizontalLayout_5.setStretch(1, 40)
            self.horizontalLayout_5.addWidget(self.powerbar, stretch=5)
            self.gridLayout_2.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)
            self.tabWidget.addTab(self.tab, "")
            self.tab_2 = QtWidgets.QWidget()
            self.tab_2.setObjectName("tab_2")
            self.tabWidget.addTab(self.tab_2, "")
            self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

            self.c6 = QtWidgets.QPushButton(self.tab_2)
            self.c6.setGeometry(QtCore.QRect(920, 10, 41, 181))
            self.c6.setStyleSheet("#C{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#c6:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.c6.setText("")
            self.c6.setObjectName("C")
            self.c4 = QtWidgets.QPushButton(self.tab_2)
            self.c4.setGeometry(QtCore.QRect(360, 10, 41, 181))
            self.c4.setStyleSheet("#d{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#c4:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.c4.setText("")
            self.c4.setObjectName("d")
            self.b4 = QtWidgets.QPushButton(self.tab_2)
            self.b4.setGeometry(QtCore.QRect(600, 10, 41, 181))
            self.b4.setStyleSheet("#D{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#b4:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.b4.setText("")
            self.b4.setObjectName("D")
            self.a4 = QtWidgets.QPushButton(self.tab_2)
            self.a4.setGeometry(QtCore.QRect(560, 10, 41, 181))
            self.a4.setStyleSheet("#E{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#a4:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.a4.setText("")
            self.a4.setObjectName("E")
            self.c5 = QtWidgets.QPushButton(self.tab_2)
            self.c5.setGeometry(QtCore.QRect(640, 10, 41, 181))
            self.c5.setStyleSheet("#B{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#c5:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.c5.setText("")
            self.c5.setObjectName("B")
            self.f5 = QtWidgets.QPushButton(self.tab_2)
            self.f5.setGeometry(QtCore.QRect(760, 10, 41, 181))
            self.f5.setStyleSheet("#f{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#f5:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.f5.setText("")
            self.f5.setObjectName("f")
            self.e5 = QtWidgets.QPushButton(self.tab_2)
            self.e5.setGeometry(QtCore.QRect(720, 10, 41, 181))
            self.e5.setStyleSheet("#F{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#e5:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.e5.setText("")
            self.e5.setObjectName("F")
            self.b5 = QtWidgets.QPushButton(self.tab_2)
            self.b5.setGeometry(QtCore.QRect(880, 10, 41, 181))
            self.b5.setStyleSheet("#G{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#b5:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.b5.setText("")
            self.b5.setObjectName("G")
            self.e4 = QtWidgets.QPushButton(self.tab_2)
            self.e4.setGeometry(QtCore.QRect(440, 10, 41, 181))
            self.e4.setStyleSheet("#g{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#e4:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.e4.setText("")
            self.e4.setObjectName("g")
            self.g4 = QtWidgets.QPushButton(self.tab_2)
            self.g4.setGeometry(QtCore.QRect(520, 10, 41, 181))
            self.g4.setStyleSheet("#A{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#g4:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.g4.setText("")
            self.g4.setObjectName("A")
            self.a5 = QtWidgets.QPushButton(self.tab_2)
            self.a5.setGeometry(QtCore.QRect(840, 10, 41, 181))
            self.a5.setStyleSheet("#a{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#a5:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.a5.setText("")
            self.a5.setObjectName("a")
            self.d4 = QtWidgets.QPushButton(self.tab_2)
            self.d4.setGeometry(QtCore.QRect(400, 10, 41, 181))
            self.d4.setStyleSheet("#D{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#d4:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.d4.setText("")
            self.d4.setObjectName("D")
            self.g5 = QtWidgets.QPushButton(self.tab_2)
            self.g5.setGeometry(QtCore.QRect(800, 10, 41, 181))
            self.g5.setStyleSheet("#d{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#g5:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.g5.setText("")
            self.g5.setObjectName("d")
            self.d5 = QtWidgets.QPushButton(self.tab_2)
            self.d5.setGeometry(QtCore.QRect(680, 10, 41, 181))
            self.d5.setStyleSheet("#C{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#d5:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.d5.setText("")
            self.d5.setObjectName("C")
            self.f4 = QtWidgets.QPushButton(self.tab_2)
            self.f4.setGeometry(QtCore.QRect(480, 10, 41, 181))
            self.f4.setStyleSheet("#c{\n"
                                  "background-color: rgb(242, 242, 242);\n"
                                  "background-color: qlineargradient(spread:pad, x1:1, y1:0.711, x2:0.903455, y2:0.711, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
                                  "}\n"
                                  "\n"
                                  "\n"
                                  "#f4:pressed{\n"
                                  "background-color: rgb(250, 250, 250);\n"
                                  "\n"
                                  "}")
            self.f4.setText("")
            self.f4.setObjectName("c")
            self.c40 = QtWidgets.QPushButton(self.tab_2)
            self.c40.setGeometry(QtCore.QRect(380, 10, 31, 111))
            self.c40.setStyleSheet("#EgB{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
                                   "}\n"
                                   "#c40:pressed{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
                                   "\n"
                                   "}\n"
                                   "")
            self.c40.setText("")
            self.c40.setObjectName("EgB")
            self.d40 = QtWidgets.QPushButton(self.tab_2)
            self.d40.setGeometry(QtCore.QRect(420, 10, 31, 111))
            self.d40.setStyleSheet("#DfA{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
                                   "}\n"
                                   "#d40:pressed{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
                                   "\n"
                                   "}\n"
                                   "")
            self.d40.setText("")
            self.d40.setObjectName("DfA")
            self.f40 = QtWidgets.QPushButton(self.tab_2)
            self.f40.setGeometry(QtCore.QRect(510, 10, 31, 111))
            self.f40.setStyleSheet("#AcE{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
                                   "}\n"
                                   "#f40:pressed{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
                                   "\n"
                                   "}\n"
                                   "")
            self.f40.setText("")
            self.f40.setObjectName("AcE")
            self.g40 = QtWidgets.QPushButton(self.tab_2)
            self.g40.setGeometry(QtCore.QRect(550, 10, 31, 111))
            self.g40.setStyleSheet("#BDf{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
                                   "}\n"
                                   "#g40:pressed{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
                                   "\n"
                                   "}\n"
                                   "")
            self.g40.setText("")
            self.g40.setObjectName("BDf")
            self.a40 = QtWidgets.QPushButton(self.tab_2)
            self.a40.setGeometry(QtCore.QRect(590, 10, 31, 111))
            self.a40.setStyleSheet("#gAc{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
                                   "}\n"
                                   "#a40:pressed{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
                                   "\n"
                                   "}\n"
                                   "")
            self.a40.setText("")
            self.a40.setObjectName("gAc")
            self.c50 = QtWidgets.QPushButton(self.tab_2)
            self.c50.setGeometry(QtCore.QRect(670, 10, 31, 111))
            self.c50.setStyleSheet("#fAc{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
                                   "}\n"
                                   "#c50:pressed{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
                                   "\n"
                                   "}\n"
                                   "")
            self.c50.setText("")
            self.c50.setObjectName("fAc")
            self.d50 = QtWidgets.QPushButton(self.tab_2)
            self.d50.setGeometry(QtCore.QRect(710, 10, 31, 111))
            self.d50.setStyleSheet("#AcE{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
                                   "}\n"
                                   "#d50:pressed{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
                                   "\n"
                                   "}\n"
                                   "")
            self.d50.setText("")
            self.d50.setObjectName("AcE")
            self.f50 = QtWidgets.QPushButton(self.tab_2)
            self.f50.setGeometry(QtCore.QRect(790, 10, 31, 111))
            self.f50.setStyleSheet("#DfA{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
                                   "}\n"
                                   "#f50:pressed{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
                                   "\n"
                                   "}\n"
                                   "")
            self.f50.setText("")
            self.f50.setObjectName("DfA")
            self.g50 = QtWidgets.QPushButton(self.tab_2)
            self.g50.setGeometry(QtCore.QRect(830, 10, 31, 111))
            self.g50.setStyleSheet("#gAc{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
                                   "}\n"
                                   "#g50:pressed{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
                                   "\n"
                                   "}\n"
                                   "")
            self.g50.setText("")
            self.g50.setObjectName("gAc")
            self.a50 = QtWidgets.QPushButton(self.tab_2)
            self.a50.setGeometry(QtCore.QRect(870, 10, 31, 111))
            self.a50.setStyleSheet("#BDf{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0.028, y1:0.619, x2:1, y2:0.494, stop:0.852273 rgba(0, 0, 0, 250), stop:1 rgba(255, 255, 255, 255));\n"
                                   "}\n"
                                   "#a50:pressed{\n"
                                   "background-color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0.857955, y1:0.0170455, x2:1, y2:0, stop:0.125 rgba(0, 0, 0, 255), stop:0.977273 rgba(255, 255, 255, 255));\n"
                                   "\n"
                                   "}\n"
                                   "")
            self.a50.setText("")
            self.a50.setObjectName("BDf")
            self.label = QtWidgets.QLabel(self.tab_2)
            self.label.setGeometry(QtCore.QRect(650, 250, 291, 391))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap("g2-removebg-preview.png"))
            self.label.setScaledContents(True)
            self.label.setObjectName("label")
            self.String1 = QtWidgets.QPushButton(self.tab_2)
            self.String1.setGeometry(QtCore.QRect(795, 480, 16, 81))
            self.String1.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.String1.setText("")
            self.String1.setObjectName("String1")
            self.String2 = QtWidgets.QPushButton(self.tab_2)
            self.String2.setGeometry(QtCore.QRect(777, 480, 16, 81))
            self.String2.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.String2.setText("")
            self.String2.setObjectName("String2")
            self.String3 = QtWidgets.QPushButton(self.tab_2)
            self.String3.setGeometry(QtCore.QRect(813, 480, 16, 81))
            self.String3.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.String3.setText("")
            self.String3.setObjectName("String3")
            self.String4 = QtWidgets.QPushButton(self.tab_2)
            self.String4.setGeometry(QtCore.QRect(759, 480, 16, 81))
            self.String4.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.String4.setText("")
            self.String4.setObjectName("String4")
            self.DR1 = QtWidgets.QPushButton(self.tab_2)
            self.DR1.setGeometry(QtCore.QRect(380, 300, 151, 151))
            self.DR1.setMinimumSize(QtCore.QSize(93, 0))
            self.DR1.setStyleSheet("QPushButton {\n"
                                   "    background-color: rgb(247, 247, 247);\n"
                                   "    \n"
                                   "    \n"
                                   "    border: 2px solid #555;\n"
                                   "    border-radius: 50px;\n"
                                   "    border-style: outset;\n"
                                   " \n"
                                   "    padding: 5px;\n"
                                   "    }")
            self.DR1.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("dr2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.DR1.setIcon(icon)
            self.DR1.setIconSize(QtCore.QSize(120, 120))
            self.DR1.setObjectName("DOM")
            self.DR2 = QtWidgets.QPushButton(self.tab_2)
            self.DR2.setGeometry(QtCore.QRect(548, 300, 151, 151))
            self.DR2.setMinimumSize(QtCore.QSize(93, 0))
            self.DR2.setStyleSheet("QPushButton {\n"
                                   "    background-color: rgb(247, 247, 247);\n"
                                   "    \n"
                                   "    \n"
                                   "    border: 2px solid #555;\n"
                                   "    border-radius: 50px;\n"
                                   "    border-style: outset;\n"
                                   " \n"
                                   "    padding: 5px;\n"
                                   "    }\n"
                                   "\n"
                                   "\n"
                                   "")
            self.DR2.setText("")
            self.DR2.setIcon(icon)
            self.DR2.setIconSize(QtCore.QSize(110, 110))
            self.DR2.setObjectName("TNN")
            self.label = QtWidgets.QLabel(self.tab_2)
            self.label.setGeometry(QtCore.QRect(-110, 0, 451, 531))
            self.label.setText("")
            self.label.setPixmap(QtGui.QPixmap("cover.png"))
            self.label.setObjectName("label")
            self.PianoLabel = QtWidgets.QLabel(self.tab_2)
            self.PianoLabel.setGeometry(QtCore.QRect(380, 220, 271, 31))
            self.PianoLabel.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                       "selection-color: rgb(255, 255, 255);\n"
                                       "gridline-color: rgb(255, 255, 255);")
            self.PianoLabel.setTextFormat(QtCore.Qt.PlainText)
            self.PianoLabel.setIndent(-1)
            self.PianoLabel.setOpenExternalLinks(False)
            self.PianoLabel.setObjectName("PianoLabel")
            self.DrumLable = QtWidgets.QLabel(self.tab_2)
            self.DrumLable.setGeometry(QtCore.QRect(400, 490, 271, 31))
            self.DrumLable.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                       "selection-color: rgb(255, 255, 255);\n"
                                       "gridline-color: rgb(255, 255, 255);")
            self.DrumLable.setTextFormat(QtCore.Qt.PlainText)
            self.DrumLable.setIndent(-1)
            self.DrumLable.setOpenExternalLinks(False)
            self.DrumLable.setObjectName("DrumLable")
            self.GuitarLable = QtWidgets.QLabel(self.tab_2)
            self.GuitarLable.setGeometry(QtCore.QRect(750, 490, 271, 31))
            self.GuitarLable.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                       "selection-color: rgb(255, 255, 255);\n"
                                       "gridline-color: rgb(255, 255, 255);")
            self.GuitarLable.setTextFormat(QtCore.Qt.PlainText)
            self.GuitarLable.setIndent(-1)
            self.GuitarLable.setOpenExternalLinks(False)
            self.GuitarLable.setObjectName("GuitarLable")

            self.drumslider = QtWidgets.QSlider(self.tab_2)
            self.drumslider.setGeometry(QtCore.QRect(400, 500, 280, 22))
            self.drumslider.setOrientation(QtCore.Qt.Horizontal)
            self.drumslider.setObjectName("drumslider")
            self.drumslider.setStyleSheet("QSlider::handle:horizontal {background-color: black;}")
            self.drumslider.setMinimum(0)
            self.drumslider.setValue(5)
            self.drumslider.setMaximum(10)

            self.label1 = QtWidgets.QLabel(self.tab_2)
            self.label1.setGeometry(QtCore.QRect(690, 500, 778, 16))
            self.label1.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(self.tab_2)
            self.label_2.setGeometry(QtCore.QRect(690, 540, 778, 16))
            self.label_2.setObjectName("label_2")

            self.sliderguitar = QtWidgets.QSlider(self.tab_2)
            self.sliderguitar.setGeometry(QtCore.QRect(400, 540, 280, 22))
            self.sliderguitar.setOrientation(QtCore.Qt.Horizontal)
            self.sliderguitar.setObjectName("sliderguitar")
            self.sliderguitar.setStyleSheet("QSlider::handle:horizontal {background-color: black;}")
            self.sliderguitar.setMinimum(0)
            self.sliderguitar.setValue(5)
            self.sliderguitar.setMaximum(10)


            self.c4.raise_()
            self.d4.raise_()
            self.c40.raise_()
            self.e4.raise_()
            self.f4.raise_()
            self.d40.raise_()
            self.g4.raise_()
            self.a4.raise_()
            self.b4.raise_()
            self.c5.raise_()
            self.d5.raise_()
            self.a5.raise_()
            self.e5.raise_()
            self.g5.raise_()
            self.f5.raise_()
            self.b5.raise_()
            self.c6.raise_()
            self.f40.raise_()
            self.g40.raise_()
            self.a40.raise_()
            self.c50.raise_()
            self.d50.raise_()
            self.f50.raise_()
            self.g50.raise_()
            self.a50.raise_()
            self.String1.raise_()
            self.String2.raise_()
            self.String3.raise_()
            self.String4.raise_()
            self.DR1.raise_()
            self.DR2.raise_()

            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 26))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)

            self.retranslateUi(MainWindow)
            self.tabWidget.setCurrentIndex(0)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            self.LoadButton.setText(_translate("MainWindow", "LOAD"))
            self.PlayButton.setText(_translate("MainWindow", "PLAY"))
            self.toolButton.setText(_translate("MainWindow", "..."))
            self.toolButton_4.setText(_translate("MainWindow", "..."))
            self.toolButton_5.setText(_translate("MainWindow", "..."))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
            self.c4.setShortcut(_translate("MainWindow", "A"))
            self.d4.setShortcut(_translate("MainWindow", "S"))
            self.c40.setShortcut(_translate("MainWindow", "Q"))
            self.d40.setShortcut(_translate("MainWindow", "W"))
            self.e4.setShortcut(_translate("MainWindow", "D"))
            self.f4.setShortcut(_translate("MainWindow", "F"))
            self.g4.setShortcut(_translate("MainWindow", "G"))
            self.a4.setShortcut(_translate("MainWindow", "H"))
            self.b4.setShortcut(_translate("MainWindow", "J"))
            self.c5.setShortcut(_translate("MainWindow", "K"))
            self.d5.setShortcut(_translate("MainWindow", "L"))
            self.a5.setShortcut(_translate("MainWindow", "V"))
            self.e5.setShortcut(_translate("MainWindow", "Z"))
            self.g5.setShortcut(_translate("MainWindow", "C"))
            self.f5.setShortcut(_translate("MainWindow", "X"))
            self.b5.setShortcut(_translate("MainWindow", "B"))
            self.c6.setShortcut(_translate("MainWindow", "N"))
            self.f40.setShortcut(_translate("MainWindow", "E"))
            self.g40.setShortcut(_translate("MainWindow", "R"))
            self.a40.setShortcut(_translate("MainWindow", "T"))
            self.c50.setShortcut(_translate("MainWindow", "Y"))
            self.d50.setShortcut(_translate("MainWindow", "U"))
            self.f50.setShortcut(_translate("MainWindow", "I"))
            self.g50.setShortcut(_translate("MainWindow", "O"))
            self.a50.setShortcut(_translate("MainWindow", "P"))
            self.DR1.setShortcut(_translate("MainWindow", "1"))
            self.DR2.setShortcut(_translate("MainWindow", "2"))

            self.String1.setShortcut(_translate("MainWindow", "4"))
            self.String2.setShortcut(_translate("MainWindow", "5"))
            self.String3.setShortcut(_translate("MainWindow", "6"))
            self.String4.setShortcut(_translate("MainWindow", "7"))

            self.label1.setText(_translate("MainWindow", "Drums"))
            self.label_2.setText(_translate("MainWindow", "guatar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())