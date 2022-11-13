import os
from modules.padslist import Pads
from gui.gui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow


def fill_pads(ui: Ui_MainWindow, MainWindow: QMainWindow):
    ui.first_pads_dict = dict()
    ui.second_pads_dict = dict()

    first_pads_list = \
        [ui.edit_first_pads_collection_list.item(x).text() for x in range(ui.edit_first_pads_collection_list.count())]

    for i in range(len(first_pads_list)):
        item = first_pads_list[i]
        if item == '':
            continue
        ui.first_pads_dict[os.path.split(item)[-1]] = item
        button = QtWidgets.QPushButton()
        button.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                                   QtWidgets.QSizePolicy.Expanding))
        button.setText(os.path.split(item)[-1] if os.path.exists(item) else "File doesn't exist")
        button.clicked.connect(lambda: print(ui.first_pads_dict[MainWindow.sender().text()]
                                             if MainWindow.sender().text() != "File doesn't exist" else None))
        print('First: ', ui.first_pads_dict)
        Pads.update("first_pads", ui.first_pads_dict)
        ui.pads_collection_1_lay.addWidget(button, i // 4, i % 4)

    second_pads_list = \
        [ui.edit_second_pads_collection_list.item(x).text() for x in range(ui.edit_second_pads_collection_list.count())]

    for i in range(len(second_pads_list)):
        item = second_pads_list[i]
        if item == '':
            continue
        ui.second_pads_dict[os.path.split(item)[-1]] = item
        button = QtWidgets.QPushButton()
        button.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                                   QtWidgets.QSizePolicy.Expanding))
        button.setText(os.path.split(item)[-1] if os.path.exists(item) else "File doesn't exist")
        button.clicked.connect(lambda: print(ui.second_pads_dict[MainWindow.sender().text()]
                                             if MainWindow.sender().text() != "File doesn't exist" else None))
        print('Second', ui.second_pads_dict)
        Pads.update("second_pads", ui.second_pads_dict)
        ui.pads_collection_2_lay.addWidget(button, i // 4, i % 4)
