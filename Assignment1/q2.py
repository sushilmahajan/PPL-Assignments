import random

ip = 'y'
while ip == 'y':
    print(random.randrange(1, 6))
    ip = input("Roll Again? y/n ")
    if ip == 'n':
        break
