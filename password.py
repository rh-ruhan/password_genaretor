import random
pwd = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567!@#$%^&*(')"

res = ''.join(random.choices(pwd,k=7))

print(res)