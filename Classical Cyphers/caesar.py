def caesar_encrypt(plain_text, key):
    key = int(key)
    cypher_text = ''
    for word in plain_text.split(' '):
        for l in word:
            if l.islower():
                cypher_text += chr( (ord(l) - 97 + key) % 26 + 97 )
            else:
                cypher_text += chr( (ord(l) - 65 + key) % 26 + 65 )
        cypher_text += ' '
    return cypher_text[:-1]

if __name__ == '__main__':

    c = caesar_encrypt("CEASER CIPHER DEMO", "4")
    print(c)



