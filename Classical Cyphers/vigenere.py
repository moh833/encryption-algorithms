
def vigenere_encrypt(plain_text, key, auto=False):
    plain_text = plain_text.upper()
    key = key.upper()


    if(len(plain_text) > len(key) and auto):
        expanded_key = key + plain_text[:len(plain_text) - len(key)]
    else:
        n = len(plain_text) // len(key) + 1
        expanded_key = key * n


    cipher_text = ''
    for i in range(len(plain_text)):
        p_i = ord(plain_text[i]) - 65
        k_i = ord(expanded_key[i]) - 65
        l_i = ( p_i + k_i ) % 26
        cipher_text += chr(l_i + 65)
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    n = len(cipher_text) // len(key) + 1
    expanded_key = key * n
    plain_text = ''
    for i in range(len(cipher_text)):
        c_i = ord(cipher_text[i]) - 65
        k_i = ord(expanded_key[i]) - 65
        l_i = ( c_i - k_i ) % 26
        plain_text += chr(l_i + 65)
    return plain_text

if __name__ == '__main__':

    key = 'AYUSH'
    plain_text = 'GEEKSFORGEEKS'
    cipher_text = vigenere_encrypt(plain_text, key)
    print(cipher_text)
    decrypted_text = vigenere_decrypt(cipher_text, key)
    print(decrypted_text)