cipher="rdsfrjnxwflmz"
print("cipher text:",cipher)
print("key:")
for x in range(26):
    decrypt = ''
    for i in cipher:
        if i.isalpha():
            ascii=ord('a') if i.islower() else ord('A')
            key=chr((ord(i)-ascii-x)%26+ascii)
            decrypt += key
        else:
            decrypt += i
    print(f"x {x}: {decrypt}")
        
