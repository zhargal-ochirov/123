# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'regognition.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import json

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog
import functions
from main import Ui_Results


class Ui_MainWindow(QDialog):
    # def open_window(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_Results()
    #     self.ui.setupUi(self.window)
    #     self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 390)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 41))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.file_dialog)
        self.path_session = ''


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 101, 41))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 80, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setEnabled(False)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 141, 41))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 140, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 190, 141, 41))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 200, 241, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['Евклидово расстояние', 'Манхэттеновское расстояние', 'Евклидово расстояние + частотность',
                                'Манхэттеновское расстояние + частотность', 'Метод опорных векторов'])
        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(80, 250, 321, 28))
        # self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 300, 321, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton_3.clicked.connect(self.recognize)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Путь к файлу"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать файл"))
        self.label_2.setText(_translate("MainWindow", "Сессий в файле"))
        self.label_3.setText(_translate("MainWindow", "Выбрать номер сессий"))
        self.label_4.setText(_translate("MainWindow", "Метод распознования"))
        # self.pushButton_2.setText(_translate("MainWindow", "Точность методов"))
        self.pushButton_3.setText(_translate("MainWindow", "РАСПОЗНАТЬ"))

    def file_dialog(self):
        path = QFileDialog.getOpenFileName()
        with open(path[0], encoding='utf-8') as json_file:
            data = json.load(json_file)
            session_in_the_file = len(data)
        self.lineEdit.setText(str(session_in_the_file))
        self.path_session = path[0]
        # return path[0]

    def recognize(self):
        patterns_users, expected_values = functions.patterns()
        session_users, session_letters = functions.sessions(self.path_session)
        frequency = functions.frequency()
        n_session = int(self.lineEdit_2.text()) - 1
        n_session = int(n_session)
        # print(type(n_session))

        if self.comboBox.currentText() == 'Евклидово расстояние':
            result = functions.Eucliadian_dist(expected_values, session_letters, n_session)
            dict_result = dict(zip(patterns_users, result))
            dict_result_sort = (dict(sorted(dict_result.items(), key=lambda x: x[1])))
        elif self.comboBox.currentText() == 'Евклидово расстояние + частотность':
            result = functions.Eucliadian_freq_dist(expected_values, session_letters, n_session, frequency)
            dict_result = dict(zip(patterns_users, result))
            dict_result_sort = (dict(sorted(dict_result.items(), key=lambda x: x[1])))
        elif self.comboBox.currentText() == 'Манхэттеновское расстояние':
            result = functions.Manhattan_dist(expected_values, session_letters, n_session)
            dict_result = dict(zip(patterns_users, result))
            dict_result_sort = (dict(sorted(dict_result.items(), key=lambda x: x[1])))
        elif self.comboBox.currentText() == 'Манхэттеновское расстояние + частотность':
            result = functions.Manhattan_freq_dist(expected_values, session_letters, n_session, frequency)
            dict_result = dict(zip(patterns_users, result))
            dict_result_sort = (dict(sorted(dict_result.items(), key=lambda x: x[1])))
        elif self.comboBox.currentText() == 'Метод опорных векторов':
            result = functions.SVM(expected_values, patterns_users, session_letters, n_session)
            dict_result = dict(zip(patterns_users, result))
            dict_result_sort = (dict(sorted(dict_result.items(), key=lambda x: x[1])))
        else:
            print(self.comboBox.currentText())
            dict_result_sort = None

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Results()
        if self.comboBox.currentText() != 'метод опорных векторов':
            self.ui.dict_sort = dict_result_sort
            self.ui.setupUi(self.window)
            self.window.show()

            self.ui.label_2.setText(self.ui.label_2.text()+' '+self.comboBox.currentText())
        if result[0] == session_users[n_session]:
            self.ui.lineEdit.setText(session_users[n_session])
        elif list(dict_result_sort.keys())[0] == session_users[n_session]:
            self.ui.lineEdit.setText(session_users[n_session])
        else:
            self.ui.lineEdit.setText('unknown')



        # print(dict_result_sort)
        # print(n_session)
        # print(*patterns_users)
        # # print(len(expected_values))
        #
        # print(len(session_users))
        # print('Распознать')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
