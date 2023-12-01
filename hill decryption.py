import numpy as np

# Function to find the modular inverse of a matrix
def modInverse(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, modulus)
    adjoint = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)
    return adjoint % modulus

# Function to decrypt using Hill Cipher
def hill_decrypt(ciphertext, key_matrix, modulus, block_size):
    key_matrix_inv = modInverse(key_matrix, modulus)

    # Prepare the ciphertext matrix
    ciphertext = [ord(char) - ord('A') for char in ciphertext]
    ciphertext = np.array(ciphertext)
    ciphertext = np.reshape(ciphertext, (-1, block_size))

    # Decrypt the ciphertext
    plaintext = np.dot(ciphertext, key_matrix_inv) % modulus
    plaintext = plaintext.flatten()

    # Convert the decrypted numbers back to characters
    plaintext = ''.join([chr(int(x) + ord('A')) for x in plaintext])
    return plaintext

# Example usage:
# Ciphertext to decrypt
ciphertext = "WKNGDZ"

# Key matrix (3x3 matrix for a 3x3 Hill cipher)
key_matrix = np.array([[6, 24, 1],
                       [13, 16, 10],
                       [20, 17, 15]])

# Modulus (usually 26 for working with letters)
modulus = 26

# Block size (in this case, it's a 3x3 matrix)
block_size = 3

decrypted_text = hill_decrypt(ciphertext, key_matrix, modulus, block_size)
print("Decrypted text:", decrypted_text)
