def menu():
    print("-----[Program Statistika]------")
    print("1.input data")
    print("2.tampilkan data")
    print("3.operasi statistika data")
    print("4.exit")

list = []

#function buat menginput data dari user
def input_user():
    n=int(input("Masukkan jumlah data : "))
    for i in range(n):
        nilai=int(input('Masukkan data ke-'+str(i+1)+': '))
        list.append(nilai)
    return n,list,nilai

#function buat menampilkan data dari user
def user_data():
    if(len(list)<=0):
        print("Belum ada data yang di input.Silahkan iput terlebih dahulu :) ")
    else :
        for i in range(len(list)-1, 0, -1):
            for j in range(i):
                if list[j] > list[j+1]:
                    temp = list[j]
                    list[j] = list[j+1]
                    list[j+1] = temp
        print(list)
#function buat operasi statistika
def operasi_statistika():
    #nilai awal
    nilai_rata_rata = 0
    jumlah_nilai = 0
    nilai_terkecil = list[0] 
    nilai_terbesar = list[0]
    kemunculan = {}
    frekuensi={}
    for nilai in list:
        jumlah_nilai = jumlah_nilai + nilai
        #nilai terbesar code
        if nilai_terbesar < nilai: 
            nilai_terbesar = nilai 
        #nilai terkecil code
        if nilai_terkecil > nilai:
            nilai_terkecil = nilai
    #nilai rata2 code
    nilai_rata_rata = jumlah_nilai /len(list)
    #median code
    data = list
    n = len(list)
    if n == 0:
        None
    if n % 2 == 1:
        median=data[n // 2]
    else:
        i = n // 2
        median = (data[i - 1] + data[i]) / 2
    # modus code
    for nilai in list:
      if nilai in kemunculan:
        kemunculan[nilai] += 1
      else:
        kemunculan[nilai] = 1
    bilangan_terbesar = list[0] 
    for nilai in kemunculan.keys():
        jumlah = kemunculan[nilai]

    if jumlah > kemunculan[bilangan_terbesar]:
        bilangan_terbesar = nilai
    # frekuensi code
    for nilai in list: 
        if nilai in frekuensi:
            frekuensi[nilai] += 1
        else:         
            frekuensi[nilai] = 1
    

    print('Median pada list: ',median)
    print('modus pada list',bilangan_terbesar)
    print('rata-rata nilai pada list: ',nilai_rata_rata)
    print('nilai terbesar pada list: ',nilai_terbesar)
    print('nilai terkecil pada list: ',nilai_terkecil)
    print('frekuensi pada list: ',frekuensi)


    
loop = 1
pilihan = 0
while loop == 1:
#program utama
  menu()
  pilihan = int(input('masukan pilihan: '))
  if pilihan == 1 :
    input_user()
  elif pilihan == 2 :
    user_data()
  elif pilihan == 3 :
    operasi_statistika()
  elif pilihan == 4 :
    yakin = input('Ingin keluar? (y/n) ')
    if yakin == 'y':
      loop = 0
  else:
    print('maaf pilihan tidak ada')

