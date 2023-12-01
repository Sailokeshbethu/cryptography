n=str(input("enter the cipher text:"))
print("cipher text:",n)
x=int(input("enter the key:"))
print("plain text")
for i in n:
    if i.isalpha():
        ascii=ord('a') if i.islower()else ord('A')
        plain=chr((ord(i)-ascii-x)%26+ascii)
        print(plain,end="")
    else:
        print(i,end="")
