from collections import Counter
import operator

# English language letter frequency (approximate)
english_letter_frequency = {
    'E': 0.1202, 'T': 0.091, 'A': 0.0812, 'O': 0.0768, 'I': 0.0731, 'N': 0.0695, 'S': 0.0628, 'R': 0.0602,
    'H': 0.0592, 'D': 0.0432, 'L': 0.0398, 'U': 0.0288, 'C': 0.0271, 'M': 0.0261, 'F': 0.023, 'Y': 0.0211,
    'W': 0.0209, 'G': 0.0203, 'P': 0.0182, 'B': 0.0149, 'V': 0.011, 'K': 0.0069, 'X': 0.0017, 'Q': 0.0011,
    'J': 0.001, 'Z': 0.0007
}

# Function to calculate letter frequencies in the text
def calculate_frequencies(text):
    # Count occurrences of each letter in the text
    letter_counts = Counter(letter for letter in text if letter.isalpha())
    
    # Calculate frequencies of each letter
    total_letters = sum(letter_counts.values())
    frequencies = {letter: count / total_letters for letter, count in letter_counts.items()}
    
    return frequencies

# Function to perform a letter frequency attack on an additive cipher
def additive_cipher_attack(ciphertext, top_n=10):
    potential_plaintexts = []
    
    for shift in range(26):  # Try all possible shifts (0 to 25)
        plaintext = ''.join(chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                            if char.isalpha() else char for char in ciphertext.upper())
        
        # Calculate the distance between the frequency of the potential plaintext and English letter frequency
        plaintext_frequencies = calculate_frequencies(plaintext)
        distance = sum(abs(plaintext_frequencies.get(letter, 0) - english_letter_frequency.get(letter, 0)) 
                       for letter in english_letter_frequency.keys())
        
        potential_plaintexts.append((plaintext, distance))
    
    # Sort potential plaintexts by their distance from English letter frequencies
    potential_plaintexts.sort(key=lambda x: x[1])
    
    # Return the top 'top_n' possible plaintexts
    return [plaintext for plaintext, _ in potential_plaintexts[:top_n]]

# Example usage:
ciphertext = "GWC uivioml bw nqvl bpm zqopb apqnb"
top_10_plaintexts = additive_cipher_attack(ciphertext, top_n=10)
for i, plaintext in enumerate(top_10_plaintexts, start=1):
    print(f"Plaintext {i}: {plaintext}")
