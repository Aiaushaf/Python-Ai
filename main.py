import random

pw = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pg = int(input("Berapa panjang password yang ingin dibuatkan?"))
pe = ""

for i in range(pg) :
    pe = pe + random.choice(pw)
    
print(pe)
