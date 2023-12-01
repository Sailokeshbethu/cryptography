def generate_key_square(keyword):
    # Create a key square (5x5 matrix) based on the keyword
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Excluding 'J' as per Playfair rules

    # Remove duplicates from the keyword and convert it to uppercase
    keyword = ''.join(dict.fromkeys(keyword.upper()))

    # Create the initial key square using the keyword
    key_square = ''
    for letter in keyword:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, '')  # Remove the letter from the alphabet
            key_square += letter

    key_square += alphabet  # Add remaining letters of the alphabet to complete the key square

    return [key_square[i:i+5] for i in range(0, 25, 5)]  # Return the 5x5 matrix

def get_coordinates(matrix, letter):
    # Get the coordinates (row, column) of a letter in the key square
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)
    return -1, -1  # Return default coordinates if letter not found


def encrypt(plaintext, key_square):
    plaintext = plaintext.upper().replace('J', 'I')  # Convert to uppercase and replace 'J' with 'I'
    plaintext = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]

    encrypted_text = ''
    for pair in plaintext:
        if len(pair) < 2:  # If the last pair has only one letter, add an 'X'
            pair += 'X'

        row1, col1 = get_coordinates(key_square, pair[0])
        row2, col2 = get_coordinates(key_square, pair[1])

        if row1 == row2:  # Same row, shift columns cyclically
            encrypted_text += key_square[row1][(col1 + 1) % 5] + key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column, shift rows cyclically
            encrypted_text += key_square[(row1 + 1) % 5][col1] + key_square[(row2 + 1) % 5][col2]
        else:  # Form rectangle, take corners
            encrypted_text += key_square[row1][col2] + key_square[row2][col1]

    return encrypted_text

# Example usage:
keyword = "KEYWORD"
plaintext = "HELLO PLAYFAIR"

key_square = generate_key_square(keyword)
encrypted = encrypt(plaintext, key_square)

print("Key Square:")
for row in key_square:
    print(row)
print("\nEncrypted Text:", encrypted)
