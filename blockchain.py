
blockchain = [1]


def get_last_bc_value():
    return blockchain[-1]


def add_value(trans_amt):
    blockchain.append([get_last_bc_value(), trans_amt])


add_value(34.5)
add_value(42)
add_value(666)
print(blockchain)
