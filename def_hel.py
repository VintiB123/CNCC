
def generate_public_key(private_key, p, g):
    return (g ** private_key) % p


p = 23
g = 5

print(f"Prime number (p): {p}")
print(f"Generator (g): {g}\n")


alice_private = int(input("Enter a private number for Alice: "))
bob_private = int(input("Enter a private number for Bob: "))


alice_public = generate_public_key(alice_private, p, g)
bob_public = generate_public_key(bob_private, p, g)

print(f"\nAlice's Public Key: {alice_public}")
print(f"Bob's Public Key: {bob_public}\n")


alice_shared_secret = (bob_public ** alice_private) % p
bob_shared_secret = (alice_public ** bob_private) % p


if alice_shared_secret == bob_shared_secret:
    print(f"Shared Secret Key: {alice_shared_secret}")
else:
    print("The shared secret keys do not match.")
