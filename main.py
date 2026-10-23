print ("Bilgi Yarismasina Hosgeldin!")

isim = input("Adin ne ? ")

puan = 0

print("Turkiyenin baskenti neresidir ? ")

cevap =input("Cevabin:").strip().lower()

if cevap =="ankara":
    print("Dogru cevap!")

    puan += 10

else:
    print("Yanlis Dogru cevap : ankara")

print(f"{isim}, toplam puanin:{puan}")