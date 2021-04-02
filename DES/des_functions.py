from des_data import SHIFTS, PC_1, PC_2, S_BOX

def permut(block, table):
    return [block[t-1] for t in table]

def shift(block, round):
    l_block, r_block = block[:len(block)//2], block[len(block)//2:]
    n = SHIFTS[round-1]
    return l_block[n:] + l_block[:n] + r_block[n:] + r_block[:n]

# returns list of 16 keys
def expand_keys(key):
    keys = []
    pc1_key = permut(key, PC_1)
    sh_key = pc1_key
    for i in range(1, 17):
        sh_key = shift(sh_key, i)
        keys.append( permut(sh_key, PC_2) )
    return keys

###############

# 48 bits -> 32 bits
def sub_box(block):
    mini_blocks = [block[i: i+6] for i in range(0, len(block), 6)]
    new_block = ''
    for i, b in enumerate(mini_blocks):
        row = int(b[0] + b[-1], 2)
        col = int("".join( b[1:-1] ), 2)
        new_block += "{:04b}".format( S_BOX[i][row][col] )
    return list(new_block)

def xor(b_x, b_y):
    result = ''
    if len(b_x) == 32:
        result = "{:032b}".format( int("".join(b_x), 2) ^ int("".join(b_y), 2) )
    else:
        result = "{:048b}".format( int("".join(b_x), 2) ^ int("".join(b_y), 2) )
    return list(result)