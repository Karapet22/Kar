class DiffieHellman:
    def __init__(self, p, g):
        self.p = p  
        self.g = g  

    def public_key(self, private_key):
        return pow(self.g, private_key, self.p)

    def shared_secret(self, public_key, private_key):
        return pow(public_key, private_key, self.p)


p = 23 
g = 5   

obj = DiffieHellman(p, g)

alice_private = 6
bob_private = 15

alice_public = obj.public_key(alice_private)
bob_public = obj.public_key(bob_private)

alice_shared = obj.shared_secret(bob_public, alice_private)
bob_shared = obj.shared_secret(alice_public, bob_private)

print("Alice's public key:", alice_public)
print("Bob's public key:", bob_public)
print("Shared secret (Alice):", alice_shared)
print("Shared secret (Bob):", bob_shared)
