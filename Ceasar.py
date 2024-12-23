def encrypt(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ""

    for ch in plaintext:
        if ch.isalpha():
            ch = ch.upper() 
            index = alphabet.index(ch)
            new_index = (index + key) % 26 
            ciphertext += alphabet[new_index]
        else:
            ciphertext += ch  # If non-alphabetic, add as is

    return ciphertext

def decrypt(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ""

    for ch in ciphertext:
        if ch.isalpha():
            ch = ch.upper()
            index = alphabet.index(ch)
            new_index = (index - key + 26) % 26
            plaintext += alphabet[new_index]
        else:
            plaintext += ch 

    return plaintext


plaintext = input("Enter plaintext (uppercase only): ").upper()
key = int(input("Enter key (0-25): "))

encrypted = encrypt(plaintext, key)
print(encrypted)

decrypted = decrypt(encrypted, key)
print(decrypted)
