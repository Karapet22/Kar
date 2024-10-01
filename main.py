alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Функция шифрования по ключу
#text - list символов текста
#key - list с перестановкой на алфавите
def encrypt(text, key):
    result = []
    for i in range(len(text)):
        result.append(key[alphabet.index(text[i])])
    print(result)
    return result