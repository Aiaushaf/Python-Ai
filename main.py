import random

def pass_make(pg) :

    pw = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    pe = ""

    for _ in range(pg) :
        pe = pe + random.choice(pw)
        
    return pe

