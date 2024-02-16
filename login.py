from PyQt5.QtWidgets import *
from login_python import Ui_Form
from anapencere import MainPage

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.loginform = Ui_Form()
        self.loginform.setupUi(self)
        self.mainWindowOpener = MainPage()
        self.loginform.pushButton_giris.clicked.connect(self.GirisYap)

    def GirisYap(self):
        kull_Adi = self.loginform.lineEdit_kullaniciAdi.text()
        sifre = self.loginform.lineEdit_password.text()
        if kull_Adi == "tayfun" and sifre == "123":
            self.hide()
            self.mainWindowOpener.show()
