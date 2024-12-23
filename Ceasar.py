def encrypt(plaintext, key):
    ciphertext = ""
    plaintext = plaintext.upper() #Cankacac mutqagrvac tar sarquma mecatar vorovhetev xndiry mecatareri heta ashxarum
    key = key % 26

    for ch in plaintext:
        if ch.isalpha():  
            base = ord('A') #Mutqagrvac symboly convert a anum ASCII kodi(ira tvayin arjeqin)
            ch = chr((ord(ch) - base + key) % 26 + base) # tary hamapatasxan key-ov texasharjelu banadzevna
        ciphertext += ch

    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    ciphertext = ciphertext.upper() 
    key = key % 26

    for ch in ciphertext:
        if ch.isalpha():  
            base = ord('A')
            ch = chr((ord(ch) - base - key + 26) % 26 + base)
        plaintext += ch

    return plaintext

if _name_ == "_main_":
    plaintext = input("Enter plaintext (uppercase only): ").upper()
    key = int(input("Enter key (0-25): "))

    encrypted = encrypt(plaintext, key)
    print(f"Encrypted text: {encrypted}")

    decrypted = decrypt(encrypted, key)
    print(f"Decrypted text: {decrypted}")
