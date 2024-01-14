string='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
n=24523
base62=''
while n>0:
    t=n%62
    base62+=string[t]
    n=n//62
base62=base62[::-1]
print(base62)