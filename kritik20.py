from pypresence import Presence
import time, random

client_id = '805415115938594817'#------------------| Application Client ID
RPC = Presence(client_id)
RPC.connect()

print("Lets go!")

komutlar = ["State", "Details", "Large Text", "Small Text", "Party Size", "Button1", "Button2"]

state_ = "🎲 Zar atıyor: "
details_ = "📚 Kitapların tozunu alıyor..."
large_image_ = "k20"
large_text_ = "Kritik20"
button1 = {"label": "İnternet Adresi", "url": "https://kritik20.com"}
button2 = {"label": "Discord Adresi", "url": "https://discord.gg/VNWCr7DYha"}
small_image_ = None
small_text_ = None
zar = random.SystemRandom().randint(0, 20)
party_size_ = [zar,20]
party_id_ = None
join_ = None
enter = True
while True:
    if enter == True:
        değiştirme_soru = input("Değiştirmek istediğiniz bir şey var mı?\n")
        if değiştirme_soru.lower() in ("var", "evet", "yes", "e"):
            while True:
                komut_join = "\n - ".join(komutlar)
                soru = input(f"""Lütfen değiştirmek istediğiniz şeyi yazın, yoksa "kaydet" diyerek devam edebilirsiniz:\n Komut Listesi\n - {komut_join} \n""")
                soru = soru.strip()
                try:
                    if soru.lower() == "kaydet":
                        break

                    if soru.lower() == "state":
                        value = input("Değer Girin: ")
                        state_ = str(value)

                    elif soru.lower() == "details":
                        value = input("Değer Girin: ")
                        details_ = str(value)

                    elif soru.lower() == "large text":
                        value = input("Değer Girin: ")
                        large_text_ = str(value)

                    elif soru.lower() == "small text":
                        value = input("Değer Girin: ")
                        small_text_ = str(value)

                    elif soru.lower() == "party size":
                        value1 = input("Şu Anki Parti Boyutunu Girin (0'dan büyük olmalı.): ")
                        if int(value1) == 0:
                            print("Anlık parti sayısı 0 olamaz, bu yüzden 1 verildi.")
                            value1 = "1"
                        value2 = input("Maksimum Parti Boyutunu Girin: ")
                        party_size_ = [int(value1), int(value2)]

                    elif soru.lower() == "party id":
                        value = input("Değer Girin: ")
                        if len(value) < 3:
                            print("Lütfen üçten küçük bir party id girmeyin, tekrar deneyiniz.")
                            continue
                        party_id_ = str(value)

                    elif soru.lower() == "button1":
                        value1 = input("Butonun üstündeki yazıyı girin: ")
                        value2 = input("Adres girin (http/https): ")
                        button1 = {"label": str(value1), "url": str(value2)}

                    elif soru.lower() == "button2":
                        value1 = input("Butonun üstündeki yazıyı girin: ")
                        value2 = input("Adres girin (http/https): ")
                        button2 = {"label": str(value1), "url": str(value2)}

                    elif soru.lower() == "liste":
                        print(f"Komut Listesi: {komut_join}")
                        continue
                    else:
                        print("Girdiğiniz komut, komutlar listemizde bulunamadı tekrar deneyin.")
                        continue
                except Exception as e:
                    print(f"Bir hata çıktı: {e}")

        elif değiştirme_soru.lower() in ("hayır", "h", "n", "no", "yok"):
            print("Devam ediliyor.")
            enter = False
        else:
            print("Girdiğiniz komut anlaşılamadı, lütfen tekrar deneyin.")
            continue
    
    try:
        (RPC.update(state = state_,                             #--------------| Durum
                    details = details_,                         #--------------| Detaylar
                    large_image = large_image_,                 #-----------| Büyük Resim
                    large_text = large_text_,                   #----| Büyük Resmin Yazısı
                    small_image = small_image_,                 #--------------| Küçük Resim
                    small_text = small_text_,                   #--| Küçük Resmin Yazısı
                    party_size = party_size_,                   #--------------------| Parti Boyutu
                    party_id = party_id_,                       #------------------| Parti Idsi
                    start = None,                         #--------------------| Zaman için başlangıç zamanı
                    end = None,                           #----------------------| Zaman için bitiş zamanı
                    buttons = [button1, button2]
                    # join = join_
                    ))                              #--------------------| Join idsi
    except Exception as error:
        print("Lütfen hatasız bir şekilde 60 saniye içerisinde tekrar deneyin.", "Hata:", error)
    time.sleep(30*60)
    party_size_=[random.SystemRandom().randint(0,20), 20]
