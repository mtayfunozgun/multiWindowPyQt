from PyQt5.QtWidgets import *
from urun_kategori_python import Ui_Form


class UrunKategoriPage(QWidget):
    def __init__(self):
        super().__init__()
        self.kategoriForm = Ui_Form()
        self.kategoriForm.setupUi(self)
