from des_class import DES

l = input('Enter E to Encrypt and D to Decrypt\n')


des = DES()
if l[0] == 'E' or l[0] == 'e':
    key = input('Enter the key as hex characters\n')
    msg = input('Enter the Message as hex characters\n')
    n = int(input('Enter the number of times to run the encryption\n'))

    des.set_key(key)
    for i in range(n):
        encrypted_msg = des.encrypt(msg)
    print(f"The Ciphertext after {n} encryptions: ", encrypted_msg)
else:
    key = input('Enter the key as hex characters\n')
    encrypted_msg = input('Enter the Ciphertext as hex characters\n')
    n = int(input('Enter the number of times to run the decryption\n'))

    des.set_key(key)
    for i in range(n):
        decrypted_msg = des.decrypt(encrypted_msg)
    print(f"The Plaintext after {n} decryptions: ", decrypted_msg)

input("Press any Key to exit..")
