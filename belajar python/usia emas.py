import datetime
a = datetime.datetime.now()

nama = str(input("masukan nama anda : "))
umur = int(input("masukan umur anda : "))
tahunlahir = a.year - umur 
fut = tahunlahir + 50
umurnanti= fut - tahunlahir
print("nama anda ",nama)
print("anda berusia ",umur)
print("pada tahun",fut,"umur anda ",umurnanti)