import math

def sort_key(key):
    return sorted(key)

def generate_key_matrix(sorted_key, msg):
    b = math.ceil(len(msg) / len(sorted_key))
    arr = [['_' for _ in range(len(sorted_key))] for _ in range(b)]
    i = 0
    j = 0
    for h in range(len(msg)):
        arr[i][j] = msg[h]
        j += 1
        if j > len(sorted_key) - 1:
            j = 0
            i += 1
    return arr

def print_encrypted_matrix(arr, sorted_key):
    cipher_text = ""
    for i in sorted_key:
        h = sorted_key.index(i)
        for j in range(len(arr)):
            cipher_text += arr[j][h]
    print("The cipher text is: ", cipher_text)

def row(s, key):
    sorted_key = sort_key(key)
    print("The key used for encryption is: ", sorted_key)
    key_matrix = generate_key_matrix(sorted_key, s)
    print("The message matrix is: ")
    for i in key_matrix:
        print(i)
    print_encrypted_matrix(key_matrix, sorted_key)

msg = input("Enter the message: ")
key = input("Enter the key in alphabets: ")
row(msg, key)
