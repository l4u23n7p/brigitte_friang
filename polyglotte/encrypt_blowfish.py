#!/usr/bin/python3

import sys
import binascii
from Crypto.Cipher import Blowfish
from struct import pack

bs = Blowfish.block_size
key = b'\xce]`^+5w#\x96\xbbsa\x14\xa7\x0ei'
iv = b'\xc4\xa7\x1e\xa6\xc7\xe0\xfc\x82'
ciphertext = open('message.pdf', 'rb').read()
cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
msg = cipher.encrypt(ciphertext)

with open('message.pdf.blowfish', 'wb') as f:
    f.write(msg)


