# -----------------------------------------
# ECC BASIC IMPLEMENTATION
# -----------------------------------------

# Elliptic Curve:
# y^2 = x^3 + ax + b mod p

a = 2
b = 3
p = 97

# Base point G
G = (3, 6)

# -----------------------------------------
# Modular Inverse Function
# -----------------------------------------

def mod_inverse(k, p):

    for i in range(1, p):

        if (k * i) % p == 1:

            return i

    return None


# -----------------------------------------
# Point Addition Function
# -----------------------------------------

def point_addition(P, Q):

    if P == Q:
        return point_doubling(P)

    x1, y1 = P
    x2, y2 = Q

    m = ((y2 - y1) * mod_inverse(x2 - x1, p)) % p

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)


# -----------------------------------------
# Point Doubling Function
# -----------------------------------------

def point_doubling(P):

    x1, y1 = P

    m = ((3 * x1 * x1 + a) *
         mod_inverse(2 * y1, p)) % p

    x3 = (m * m - 2 * x1) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)


# -----------------------------------------
# Scalar Multiplication
# -----------------------------------------

def scalar_multiplication(k, P):

    result = P

    for i in range(k - 1):

        result = point_addition(result, P)

    return result


# -----------------------------------------
# Key Generation
# -----------------------------------------

private_key = 5

public_key = scalar_multiplication(private_key, G)

print("\nPrivate Key:", private_key)
print("Public Key:", public_key)

# -----------------------------------------
# Encryption
# -----------------------------------------

message = 10

k = 2

C1 = scalar_multiplication(k, G)

shared_secret = scalar_multiplication(k, public_key)

C2 = message + shared_secret[0]

print("\nEncrypted Message:")
print("C1 =", C1)
print("C2 =", C2)

# -----------------------------------------
# Decryption
# -----------------------------------------

decryption_secret = scalar_multiplication(private_key, C1)

decrypted_message = C2 - decryption_secret[0]

print("\nDecrypted Message:", decrypted_message)