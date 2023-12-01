import numpy as np

# Define the plaintext message
plaintext = "meet me at the usual place at ten rather than eight oclock"

# Define the key matrix
key_matrix = np.array([[9, 4],
                        [5, 7]])

# Convert the plaintext to a matrix of integers
plaintext_matrix = np.zeros((len(plaintext)//2, 2), dtype=np.int32)
for i in range(len(plaintext)):
    if i % 2 == 0:
        plaintext_matrix[i//2, 0] = ord(plaintext[i]) - ord('a')
    else:
        plaintext_matrix[i//2, 1] = ord(plaintext[i]) - ord('a')

# Encrypt the plaintext matrix
ciphertext_matrix = np.dot(plaintext_matrix, key_matrix) % 26

# Convert the ciphertext matrix to a string
ciphertext = ""
for i in range(len(ciphertext_matrix)):
    for j in range(len(ciphertext_matrix[i])):
        ciphertext += chr(ciphertext_matrix[i, j] + ord('a'))

 print("Ciphertext:", ciphertext)

# Decrypt the ciphertext matrix
decryption_matrix = np.linalg.inv(key_matrix) % 26
decrypted_matrix = np.dot(ciphertext_matrix, decryption_matrix) % 26

# Convert the decrypted matrix to a string
decrypted_plaintext = ""
for i in range(len(decrypted_matrix)):
    for j in range(len(decrypted_matrix[i])):
        decrypted_matrix = decrypted_matrix.astype(np.int32)
        decrypted_plaintext += chr(decrypted_matrix[i, j] + ord('a'))

print("Decrypted plaintext:", decrypted_plaintext)
