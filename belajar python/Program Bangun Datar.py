import os
# Clear tulisan
def screen_clear():
   # untuk mac dan linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # untuk windows
      _ = os.system('cls')

def menu():
  print('[1] Persegi panjang')
  print('[2] Segitiga')
  print('[3] Lingkaran')
  print('[4] Belah ketupat')
  print('[5] Belah ketupat')
  print('[6] Exit program')

def persegi_panjang():
  p = float(input("Masukan nilai panjang : "))
  l = float(input("Masukan nilai lebar : "))
  luas = p*l
  keliling = 2*(p*l)
  print('Luas persegi panjang = ', luas)
  print('Keliling persegi panjang = ', keliling)

def segitiga():
  t = float(input("Masukkan tinggi segitiga : "))
  a = float(input("Masukkan alas segitiga : "))
  luas = 1/2 * a * t
  print('Luas segitiga = ', luas)

def lingkaran():
  r = float(input("Masukan nilai jari-jari : "))
  luas = 3.14*r*r
  keliling = 3.14*2*r
  print('luas lingkaran = ', luas)
  print('Keliling lingkaran = ', keliling)
                
def belah_ketupat():
  d1 = float(input('Masukan nilai diagonal 1 : '))
  d2 = float(input('Masukan nilai diagonal 2 : '))
  luas = (d1*d2)/2
  print('Luas belah ketupat = ', luas)

def lingkaran():
    r = int(input("Masukan Jari-jari : "))
    luas = 3.14*(r*r)
    keliling = 2*3.14*r
    print ("Luas Lingkaran = ",luas)
    print ("Keliling Lingkaran = ",keliling)

loop = 1
choice = 0
while loop == 1:
  # fungsi untuk menampikan menu
  print ("=====[Program menghitung bangun datar]====")
  print ("\n")
  menu()
  choice = int(input('Masukkan pilihan : ')) 
  if choice == 1 :
    persegi_panjang()
  elif choice == 2 :
    segitiga()   
  elif choice == 3 :
    lingkaran()
  elif choice == 4 :
    belah_ketupat()
  elif choice == 5 :
    lingkaran()
  elif choice == 6:
    yakin = input('Ingin keluar? (y/n) ')
    if yakin == 'y':
      loop = 0
  else:
    print('maaf pilihan anda tidak ada dimenu')
  # kalau mau keluar ga usah di bersihkan
  if choice != 6:
    input('Enter untuk melanjutkan');
    screen_clear()
