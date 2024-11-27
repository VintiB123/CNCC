import math


def modular_inverse(e, phi_n):
    d = pow(e, -1, phi_n)   
    return d


def encrypt(e, n, message):
    cipher = (message ** e) % n  
    return cipher


def decrypt(d, n, cipher):
    decrypted = (cipher ** d) % n  
    return decrypted


p = 11  
q = 13  


n = p * q  
phi_n = (p - 1) * (q - 1) 


e = 2
while math.gcd(e, phi_n) != 1:  
    e += 1


d = modular_inverse(e, phi_n)


print(f"Public key: (e = {e}, n = {n})")
print(f"Private key: (d = {d}, n = {n})")


while True:
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        message = int(input("Enter an integer to encrypt: "))
        cipher = encrypt(e, n, message)
        print(f"Encrypted message: {cipher}")
    elif choice == 2:
        cipher = int(input("Enter an encrypted integer to decrypt: "))
        decrypted = decrypt(d, n, cipher)
        print(f"Decrypted message: {decrypted}")
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
