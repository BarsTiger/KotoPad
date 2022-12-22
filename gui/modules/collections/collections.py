from gui.gui import Ui_MainWindow
from modules.config import PathsConfig
import os
from gui.modules.core import popup
from modules.player.player import Player


def update_collections_lw(ui: Ui_MainWindow):
    ui.all_collections_list = list()
    ui.collections_listwidget.clear()

    for item in PathsConfig.get().collections_list:
        ui.all_collections_list.append([item.replace("\\", "/").split("/")[-1], item])
        ui.collections_listwidget.addItem(item.replace("\\", "/").split("/")[-1])


def on_collection_click(ui: Ui_MainWindow):
    ui.this_collection_listwidget.clear()
    try:
        ui.this_collection_listwidget.addItems(
            [f for f in os.listdir(
                ui.all_collections_list[ui.collections_listwidget.currentRow()][1]
            )
             if os.path.isfile(os.path.join(ui.all_collections_list[ui.collections_listwidget.currentRow()][1], f))]
        )
    except Exception as e:
        print(e)
        popup.popup("Error", "Cannot access files in this folder")


def on_collection_item_double(ui: Ui_MainWindow, p: Player):
    p.set_media(os.path.join(
        os.path.join(ui.all_collections_list[ui.collections_listwidget.currentRow()][1],
                     ui.this_collection_listwidget.currentItem().text())
    ))
    p.play(ui)
