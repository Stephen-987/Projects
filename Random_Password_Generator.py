import random
P_L = int(input("Enter the length of the password: "))
s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&()*?=+-_"
p = "".join(random.sample(s, P_L))
print(p)

