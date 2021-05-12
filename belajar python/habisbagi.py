def cari_faktor(bil):
  faktor = []
  for pembagi in range(1,bil+1):
    if bil % pembagi == 0: # tidak ada sisa hasil bagi
      faktor.append(pembagi)
  return faktor

bil = input('Masukkan sebuah bilangan untuk dicari faktornya: ')
bil = int(bil)
faktor = cari_faktor(bil)
print('faktor dari',bil,'adalah:',faktor)