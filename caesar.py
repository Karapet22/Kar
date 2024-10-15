# lab 4
class Caesarobj:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        result = ""
        for i in text:
            if i.isalpha():
                asci = 65 if i.isupper() else 97
                result += chr((ord(i) - asci + self.shift) % 26 + asci)
            else:
                result += i
        return result

    def decrypt(self, text):
        result = ""
        for i in text:
            if i.isalpha():
                asci = 65 if i.isupper() else 97
                result += chr((ord(i) - asci - self.shift) % 26 + asci)
            else:
                result += i
        return result

obj = Caesarobj(shift= 3)

text = input()

x = obj.encrypt(text)
print(f"objtext: {x}")

y = obj.decrypt(x)
print(f"Deobjed text: {y}")