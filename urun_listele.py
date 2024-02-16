from PyQt5.QtWidgets import *
from urunListele_python import Ui_Form



class urunListelePage(QWidget):
    def __init__(self):
        super().__init__()
        self.urunListeleForm = Ui_Form()
        self.urunListeleForm.setupUi(self)

