import math



def get_key_matrix(key):
    key = key.upper()
    l = int( math.sqrt(len(key)) )
    key_matrix = []
    k = 0
    for i in range(l):
        key_matrix.append([])
        for j in range(l):
            key_matrix[i].append(ord(key[k]) % 65)
            k += 1
    return key_matrix

def get_key_matrix_from_string_numbers(key):
    key = key.split()
    l = int( math.sqrt(len(key)) )
    key_matrix = []
    k = 0
    for i in range(l):
        key_matrix.append([])
        for j in range(l):
            key_matrix[i].append(int(key[k]))
            k += 1
    return key_matrix

def hill_encrypt(plain_text, key_matrix):
    n = len(key_matrix)
    plain_text = plain_text.upper()
    # expand plain_text
    e = n - ( len(plain_text) % n )
    plain_text += "x" * e
    assert(len(plain_text) % n == 0)
    cipher_text = ''
    for k in range(0, len(plain_text), n):
        mini = [ord(l)-65 for l in plain_text[k: k+n]]
        for i in range(n):
            letter_ind = 0
            for j in range(n):
                letter_ind += key_matrix[i][j] * mini[j]
            cipher_text += chr( (letter_ind % 26) + 65 )
    return cipher_text


if __name__ == '__main__':
    key_matrix = [[6, 24, 1],
                  [13, 16, 10],
                  [20, 17, 15]]

    # key_matrix = [[3, 5], [1, 4]]
    
    # key = 'HILLMAGIC '
    # key_matrix = get_key_matrix(key)
    key = "6 24 1 13 16 10 20 17 15"
    key_matrix = get_key_matrix_from_string_numbers(key)
    print(key_matrix)

    plain_text = 'afaegEerwhwarhwarhwr'
    cipher_text = hill_encrypt(plain_text, key_matrix)
    print(cipher_text)