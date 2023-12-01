import numpy as np

# Function to convert letters to numbers (A=0, B=1, ..., Z=25)
def letter_to_number(letter):
    return ord(letter.upper()) - ord('A')

# Function to convert numbers to letters (0=A, 1=B, ..., 25=Z)
def number_to_letter(number):
    return chr(number + ord('A'))

# Function to perform a known plaintext attack on Hill cipher
def known_plaintext_attack(plaintexts, ciphertexts):
    if len(plaintexts) != len(ciphertexts):
        raise ValueError("Number of plaintexts and ciphertexts should be the same.")

    n = len(plaintexts[0])  # Size of the key matrix (assuming square matrix)
    
    # Ensure all plaintexts and ciphertexts have the same length
    for plaintext, ciphertext in zip(plaintexts, ciphertexts):
        if len(plaintext) != n or len(ciphertext) != n:
            raise ValueError("All plaintexts and ciphertexts should have the same length.")
    
    # Convert plaintexts and ciphertexts to numeric form
    plaintext_numbers = [[letter_to_number(letter) for letter in plaintext] for plaintext in plaintexts]
    ciphertext_numbers = [[letter_to_number(letter) for letter in ciphertext] for ciphertext in ciphertexts]
    
    P = np.array(plaintext_numbers)
    C = np.array(ciphertext_numbers)
    
    # Calculate the key matrix
    key_matrix = np.dot(np.linalg.inv(P), C) % 26
    key_matrix = key_matrix.astype(int)
    
    # Calculate the inverse of the key matrix
    inv_key_matrix = mod_inverse(key_matrix)
    
    if inv_key_matrix is None:
        return None
    
    return inv_key_matrix
# Function to calculate the modular inverse of a matrix in modulo 26
def mod_inverse(matrix):
    det = int(np.round(np.linalg.det(matrix))) % 26
    det_inv = -1
    for i in range(26):
        if (det * i) % 26 == 1:
            det_inv = i
            break
    
    if det_inv == -1:
        return None
    
    adjoint = np.round(det * np.linalg.inv(matrix)).astype(int) % 26
    inv_matrix = (det_inv * adjoint) % 26
    return inv_matrix


# Example usage:
plaintexts = ["HELLO", "WORLD", "ATTACK"]
ciphertexts = ["EQNVZ", "ZPIGD", "PZMQPK"]

# Check lengths
plaintext_lengths = [len(plaintext) for plaintext in plaintexts]
ciphertext_lengths = [len(ciphertext) for ciphertext in ciphertexts]

print("Plaintext Lengths:", plaintext_lengths)
print("Ciphertext Lengths:", ciphertext_lengths)
