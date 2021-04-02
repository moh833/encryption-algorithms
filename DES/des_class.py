from des_functions import permut, shift, expand_keys, sub_box, xor
from des_data import IP, E, P, IP_1

class DES:

    def __init__(self):
        self.set_key('133457799bbcdff1')

    def set_key(self, key_hex):
        self.original_key = "{:064b}".format(int(key_hex, 16))
        self.keys = expand_keys(self.original_key)

    def get_key(self):
        return "{:016x}".format(int(self.original_key, 2))

    def forward(self, block, ENCRYPT=True):
        block = permut(block, IP)
        L = block[:len(block)//2]
        R = block[len(block)//2:]
        for i in range(16):
            E_R = permut(R, E)

            if(ENCRYPT):
                mid = xor(self.keys[i], E_R)
            else:
                mid = xor(self.keys[15-i], E_R)

            mid = sub_box(mid)
            mid = permut(mid, P)
            final = xor(L, mid)

            L = R
            R = final

        return "".join( permut(R+L, IP_1) )
    
    def encrypt(self, text_hex):
        text_block = "{:064b}".format(int(text_hex, 16))
        cipher_block = self.forward(text_block, ENCRYPT=True)
        return "{:016x}".format(int(cipher_block, 2))

    def decrypt(self, cipher_hex):
        cipher_block = "{:064b}".format(int(cipher_hex, 16))
        text_block = self.forward(cipher_block, ENCRYPT=False)
        return "{:016x}".format(int(text_block, 2))