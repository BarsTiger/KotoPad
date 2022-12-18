from gui.gui import Ui_MainWindow
from modules.config import PathsConfig
from modules.player.player import Player
from PyQt5.QtWidgets import QFileDialog
import os


def register_handlers(ui: Ui_MainWindow, p: Player):
    ui.first_browser_parent_dir_box.textChanged.connect(
        lambda: (
            ui.folders_browser_treeview_first.setRootIndex(
                ui.dir_model_first.index(ui.first_browser_parent_dir_box.text())
            ),
            PathsConfig.update("first_browser_path", ui.first_browser_parent_dir_box.text())
        )
    )

    ui.second_browser_parent_dir_box.textChanged.connect(
        lambda: (
            ui.folders_browser_treeview_second.setRootIndex(
                ui.dir_model_second.index(ui.second_browser_parent_dir_box.text())
            ),
            PathsConfig.update("second_browser_path", ui.second_browser_parent_dir_box.text())
        )
    )

    ui.files_browser_listwidget_first.itemDoubleClicked.connect(
        lambda: (
            p.set_media(
                os.path.join(
                    ui.dir_model_first.filePath(ui.first_index),
                    ui.files_browser_listwidget_first.currentItem().text()
                )
            ),
            p.play(ui)
        )
    )

    ui.files_browser_listwidget_second.itemDoubleClicked.connect(
        lambda: (
            p.set_media(
                os.path.join(
                    ui.dir_model_second.filePath(ui.second_index),
                    ui.files_browser_listwidget_second.currentItem().text()
                )
            ),
            p.play(ui)
        )
    )

    ui.first_browser_parent_dir_button.clicked.connect(
        lambda: ui.first_browser_parent_dir_box.setText(
            QFileDialog.getExistingDirectory(caption="Select root directory for first browser")
        )
    )

    ui.second_browser_parent_dir_button.clicked.connect(
        lambda: ui.second_browser_parent_dir_box.setText(
            QFileDialog.getExistingDirectory(caption="Select root directory for second browser")
        )
    )
