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
    print ("====[Menu]====")
    print ("1. FAKTORIAL")
    print ("2. PERMUTASI")
    print ("3. KOMBINASI")
    print ("4. exit ")

def faktorial(a) :
    hasil = 1
    for a in range (a,1,-1) :
      hasil = hasil * a
    return hasil

def permutasi(sx,tx) :
  hasil = 1
  tx = sx - tx
  for z in range (sx,tx, -1) :
    hasil = hasil * z
  return hasil

def kombinasi(bk,ck) :
  hasil1 = 1
  hasil2 = 1
  for p in range(bk,ck,-1) :
    hasil1 = hasil1 * p
    for q in range(bk-ck,1,-1) :
      hasil2 = hasil2 * q
    hasil = hasil1/(hasil2)
  return hasil

loop = 1
pilihan = 0
while loop == 1:
    menu()
    pil = int(input("Masukkan Pilihan anda : "))
    if pil == 1 :
      a = int(input("Masukkan Angka : "))
      print("Hasil Faktorial dari", a, "adalah :",faktorial(a))
    elif pil == 2:
      sx = int(input("Masukkan Angka di s : "))
      tx = int(input("Masukkan Angka di t : "))
      print("Permutasinya yaitu",permutasi(sx,tx))
    elif pil == 3:
      bk = int(input("Masukkan Angka di s : "))
      ck = int(input("Masukkan Angka di t : "))
      print("Permutasinya yaitu",kombinasi(bk,ck))
    elif pil == 4:
      yakin = input('Ingin keluar? (y/n) ')
      if yakin == 'y':
        loop = 0
    else:
      print('error')
    if pil != 4:
      input('Enter untuk melanjutkan');
      screen_clear()