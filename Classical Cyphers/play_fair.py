def get_matrix(key):
    '''takes a key and returns
    matrix: a 5x5 matrix of letters
    locations: a dictionary with letters as keys and (row, column) as value
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    matrix_text = key + letters
    matrix_text = matrix_text.lower()
    matrix_text = matrix_text.replace('j', 'i')
    matrix_text = ''.join(sorted(set(matrix_text), key=matrix_text.index))
    assert( len(matrix_text) == 25 )

    matrix = []
    k = 0
    locations = {} 
    for i in range(5):
        matrix.append([])
        for j in range(5):
            matrix[i].append(matrix_text[k])
            locations[ matrix_text[k] ] = (i, j)
            k += 1
    return matrix, locations

def play_fair_encrypt(plain_text, key):
    matrix, locations = get_matrix(key)

    plain_text = plain_text.lower()
    plain_text = plain_text.replace('j', 'i')
    plain_text = plain_text.replace(' ', '')
    len_text = len(plain_text)

    i = 0
    cipher_text = ''
    while i < len_text:
        l = plain_text[i]
        if i+1 < len_text:
            r = plain_text[i+1]
        else:
            r = 'x'
        if l == r:
            r = 'x'
            i += 1
        else:
            i += 2
        loc_l = locations[l]
        loc_r = locations[r]
        if loc_l[0] == loc_r[0]:
            cipher_text += matrix[ loc_l[0] ][ (loc_l[1]+1)%5 ]
            cipher_text += matrix[ loc_r[0] ][ (loc_r[1]+1)%5 ]
        elif loc_l[1] == loc_r[1]:
            cipher_text += matrix[ (loc_l[0]+1)%5 ][loc_l[1]]
            cipher_text += matrix[ (loc_r[0]+1)%5 ][loc_r[1]]
        else:
            cipher_text += matrix[ loc_l[0] ][ loc_r[1] ]
            cipher_text += matrix[ loc_r[0] ][ loc_l[1] ]
    return cipher_text

if __name__ == '__main__':
    plain_text = 'instrumentsz'

    key = 'monarchy'

    cipher_text = play_fair_encrypt(plain_text, key)
    print(cipher_text)