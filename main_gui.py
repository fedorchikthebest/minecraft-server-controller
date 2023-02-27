# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.tabWidget.setObjectName("tabWidget")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.main_tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(780, 0, 491, 541))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.console = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.console.setObjectName("console")
        self.verticalLayout.addWidget(self.console)
        self.input = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input.setObjectName("input")
        self.verticalLayout.addWidget(self.input)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.start.setObjectName("start")
        self.horizontalLayout.addWidget(self.start)
        self.stop = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.stop.setObjectName("stop")
        self.horizontalLayout.addWidget(self.stop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayoutWidget = QtWidgets.QWidget(self.main_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(140, 240, 389, 80))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Xms = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Xms.setObjectName("Xms")
        self.gridLayout.addWidget(self.Xms, 1, 1, 1, 1)
        self.Xmx = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Xmx.setObjectName("Xmx")
        self.gridLayout.addWidget(self.Xmx, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.accept = QtWidgets.QPushButton(self.main_tab)
        self.accept.setGeometry(QtCore.QRect(300, 320, 75, 23))
        self.accept.setObjectName("accept")
        self.label_3 = QtWidgets.QLabel(self.main_tab)
        self.label_3.setGeometry(QtCore.QRect(10, 380, 231, 311))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("download.jpg"))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.main_tab, "")
        self.settings_tab = QtWidgets.QWidget()
        self.settings_tab.setObjectName("settings_tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.settings_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 1281, 661))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.question_window = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.question_window.setEnabled(True)
        self.question_window.setChecked(True)
        self.question_window.setObjectName("question_window")
        self.gridLayout_2.addWidget(self.question_window, 0, 0, 1, 1)
        self.hints_box = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.hints_box.setChecked(True)
        self.hints_box.setObjectName("hints_box")
        self.gridLayout_2.addWidget(self.hints_box, 1, 0, 1, 1)
        self.server_properties_settings = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.server_properties_settings.setObjectName("server_properties_settings")
        self.gridLayout_2.addWidget(self.server_properties_settings, 2, 0, 1, 1)
        self.change_core = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.change_core.setObjectName("change_core")
        self.gridLayout_2.addWidget(self.change_core, 3, 0, 1, 1)
        self.tabWidget.addTab(self.settings_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
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
        self.start.setText(_translate("MainWindow", "Запустить"))
        self.stop.setText(_translate("MainWindow", "Остановить"))
        self.label.setText(_translate("MainWindow", "Ограничение по памяти на работу(Кб)"))
        self.label_2.setText(_translate("MainWindow", "Ограничение памяти на запуска(Кб)"))
        self.accept.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main_tab), _translate("MainWindow", "Tab 1"))
        self.question_window.setText(_translate("MainWindow", "Всплывающее окно при выключении сервера"))
        self.hints_box.setText(_translate("MainWindow", "Подсказки для комманд"))
        self.server_properties_settings.setText(_translate("MainWindow", "изменить server.properties"))
        self.change_core.setText(_translate("MainWindow", "Изменить ядро сервера"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settings_tab), _translate("MainWindow", "Страница"))