#long code
def Palindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 

s = str(input("masukan kata: "))
ans = Palindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")

#short code
# x = str(input("masukan kata: "))
 
# w = ""
# for i in x:
#     w = i + w
 
# if (x == w):
#     print("Yes")
# else:
#     print("No")
   