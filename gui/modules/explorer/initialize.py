from gui.gui import Ui_MainWindow
from PyQt5 import QtWidgets, QtCore
from modules.config import PathsConfig
from gui.modules.core import popup
import os


def fill_paths(ui: Ui_MainWindow):
    ui.first_browser_parent_dir_box.setText(PathsConfig.get().first_browser_path)
    ui.second_browser_parent_dir_box.setText(PathsConfig.get().second_browser_path)


def first_clicked(ui: Ui_MainWindow, index):
    ui.first_index = index
    ui.files_browser_listwidget_first.clear()
    try:
        ui.files_browser_listwidget_first.addItems(
            [f for f in os.listdir(ui.dir_model_first.filePath(index))
             if os.path.isfile(os.path.join(ui.dir_model_first.filePath(index), f))]
        )
    except Exception as e:
        print(e)
        popup.popup("Error", "Cannot access files in this folder")


def second_clicked(ui: Ui_MainWindow, index):
    ui.second_index = index
    ui.files_browser_listwidget_second.clear()
    try:
        ui.files_browser_listwidget_second.addItems(
            [f for f in os.listdir(ui.dir_model_second.filePath(index))
             if os.path.isfile(os.path.join(ui.dir_model_second.filePath(index), f))]
        )
    except Exception as e:
        print(e)
        popup.popup("Error", "Cannot access files in this folder")


def init_explorer(ui: Ui_MainWindow):
    fill_paths(ui)

    ui.dir_model_first = QtWidgets.QFileSystemModel()
    ui.dir_model_first.setFilter(QtCore.QDir.Filter.NoDotAndDotDot | QtCore.QDir.Filter.AllDirs)
    ui.dir_model_first.setRootPath("")
    ui.folders_browser_treeview_first.setModel(ui.dir_model_first)
    ui.folders_browser_treeview_first.setRootIndex(ui.dir_model_first.index(ui.first_browser_parent_dir_box.text()))

    ui.folders_browser_treeview_first.clicked[QtCore.QModelIndex].connect(lambda idx: first_clicked(ui, idx))

    ui.folders_browser_treeview_first.setHeaderHidden(True)
    for i in range(1, 4):
        ui.folders_browser_treeview_first.hideColumn(i)

    ui.dir_model_second = QtWidgets.QFileSystemModel()
    ui.dir_model_second.setFilter(QtCore.QDir.Filter.NoDotAndDotDot | QtCore.QDir.Filter.AllDirs)
    ui.dir_model_second.setRootPath("")
    ui.folders_browser_treeview_second.setModel(ui.dir_model_second)
    ui.folders_browser_treeview_second.setRootIndex(ui.dir_model_second.index(ui.second_browser_parent_dir_box.text()))

    ui.folders_browser_treeview_second.clicked[QtCore.QModelIndex].connect(lambda idx: second_clicked(ui, idx))

    ui.folders_browser_treeview_second.setHeaderHidden(True)
    for i in range(1, 4):
        ui.folders_browser_treeview_second.hideColumn(i)
