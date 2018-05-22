#!/usr/bin/env python
# Python 3.5.3 (default, Jan 19 2017, 14:11:04)

# Set up the Enigma machine

from enigma.machine import EnigmaMachine
global machine
machine = EnigmaMachine.from_key_sheet(rotors='IV I V',
                                               reflector='B', ring_settings='13 03 16',
                                               plugboard_settings='AE BV FK GO IZ JT LR MX NP WY') #QTQ JIS PCQ QPB


def encrypter():

    global message
    global machine
    global ciphertext_encrypt
    # Set the initial position of the Enigma rotors
    machine.set_display('LOL')                              #Ce que je veux, je peux mettre n'importe quoi.
    print("LOL")

    # Encrypt the text 'BFR' and sotre it as msg_key
    msg_key = machine.process_text('QTQ')                   # Ce que j'envois est le résultat codé de ces trois lettres.
    print(msg_key)

    machine.set_display(msg_key)
    plaintext = message
    ciphertext_encrypt = machine.process_text(plaintext)
    print(ciphertext_encrypt)

    position = machine.get_display()
    print(position)

def decrypter():

    global ciphertext_encrypt
    global message
    global machine
    # Set the initial position of the Enigma rotors
    machine.set_display('LOL')

    # Decrypt the text 'PWE' and store it as msg_key
    msg_key = machine.process_text('GFS')
    print(msg_key)

    # Set the new start position of the Enigma rotors
    machine.set_display('GFS')

    ciphertext_decrypt = 'RHLLQAS'                                     #Remplacer ça par le message encrypter même s'il vient de l'extérieur.
    plaintext = machine.process_text(ciphertext_decrypt)
    print(plaintext)

    position = machine.get_display()
    print(position)

###################### MAIN ###############################

print()
message = input("Saisir message : ")

encrypter()
print()
input()
decrypter()

input()

