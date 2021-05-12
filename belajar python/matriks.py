print('------[penjumlahan matriks]--------')
print("\n")

baris_1 = int(input("masukan jumlah baris: "))
kolom_1 = int(input("masukan jumlah kolom: "))

mat1 = []
for i in range(baris_1):
    baris_1 = []
    for j in range(kolom_1):
        nilai_1 = int(input("nilai baris"+ str(i+1)+(", kolom ")+ str(j+1)+': '))
        baris_1.append(nilai_1)
    mat1.append(baris_1)
print("-------[mat1]---------")  
for baris_1 in mat1:
    print(baris_1)

baris_2 = int(input("masukan jumlah baris: "))
kolom_2 = int(input("masukan jumlah kolom: "))

mat2 = []
for i in range(baris_2):
    baris_2 = []
    for j in range(kolom_2):
        nilai_2 = int(input("nilai baris"+ str(i+1)+(", kolom ")+ str(j+1)+': '))
        baris_2.append(nilai_2)
    mat2.append(baris_2)

print("-------[mat2]---------")  
for baris_2 in mat1:
    print(baris_2)

print("-------[Hasil Penjumlahan]---------")  
for x in range(0, len(mat1)):
    for y in range(0, len(mat2[0])):
        print ([mat1[x][y] + mat2[x][y]], end=''),
    print()