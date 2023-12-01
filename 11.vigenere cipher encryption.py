 def vigenere_cipher_encrypt(plain_text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_length = len(key)
    key_as_int = [alphabet.index(i) for i in key]
    plain_text_as_int = [alphabet.index(i) for i in plain_text]
    cipher_text_as_int = [
        (plain_text_as_int[i] + key_as_int[i % key_length]) % 26
        for i in range(len(plain_text_as_int))
    ]
    cipher_text = "".join(alphabet[i] for i in cipher_text_as_int)
    return cipher_text
plain_text = str(input("enter the plain text"))
key = str(input("enter the key"))
cipher_text = vigenere_cipher_encrypt(plain_text, key)
print("Plain Text:", plain_text)
print("Cipher Text:", cipher_text)
