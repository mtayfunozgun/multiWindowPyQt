from PyQt5.QtWidgets import *
from anapencere_python import Ui_MainWindow
from urun_listele import urunListelePage
from urun_kategori import UrunKategoriPage


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainForm = Ui_MainWindow()
        self.mainForm.setupUi(self)
        self.urunlisteleform = urunListelePage()
        self.urunkategoriform = UrunKategoriPage()
        self.mainForm.action_r_n_Listele.triggered.connect(self.UrunListeleFormu)
        self.mainForm.action_r_n_Kategori_Ekle_2.triggered.connect(self.UrunKategori)
        self.mainForm.pushButton.clicked.connect(self.Ekle)

    def UrunListeleFormu(self):
        self.urunlisteleform.show()

    def UrunKategori(self):
        self.urunkategoriform.show()
    def Ekle(self):
        urun_adi = self.mainForm.lineEdit.text()
        miktar = self.mainForm.lineEdit_2.text()
