import datetime

#outputnya seperti Ini
#vv = untuk kode fakultas
#ww = kode daerah asal 
#xx = tahun masuk
#yy = tahun lahir jika genap atau ganjil
#zz =  gender
#NPM 0735200001
kode_fakultas = {
  'FE': "01",
  'FH': "02",
  'FKIP': "03",
  'FSB': "04",
  'FP': "05",
  'FAPET': "06",
  'FT': "07",
  'FK': "08",
}
kode_daerah = {
  'DIB':"25",
  'DIT':"35",
  'DITA':"45",
}

loop = 1
while loop == 1:
  print ('========[Program Generate NPM]=======')
  print ('\n')
  nama = input('Masukan nama : ')
  gender = input('Masukan jenis kelamin(L/P) : ')
  if (gender == "L"):  
    kelamin = "001"  
  else:  
    kelamin = "002"
  umur = int(input('Umur : '))
  now = datetime.datetime.now()
  if ((now.year - umur) % 2 == 0):
    tahunLahir = "00"  
  else:  
    tahunLahir = "01"
  masuk = int(input('Tahun masuk : '))
  last_masuk = masuk % 100
  inputDaerah = input('Masukan daerah asal [DIB,DIT,DITA] : ')
  inputFakultas = input('Masukan fakultas [FE,FH,FKIP,FSB,FP,FAPET,FT,FK] : ')
  print('\n')
  print('==============[HASIL]==============')
  print('> Nama : ',nama)
  print('> NPM : ', kode_fakultas.get(inputFakultas),kode_daerah.get(inputDaerah),last_masuk,tahunLahir,kelamin, sep='')
  confirm = input('\nLanjut? (y/n) ')
  if confirm == 'n':
    loop = 0;""