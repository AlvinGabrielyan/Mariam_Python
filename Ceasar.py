def encrypt(plaintext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ""
    plaintext = plaintext.upper()

    for ch in plaintext:
        if ch.isalpha():
            index = alphabet.index(ch)
            new_index = (index + key) % 26
            ciphertext += alphabet[new_index]
        else:
            ciphertext += ch

    return ciphertext

def decrypt(ciphertext, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ""
    ciphertext = ciphertext.upper()

    for ch in ciphertext:
        if ch.isalpha():
            index = alphabet.index(ch)
            new_index = (index - key + 26) % 26
            plaintext += alphabet[new_index]
        else:
            plaintext += ch

    return plaintext

if __name__ == "__main__":
    plaintext = input("Enter plaintext (uppercase only): ").upper()
    key = int(input("Enter key (0-25): "))

    encrypted = encrypt(plaintext, key)
    print(encrypted)

    decrypted = decrypt(encrypted, key)
    print(decrypted)
