from gui.modules.collections.initialize import fill_collections_paths, on_path_setting_collection_change
from gui.modules.collections.collections import *


def register_handlers(ui: Ui_MainWindow, p: Player):
    fill_collections_paths(ui)
    update_collections_lw(ui)

    ui.collections_page_tabs.currentChanged.connect(lambda: on_path_setting_collection_change(ui))
    ui.collections_listwidget.itemClicked.connect(lambda: on_collection_click(ui))
    ui.this_collection_listwidget.itemDoubleClicked.connect(lambda: on_collection_item_double(ui, p))
