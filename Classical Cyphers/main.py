
from caesar import caesar_encrypt
from play_fair import play_fair_encrypt
from hill import hill_encrypt, get_key_matrix_from_string_numbers
from vigenere import vigenere_encrypt
from vernam import vernam_encrypt



def encrypt_file(data, key, n):
    data = data.split('\n')
    cipher_data = ''
    if n == 1:
        for plain_text in data:
            cipher_data += caesar_encrypt(plain_text.strip(), key) + '\n'
    elif n == 2:
        for plain_text in data:
            cipher_data += play_fair_encrypt(plain_text.strip(), key) + '\n'
    elif n == 3:
        for plain_text in data:
            cipher_data += hill_encrypt(plain_text.strip(), key) + '\n'
    elif n == 4:
        for plain_text in data:
            cipher_data += vigenere_encrypt(plain_text.strip(), key, auto) + '\n'
    elif n == 5:
        for plain_text in data:
            cipher_data += vernam_encrypt(plain_text.strip(), key) + '\n'
    return cipher_data



import os 

full_path = os.path.realpath(__file__)
path = os.path.dirname(full_path)

cipher_folders = {1: 'Caesar', 2: 'PlayFair', 3: 'Hill', 4: 'Vigenere', 5: 'Vernam'}
n = int(input("Enter a number to choose which cipher to run: \n1: Caesar\n2: PlayFair\n3: Hill\n4: Vigenere\n5: Vernam\n"))

while n not in list(range(1, 6)):
    n = int(input("Not valid input try again (1-5)\n"))

if n == 3:
    key = input("Enter the key matrix as space seperated numbers\n")
    key = get_key_matrix_from_string_numbers(key)
else:
    key = input('Enter the key:\n')

if n == 4:
    if int(input('Enter 0 for reapeating mode or 1 for auto mode.\n')):
        auto = True
    else:
        auto = False

data_path = path + f'/Input Files/{cipher_folders[n]}'
files = next(os.walk(data_path))[2]

output_path = path + f'/Output Files/{cipher_folders[n]}'

print("Encrypting files in", data_path)

if not os.path.exists(output_path):
    os.makedirs(output_path)

for f_name in files:
    with open(os.path.join(data_path, f_name), 'r') as f:
        cipher_data = encrypt_file(f.read(), key, n)

    with open(os.path.join(output_path, f_name.replace('plain', 'cipher')), 'w') as f:
        f.write(cipher_data)
with open(os.path.join(output_path, 'key.txt'), 'w') as f:
    f.write(str(key))

print("Check", output_path, 'folder')

input("Press any Key to exit..")


