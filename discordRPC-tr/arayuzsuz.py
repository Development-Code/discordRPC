import time, pypresence, struct
from pypresence import *

#####################-NOTT!!-#####################
# coding by larei
# Sadece burayı değiştirin.
# Eğer kullanmayacağınız özellikler istediğiniz kısımları silebilirsiniz.
# Ayrıca yardım için https://discord.gg/aaYjVKC gelebilirsiniz.
######################-TEMEL-######################
clientID = ''  # Client ID'nizi giriniz.
detay = '' # Detay mesajını buraya giriniz.
durum = '' # Durum mesajını buraya giriniz.
yenilenme = '' # Kaç saniyede bir yenileneceğini giriniz.
######################-GORSEL-######################
buyuk = '' # Developer Portal'a yüklediğiniz resmin ismini giriniz. Büyük olan resim bu olacak!
buyukT = ''# Resmin üstüne gelince belirecek yazıyı giriniz.
kucuk = '' # Developer Portal'a yüklediğiniz resmin ismini giriniz. Küçük olan resim bu olacak!
kucukT = ''# Resmin üstüne gelince belirecek yazıyı giriniz.
######################-BUTON-#######################
buton1Yazi = '' # İlk butonda yazan yazıyı buraya giriniz.
buton1Link = '' # İlk butonun linkini giriniz.
buton2Yazi = '' # İkinci butonda yazan yazıyı buraya giriniz.
buton2Link = '' # İlk butonun linkini giriniz.
####################################################

RPC = Presence(clientID)  # Initialize the Presence class
RPC.connect()  # Start the handshake loop
zaman = int(time.time())

try:
    while True:
        RPC.update(
            state = durum,
            details = detay,
            large_image = buyuk,
            large_text = buyukT,
            small_image = kucuk,
            small_text = kucukT,
            start = zaman,
            buttons = [{"label": buton1Yazi, "url": buton1Link}, {"label": buton2Yazi, "url": buton2Link}]
        )
        time.sleep(int(yenilenme))
except pypresence.exceptions.InvalidPipe as hata1:
    print("\nDiscord uygulamasının arka planda çalışır halde olması gerekir!\n{}\n".format(hata1))
except pypresence.exceptions.InvalidID  as hata2:
    print("\nGeçersiz Client ID!\n{}\n".format(hata2))
except struct.error as hata3:
    print("\nGeçersiz Client ID!\n{}\n".format(hata3))
except pypresence.exceptions.ServerError as hata4:
    print("\nLütfen doğru Link/İsim/ID girdiğinizden emin olunuz.\n{}\n".format(hata4))
