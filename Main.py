from PyQt5 import QtWidgets,QtGui,Qt
import sys
import Getdata
class UI:
    def __init__(self,deger):
        app = QtWidgets.QApplication(sys.argv)
        self.window = QtWidgets.QWidget()
        self.window.setWindowTitle('Hava Durumu')
        self.window.setWindowIcon(QtGui.QIcon('icon.png'))
        self.window.setStyleSheet('background-color:khaki')
        self.window.setGeometry(800, 100, 225, 75)
        sicaklik = QtWidgets.QLabel(self.window)
        sicaklik.setStyleSheet('color:#a0522d;font-size:57px;margin-right:auto;margin-left:auto;text-align:center;')
        sicaklik.setText(deger)
        self.window.setWindowOpacity(0.5)
        self.window.show()

        sys.exit(app.exec_())






data = Getdata.data()
print(data.goster())
ui = UI(data.goster()+ "C")


