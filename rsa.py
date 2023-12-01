# Function to factorize a number into prime factors
def factorize(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

# Given public key values
e = 31
n = 3599

# Factorize n into prime factors p and q
factors_n = factorize(n)
p = factors_n[0]
q = factors_n[1]

print("p =", p)
print("q =", q)
# Calculate phi(n)
phi_n = (p - 1) * (q - 1)

# Extended Euclidean Algorithm to find the modular multiplicative inverse
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x

# Calculate the modular multiplicative inverse of e mod phi(n)
gcd, x, y = egcd(e, phi_n)
if gcd == 1:
    private_key = x % phi_n
    print("Private Key (d) =", private_key)
else:
    print("e and phi(n) are not coprime, so the private key cannot be found.")
