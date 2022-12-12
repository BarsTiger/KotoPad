from PyQt5 import QtCore
from gui.gui import Ui_MainWindow


def open_menu(ui: Ui_MainWindow) -> None:
    width = ui.menu.geometry().width()
    Ui_MainWindow.animation = QtCore.QPropertyAnimation(ui.menu, b"minimumWidth")
    Ui_MainWindow.animation.setDuration(300)
    if width == 64:
        Ui_MainWindow.animation.setStartValue(64)
        Ui_MainWindow.animation.setEndValue(200)
    else:
        Ui_MainWindow.animation.setStartValue(200)
        Ui_MainWindow.animation.setEndValue(64)
    Ui_MainWindow.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)

    Ui_MainWindow.animation.start()


def handle_menu_click(text: str, ui: Ui_MainWindow) -> None:
    index = {
        "Close menu": [lambda _: open_menu(ui), None],
        "Pads": [ui.content.setCurrentWidget, ui.pads_page],
        "Explorer": [ui.content.setCurrentWidget, ui.browser_page],
        "Collections": [ui.content.setCurrentWidget, ui.collections_page],
        "Stream": [ui.content.setCurrentWidget, ui.stream_page],
        "Collab": [ui.content.setCurrentWidget, ui.collab_page],
        "Download": [ui.content.setCurrentWidget, ui.download_page],
        "Settings": [ui.content.setCurrentWidget, ui.settings_page]
    }
    index[text][0](index[text][1])
