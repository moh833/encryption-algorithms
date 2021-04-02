from aes_class import AES
from aes import matrix_to_text



l = input('Enter E to Encrypt and D to Decrypt\n')

if l[0] == 'E' or l[0] == 'e':
    key = input('Enter the key as hex characters\n')
    msg = input('Enter the Message as hex characters\n')

    key = "{:032x}".format(int(key, 16))
    msg = "{:032x}".format(int(msg, 16))

    a = AES()
    a.set_key(key)
    encrypted_msg = a.encrypt(msg)
    print(f"The Ciphertext: ", encrypted_msg)
else:
    key = input('Enter the key as hex characters\n')
    encrypted_msg = input('Enter the Ciphertext as hex characters\n')

    key = "{:032x}".format(int(key, 16))
    encrypted_msg = "{:032x}".format(int(encrypted_msg, 16))

    a = AES()
    a.set_key(key)
    decrypted_msg = a.decrypt(encrypted_msg)
    print(f"The Plaintext: ", decrypted_msg)

input("Press any Key to exit..")


