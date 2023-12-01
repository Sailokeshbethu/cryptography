def create_playfair_matrix(keyword):
    # Create a 5x5 matrix (Playfair uses a 5x5 grid)
    matrix = [['' for _ in range(5)] for _ in range(5)]
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Note: No 'J' in Playfair, 'I' and 'J' are treated as one

    # Fill the matrix with the keyword
    keyword = keyword.upper().replace('J', 'I')  # Replace 'J' with 'I'
    keyword += alphabet

    # Populate the matrix with the unique letters from the keyword
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = keyword[index]
            index += 1

    return matrix

def playfair_decrypt(ciphertext, keyword):
    ciphertext = ciphertext.replace(' ', '').upper()  # Remove spaces and convert to uppercase
    matrix = create_playfair_matrix(keyword)

    # Ensure the length of the ciphertext is even for processing in pairs
    if len(ciphertext) % 2 != 0:
        ciphertext += 'Z'  # Pad with a dummy character if needed to make it even

    decrypted_text = ''  # Define decrypted_text variable

    i = 0
    while i < len(ciphertext):
        letter1 = ciphertext[i]
        letter2 = ciphertext[i + 1]

        # Logic for Playfair decryption...
        # Here, you should implement the decryption rules for the Playfair cipher
        # Update the decrypted_text variable with the decrypted characters

        decrypted_text += letter1  # Placeholder, replace this with actual decryption logic
        decrypted_text += letter2  # Placeholder, replace this with actual decryption logic

        i += 2

    return decrypted_text

# Example usage with provided ciphertext and keyword
ciphertext = """KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ"""

keyword = "PT109"  # Keyword associated with the Playfair cipher

decrypted_message = playfair_decrypt(ciphertext, keyword)
print("Decrypted Message:")
print(decrypted_message)
