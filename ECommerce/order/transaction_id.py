from secrets import choice,token_hex
def random_generator():
    len_of_hex=choice([10,12])
    return "TRXN"+token_hex(len_of_hex)