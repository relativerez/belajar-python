n=int(input('Masukkan jumlah bilangan : '))
angka=[]
for i in range(n):
    value=int(input('Masukkan angka ke'+str(i+1)+': '))
    angka.append(value)
print(angka)
print("urutan terkecil ke terbesar : ")
for i in range(len(angka)-1, 0, -1):
        for j in range(i):
            if angka[j] > angka[j+1]:
                temp = angka[j]
                angka[j] = angka[j+1]
                angka[j+1] = temp
print(angka)
print('urutan terbesar ke terkecil : ')
for i in range(len(angka)-1, 0, -1):
        for j in range(i):
            if angka[j] < angka[j+1]:
                temp = angka[j]
                angka[j] = angka[j+1]
                angka[j+1] = temp
print(angka)