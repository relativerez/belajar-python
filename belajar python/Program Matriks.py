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
  print('menu matriks :')
  print('1. penjumlahan matriks')
  print('2. pengurangan matriks')
  print('3. perkalian matriks')
  print('4. exit program')

def buat_matriks(rows, columns):
  arr = []
  for x in range(rows):
    a = []
    for y in range(columns):
      i = input('['+str(x)+']['+str(y)+'] : ')
      a.append(int(i))
    arr.append(a)
  
  return arr

def print_matriks(rows, columns, matriks):
  for x in range(rows):
    for y in range(columns):
      print(matriks[x][y], end = " ")
    print('')

def buat_dua_matriks(rows, columns):
  print('=========[MAT1]=========')
  mat1 = buat_matriks(rows, columns)
  print('------------------------')
  print_matriks(rows, columns, mat1)
  
  print('=========[MAT2]=========')
  mat2 = buat_matriks(rows, columns)
  print('------------------------')
  print_matriks(rows, columns, mat2)
  
  return [mat1, mat2]

def penjumlahan_matriks():
  cx = int(input('Baris : '));
  cy = int(input('kolom : '));

  mm = buat_dua_matriks(cx, cy);

  print('=========[HASIL]=========')
  res = []
  for x in range(cx):
    for y in range(cy):
      print (mm[0][x][y] + mm[1][x][y], end=' ')
    print('')

def pengurangan():
  cx = int(input('Baris : '));
  cy = int(input('kolom : '));

  mm = buat_dua_matriks(cx, cy);

  print('=========[HASIL]=========')
  res = []
  for x in range(cx):
    for y in range(cy):
      print (mm[0][x][y] - mm[1][x][y], end=' ')
    print('')

def perkalian():
  cx = int(input('Baris : '));
  cy = int(input('kolom : '));

  mm = buat_dua_matriks(cx, cy);

  print('=========[HASIL]=========')
  res = []
  for x in range(cx):
    r = []
    for y in range(cy):
      total = 0
      for z in range(cx):
        total = total + (mm[0][x][z] * mm[1][z][y])
      r.append(total)
    res.append(r)
  
  print_matriks(cx, cy, res)

loop = 1
pilihan = 0
while loop == 1:
  menu()
  pilihan = int(input('masukan pilihan? '))
  if pilihan == 1 :
    penjumlahan_matriks()
  elif pilihan == 2 :
    pengurangan() 
  elif pilihan == 3 :
    perkalian()  
  elif pilihan == 4:
    yakin = input('Ingin keluar? (y/n) ')
    if yakin == 'y':
      loop = 0
  else:
    print('maaf pilihan anda tidak ada dimenu')
    # kalau mau keluar ga usah di bersihkan
  if pilihan != 4:
    input('Enter untuk melanjutkan');
    screen_clear()