from gui.gui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore


def fill_settings(ui: Ui_MainWindow):
    for i in range(16):
        item = QtWidgets.QListWidgetItem()
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled
        )
        ui.edit_first_pads_collection_list.addItem(item)

    for i in range(16):
        item = QtWidgets.QListWidgetItem()
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled
        )
        ui.edit_second_pads_collection_list.addItem(item)
