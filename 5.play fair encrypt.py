from Crypto.Cipher import playfair
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Set up a new Playfair cipher object
key = b'thisisaverylongsecretkeythisisaverylongsecret key thisisaverylongsecret key'
cipher = playfair.new(key)

# Pad the plaintext to ensure its length is a multiple of 8
plaintext = b'thisisaverylongplaintext thisisaverylongplaintext thisisaverylongplaintext'
plaintext = pad(plaintext, 8)

# Encrypt the plaintext message
ciphertext = cipher.encrypt(plaintext)

print(f"Ciphertext: {ciphertext}")
