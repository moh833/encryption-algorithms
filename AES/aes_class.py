from aes import text_to_matrix, matrix_to_text, generate_key, add_round_key , sub_bytes, shift_rows, mix_columns
from aes import inv_shift_rows, inv_sub_bytes, inv_mix_columns

def print_matrix(matrix):
    for k in range(4):
        print([ hex(s) for s in matrix[k] ])

class AES:

    def __init__(self):
        self.key_matrices = []

    def set_key(self, cipher_key):
        self.rounds = 10
        self.expand_keys(cipher_key)
        assert(len(self.key_matrices) == self.rounds+1)
    
    def expand_keys(self, cipher_key):
        key = text_to_matrix(cipher_key)
        self.key_matrices.append(key)
        for i in range(1, self.rounds+1):
            key = generate_key(key, i)
            self.key_matrices.append(key)

    def encrypt(self, plain_text):
        state = text_to_matrix(plain_text)

        add_round_key(state, self.key_matrices[0])

        for i in range(1, self.rounds):
            sub_bytes(state)
            shift_rows(state)
            mix_columns(state)
            add_round_key(state, self.key_matrices[i])
        
        sub_bytes(state)
        shift_rows(state)
        add_round_key(state, self.key_matrices[-1])

        return matrix_to_text(state)

    def decrypt(self, cipher_text):

        state = text_to_matrix(cipher_text)

        add_round_key(state, self.key_matrices[-1])
        inv_shift_rows(state)
        inv_sub_bytes(state)

        for i in range(self.rounds - 1, 0, -1):
            add_round_key(state, self.key_matrices[i])
            inv_mix_columns(state)
            inv_shift_rows(state)
            inv_sub_bytes(state)

        add_round_key(state, self.key_matrices[0])

        return matrix_to_text(state)
