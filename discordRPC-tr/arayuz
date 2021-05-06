import pypresence, time, random, sys, os, struct, webbrowser
from pypresence import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.gui()
    def gui(self):
# Widgetların Tanımlanması
        grup1 = QGroupBox("Genel")
        self.idGiris = QLineEdit()
        self.durumGiris = QLineEdit()
        self.detayGiris = QLineEdit()

        grup2 = QGroupBox("Görsel")
        self.buyukResim = QLineEdit()
        self.buyukResimT = QLineEdit()
        self.kucukResim = QLineEdit()
        self.kucukResimT = QLineEdit()

        grup3 = QGroupBox("Butonlar")
        self.buton1yazi = QLineEdit()
        self.buton1link = QLineEdit()
        self.buton2yazi = QLineEdit()
        self.buton2link = QLineEdit()

        grup4 = QGroupBox("Ek")
        self.bassure = QCheckBox("Başlatma süresini göster.")
        self.buton1 = QPushButton("Başlat")
        self.buton2 = QPushButton("Durdur")
        self.kaydet = QPushButton("Ayarları Kaydet")
        self.aktar = QPushButton("Ayarları İçe Aktar")

        menu = QGroupBox("İletişim")
        self.github = QPushButton("GitHub")
        self.discord = QPushButton("Discord")

# Widgetlerin Özelleştirilmesi
        self.idGiris.setPlaceholderText("Client ID giriniz.")
        self.durumGiris.setPlaceholderText("Durum mesajı giriniz.")
        self.detayGiris.setPlaceholderText("Detay mesajı giriniz.")

        self.buyukResim.setPlaceholderText("Büyük resmin ismini giriniz.")
        self.buyukResimT.setPlaceholderText("Büyük resmin yazısını giriniz.")
        self.kucukResim.setPlaceholderText("Küçük resmin ismini giriniz.")
        self.kucukResimT.setPlaceholderText("Küçük resmin yazısını giriniz.")

        self.buton1yazi.setPlaceholderText("Birinci butonun yazısını giriniz.")
        self.buton1link.setPlaceholderText("Birinci butonun linkini giriniz.")
        self.buton2yazi.setPlaceholderText("İkinci butonun yazısını giriniz.")
        self.buton2link.setPlaceholderText("İkinci butonun linkini giriniz.")

        self.buton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.buton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.kaydet.setCursor(QCursor(Qt.PointingHandCursor))
        self.aktar.setCursor(QCursor(Qt.PointingHandCursor))
        self.github.setCursor(QCursor(Qt.PointingHandCursor))
        self.discord.setCursor(QCursor(Qt.PointingHandCursor))

        self.github.setObjectName('gh')
        self.discord.setObjectName('dc')

        self.setStyleSheet(open("style.qss", "r").read())

# Horizontal, Vertical ve GroupBoxların Ayarlanması
        gruplar = QVBoxLayout()
        gruplar.addWidget(menu)
        gruplar.addWidget(grup1)
        gruplar.addWidget(grup2)
        gruplar.addWidget(grup3)
        gruplar.addWidget(grup4)
        gruplar.addStretch()
        gruplar.addWidget(self.buton1)
        gruplar.addWidget(self.buton2)

        menub = QHBoxLayout()
        menub.addWidget(self.github)
        menub.addWidget(self.discord)
        menu.setLayout(menub)

        g1 = QVBoxLayout()
        g1.addWidget(self.idGiris)
        g1.addWidget(self.detayGiris)
        g1.addWidget(self.durumGiris)
        grup1.setLayout(g1)

        g21 = QHBoxLayout()
        grup2.setLayout(g21)

        g22 = QVBoxLayout()
        g22.addWidget(self.buyukResim)
        g22.addWidget(self.buyukResimT)
        g21.addLayout(g22)

        g23 = QVBoxLayout()
        g23.addWidget(self.kucukResim)
        g23.addWidget(self.kucukResimT)
        g21.addLayout(g23)
       
        g31 = QHBoxLayout()
        grup3.setLayout(g31)

        g32 = QVBoxLayout()
        g32.addWidget(self.buton1yazi)
        g32.addWidget(self.buton1link)
        g31.addLayout(g32)

        g33 = QVBoxLayout()
        g33.addWidget(self.buton2yazi)
        g33.addWidget(self.buton2link)
        g31.addLayout(g33)

        g4 = QVBoxLayout()
        g4.addWidget(self.bassure)
        g4.addWidget(self.kaydet)
        g4.addWidget(self.aktar)
        grup4.setLayout(g4)

# Sinyaller
        self.buton1.clicked.connect(self.baslama)
        self.buton2.clicked.connect(self.durdur)
        self.kaydet.clicked.connect(self.kaydetme)
        self.aktar.clicked.connect(self.aktarma)
        self.github.clicked.connect(self.yonlendir)
        self.discord.clicked.connect(self.yonlendir2)

# Ana Layout Belirleme ve Arayüzün Görünür Olması
        self.setLayout(gruplar)
        self.show()

# Fonksiyonlar
    def kaydetme(self):
        try:
            dosya = QFileDialog.getSaveFileName(self, "Ayarları Kaydet", "rpc", ".larei(*.larei)", os.getenv("Desktop"))
            with open(dosya[0], "w", encoding="utf-8") as file:
                file.write("{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.idGiris.text(), self.detayGiris.text(), self.durumGiris.text(), self.buyukResim.text(), self.buyukResimT.text(), self.kucukResim.text(), self.kucukResimT.text(), self.buton1yazi.text(), self.buton1link.text(), self.buton2yazi.text(), self.buton2link.text(), self.bassure.isChecked()))
        except FileNotFoundError:
            pass

    def aktarma(self):
        try:
            dosya = QFileDialog.getOpenFileName(self, "Ayarları İçe Aktar", "rpc", ".larei(*.larei)", os.getenv("Desktop"))
            with open(dosya[0], "r", encoding="utf-8") as file:
                self.idGiris.setText(file.readline())
                self.detayGiris.setText(file.readline())
                self.durumGiris.setText(file.readline())
                self.buyukResim.setText(file.readline())
                self.buyukResimT.setText(file.readline())
                self.kucukResim.setText(file.readline())
                self.kucukResimT.setText(file.readline())
                self.buton1yazi.setText(file.readline())
                self.buton1link.setText(file.readline())
                self.buton2yazi.setText(file.readline())
                self.buton2link.setText(file.readline())
                self.bassure.setChecked(bool(file.readline()))
        except FileNotFoundError:
            pass

    def baslama(self):
        kont = self.bassure.checkState()
        if kont == 2:
            if self.idGiris.text() == "" or self.detayGiris.text() == "" or self.durumGiris.text() == "" or self.buyukResim.text() == "" or self.buyukResimT.text() == "" or self.kucukResim.text() == "" or self.kucukResimT.text() == "" or self.buton1yazi.text() == "" or self.buton1link.text() == "" or self.buton2yazi.text() == "" or self.buton2link.text() == "":
                QMessageBox.critical(self, "Hata", "Hiç bir alan boş bırakılamaz!")
            else:
                try:
                    zaman = int(time.time())
                    RPC = Presence(self.idGiris.text())
                    RPC.connect()
                    RPC.update(
                        state = self.durumGiris.text(),
                        details = self.detayGiris.text(),
                        large_image = self.buyukResim.text(),
                        large_text = self.buyukResimT.text(),
                        small_image = self.kucukResim.text(),
                        small_text = self.kucukResimT.text(),
                        start = zaman,
                        buttons = [{"label": self.buton1yazi.text(), "url": self.buton1link.text()}, {"label": self.buton2yazi.text(), "url": self.buton2link.text()}]
                    )
                except pypresence.exceptions.InvalidPipe as hata1:
                    QMessageBox.critical(self, "Hata", "Discord uygulamasının arka planda çalışır halde olması gerekir!\n{}".format(hata1))
                except pypresence.exceptions.InvalidID  as hata2:
                    QMessageBox.critical(self, "Hata", "Geçersiz Client ID!\n{}".format(hata2))
                except struct.error as hata3:
                    QMessageBox.critical(self, "Hata", "Geçersiz Client ID!\n{}".format(hata3))
                except pypresence.exceptions.ServerError as hata4:
                    QMessageBox.critical(self, "Hata", "Lütfen doğru Link/İsim/ID girdiğinizden emin olunuz.\n{}".format(hata4))
        else:
            if self.idGiris.text() == "" or self.detayGiris.text() == "" or self.durumGiris.text() == "" or self.buyukResim.text() == "" or self.buyukResimT.text() == "" or self.kucukResim.text() == "" or self.kucukResimT.text() == "" or self.buton1yazi.text() == "" or self.buton1link.text() == "" or self.buton2yazi.text() == "" or self.buton2link.text() == "":
                QMessageBox.critical(self, "Hata", "Hiç bir alan boş bırakılamaz!")
            else:
                try:
                    zaman = int(time.time())
                    RPC = Presence(self.idGiris.text())
                    RPC.connect()
                    RPC.update(
                        state = self.durumGiris.text(),
                        details = self.detayGiris.text(),
                        large_image = self.buyukResim.text(),
                        large_text = self.buyukResimT.text(),
                        small_image = self.kucukResim.text(),
                        small_text = self.kucukResimT.text(),
                        buttons = [{"label": self.buton1yazi.text(), "url": self.buton1link.text()}, {"label": self.buton2yazi.text(), "url": self.buton2link.text()}]
                    )
                except pypresence.exceptions.InvalidPipe as hata1:
                    QMessageBox.critical(self, "Hata", "Discord uygulamasının arka planda çalışır halde olması gerekir!\n{}".format(hata1))
                except pypresence.exceptions.InvalidID  as hata2:
                    QMessageBox.critical(self, "Hata", "Geçersiz Client ID!\n{}".format(hata2))
                except struct.error as hata3:
                    QMessageBox.critical(self, "Hata", "Geçersiz Client ID!\n{}".format(hata3))
                except pypresence.exceptions.ServerError as hata4:
                    QMessageBox.critical(self, "Hata", "Lütfen doğru Link/İsim/ID girdiğinizden emin olunuz.\n{}".format(hata4))

    def durdur(self):
        QCoreApplication.quit()
        status = QProcess.startDetached(sys.executable, sys.argv)

    def yonlendir(self):
        webbrowser.open_new_tab("https://github.com/Lareithen")
    def yonlendir2(self):
        webbrowser.open_new_tab("https://discord.com/invite/aaYjVKC")

obje = QApplication(sys.argv)
pencere = Pencere()
pencere.setWindowTitle("Discord RPC by larei")
pencere.setFixedSize(400,550)
sys.exit(obje.exec())

# larei was here
