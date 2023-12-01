import string

def generate_cipher_sequence(keyword):
    keyword = keyword.upper()
    unique_chars = []
    cipher_sequence = ''

    # Creating a unique list of characters from the keyword
    for char in keyword:
        if char not in unique_chars and char.isalpha():
            unique_chars.append(char)

    # Generating the cipher sequence based on the keyword
    for char in string.ascii_uppercase:
        if char not in unique_chars:
            cipher_sequence += char

    cipher_sequence = keyword + cipher_sequence
    return cipher_sequence

def encrypt(message, cipher_sequence):
    message = message.upper()
    encrypted_message = ''

    # Encrypting the message using the generated cipher sequence
    for char in message:
        if char.isalpha():
            index = ord(char) - ord('A')
            encrypted_message += cipher_sequence[index]
        else:
            encrypted_message += char

    return encrypted_message

def decrypt(ciphertext, cipher_sequence):
    ciphertext = ciphertext.upper()
    decrypted_message = ''

    # Decrypting the ciphertext using the generated cipher sequence
    for char in ciphertext:
        if char.isalpha():
            index = cipher_sequence.index(char)
            decrypted_message += chr(index + ord('A'))
        else:
            decrypted_message += char

    return decrypted_message

# Example usage:
keyword = "CIPHER"
cipher_sequence = generate_cipher_sequence(keyword)
print("Generated Cipher Sequence:", cipher_sequence)

plaintext = "Hello, World!"
encrypted_text = encrypt(plaintext, cipher_sequence)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, cipher_sequence)
print("Decrypted Text:", decrypted_text)
