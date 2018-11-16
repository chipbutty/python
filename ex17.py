"Random password generator - ex. 17"
import random
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 10
print (s)
p = "".join(random.sample(s,passlen))
print (p)