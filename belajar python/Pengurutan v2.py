def terkecil(array):
    n = len(array) # jumlah list
    # perulangan pertama
    for i in range(n): 
        # perulangan kedua
        for j in range(n - i - 1):
            # bandingkan masing" elemen
            if array[j] > array[j + 1]:
                # jika lebih besar, tukar.
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
def terbesar(array):
    n = len(array) # jumlah list
    # perulangan pertama
    for i in range(n): 
        # perulangan kedua
        for j in range(n - i - 1):
            # bandingkan masing" elemen
            if array[j] < array[j + 1]:
                # jika lebih kecil, tukar.
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
    
#inti program
n = int(input("masukan jumlah angka untuk diurutkan: "))

angka = []

for i in range(n):
    nilai = int(input("masukkan angka ke-" + str(i+1) + ': '))
    angka.append(nilai)
print("urutan awal: ",angka)
print('terkecil ke terbesar')
print(terkecil(angka))
print("terbesar ke terkecil")
print(terbesar(angka))