list_angka = [i for i in range(1, 100 )]
 
bilangan_prima = []
for i in list_angka:
    if (i==2 or i==3 or i==5 or i==7) or (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0):
        bilangan_prima.append(i)
 
print(bilangan_prima)