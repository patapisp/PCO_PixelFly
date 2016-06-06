__author__ = 'Polychronis Patapis'
from PyQt4 import QtGui
from QtGUI.core.pco_gui import CameraWidget
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QMainWindow()
    window.setWindowTitle('PCO.PixelFly                    -ETH Zurich- ')
    try:
        icon = QtGui.QIcon('App.ico')
        window.setWindowIcon(icon)
    except:
        pass
    pco_ui = CameraWidget(parent=None)
    pco_ui.create_gui(window)
    window.show()
    sys.exit(app.exec_())

