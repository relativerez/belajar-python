x = int(input("masukan nilai untuk difaktorialkan: "))
def faktorial(x):
    if x  == 1 :
        return 1
    else:
        return(x * faktorial(x-1))

print("faktorial dari ",x," adalah",faktorial(x))