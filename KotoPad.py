import sys
from PyQt5 import QtWidgets
from gui.gui import Ui_MainWindow
from gui.modules.initialize import setup_ui


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
setup_ui.on_load(ui, MainWindow)

MainWindow.show()

sys.exit(app.exec_())
