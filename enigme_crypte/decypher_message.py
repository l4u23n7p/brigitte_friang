#!/usr/bin/python3

from enigma.machine import EnigmaMachine
import string

def decode(message, display, config):
    machine = EnigmaMachine.from_key_sheet(
       rotors=config['rotors'],
       reflector=config['reflector'],
       ring_settings=config['ring'],
       plugboard_settings=config['plugboard'])

    machine.set_display(display)

    return machine.process_text(message)

config = {
    'rotors': 'I III V',
    'reflector': 'B',
    'ring': 'R E J',
    'plugboard': 'AZ BE'
}
key = 'IVQDQT'
msg = 'NHABMPSVBYYUCJIYMJBRDWXAXP'
name = 'THYVCROD'

key_decode = decode(key, 'MER', config)
print('message key is %s' % key_decode)

msg_decode = decode(msg, key_decode[:3], config)
print('flag is DGSESIEE{%s}' % msg_decode)

name_decode = decode(name, key_decode[:3], config)
print('name is %s' % name_decode)