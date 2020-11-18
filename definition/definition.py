#!/usr/bin/python3

from pwn import remote
import time

if __name__ == '__main__':
    date = str(round(time.time()))
    server = remote("challengecybersec.fr", 6660)
    server.recvuntil("> ")
    server.sendline(date)
    res = server.recvline()
    print(res)
