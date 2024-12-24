def encrypt(plaintext, key):
    ciphertext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key % 26  

    for ch in plaintext.upper(): 
        if ch in alphabet: 
            index = alphabet.index(ch)  
            new_index = (index + key) % 26
            ciphertext += alphabet[new_index]
        else:
            ciphertext += ch 

    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key % 26 

    for ch in ciphertext.upper(): 
        if ch in alphabet:  
            index = alphabet.index(ch) 
            new_index = (index - key) % 26 
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
