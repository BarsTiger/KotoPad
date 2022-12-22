from gui.gui import Ui_MainWindow
from modules.config import PathsConfig
from PyQt5 import QtWidgets, QtCore
from gui.modules.collections.collections import update_collections_lw


def on_path_setting_collection_change(ui: Ui_MainWindow):
    all_collections = list(
        filter(
            lambda a: a != "",
            list(
                map(
                    lambda x: x.text(),
                    [ui.edit_collections_paths.item(x) for x in range(ui.edit_collections_paths.count())]
                )
            )
        )
    )
    PathsConfig.update("collections_list", all_collections)
    fill_collections_paths(ui)
    update_collections_lw(ui)


def fill_collections_paths(ui: Ui_MainWindow):
    ui.edit_collections_paths.clear()
    collections = PathsConfig.get().collections_list
    for i in range(420):
        item = QtWidgets.QListWidgetItem()
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled
        )
        item.setText(collections[i] if i < len(collections) else "")

        ui.edit_collections_paths.addItem(item)
