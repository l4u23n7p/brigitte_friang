#!/usr/bin/python3

code = [0x69,0x6f,0x38,0x56,0x50,0x57,0x50,0x56,6]
password = [0,0,0,0,0,0,0,0,0,0x34]

for c in range(len(code),0,-1):
    password[c-1] = code[c-1] ^ password[c]

part = ''.join([chr(x) for x in password])

print("La partie est : %s" % part)
