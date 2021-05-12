n = int(input('masukan jumlah baris [bilangan ganjil] = '))

if n % 2 == 0:
  print('salah input kembali masukan dengan bilangan ganjil')
else:
  for x in range(n):
    for y in range(n):
      # kotak
      if x == 0 or x == n - 1 or y == 0 or y == n - 1:
        print('*', end =' ')
      # x
      elif y == n - x - 1 or x == y:
        print('*', end =' ')
      # # plus
      elif y*2 == n - 1 or x*2 == n - 1:
        print('*', end =' ')
      else:
        print(' ', end =' ')
    print()