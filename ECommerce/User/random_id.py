from secrets import choice,token_hex
from random import shuffle
def random_generator(first_name,email):
    len_of_hex=choice([8,10,12])
    token_id=token_hex(len_of_hex)
    token=list(first_name+token_id+email);shuffle(token)
    token="".join(token)
    return token