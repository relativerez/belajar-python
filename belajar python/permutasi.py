n = int(input("masukan angka n: "))
r = int(input("masukan angka r: "))
def faktorial(x):
    if x == 1 :
        return 1
    elif x == 0:
        return 1
    else:
        return(x * faktorial(x-1))
    
permutasi = (faktorial(n)/faktorial(n-r))
print("permutasi adalah",permutasi)