import time, pypresence, struct
from pypresence import *

######################-READD!!######################
# coding by larei
# Only change here.
# If there are features you do not use, you can delete the parts you want.
# btw you can come here https://discord.gg/aaYjVKC for help.
#####################-GENERAL-######################
clientID = ''  # Type your Client ID on Developer Portal.
detay = '' # Type your status.
durum = '' # Type your details.
yenilenme = '' # Type how many seconds it will be refreshed.
######################-IMAGE-######################
buyuk = '' # Type the large icon name on Developer Portal.
buyukT = ''# Type the large icon text.
kucuk = '' # Type the small icon name on Developer Portal.
kucukT = ''# Type the small icon text.
#####################-BUTTONS-######################
buton1Yazi = '' # Type the first button text.
buton1Link = '' # Type the first button link.
buton2Yazi = '' # Type the second button text.
buton2Link = '' # Type the second button link.
####################################################

RPC = Presence(clientID)
RPC.connect()
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
    print("\nDiscord must be running on the background!\n{}\n".format(hata1))
except pypresence.exceptions.InvalidID  as hata2:
    print("\nInvalid Client ID!\n{}\n".format(hata2))
except struct.error as hata3:
    print("\nInvalid Client ID!\n{}\n".format(hata3))
except pypresence.exceptions.ServerError as hata4:
    print("\nPlease make sure you entered the correct Link/Name/ID.\n{}\n".format(hata4))
