from vigenere import vigenere_encrypt, vigenere_decrypt

def vernam_encrypt(plain_text, key):
    if(len(plain_text) > len(key)):
        key += plain_text[:len(plain_text) - len(key)]
    return vigenere_encrypt(plain_text, key)

def vernam_decrypt(cipher_text, key):
    return vigenere_decrypt(cipher_text, key)


if __name__ == '__main__':
    key = 'BNCRYfqweqrrqrrq'
    plain_text = 'ACODEVERNAM'
    cipher_text = vernam_encrypt(plain_text, key)
    print(cipher_text)
    decrypted_text = vernam_decrypt(cipher_text, key)
    print(decrypted_text)