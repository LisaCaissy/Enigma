from enigma.rotors.rotor import Rotor
from enigma.plugboard import Plugboard
from enigma.machine import EnigmaMachine

#Rotors
r1 = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
r2 = Rotor('my rotor2', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', ring_setting=5, stepping='E')
r3 = Rotor('my rotor3', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=15, stepping='V')

#Reflector
reflector = Rotor('my reflector', 'FVPJIAOYEDRZXWGCTKUQSBNMHL')

#Plugboard
pb = Plugboard.from_key_sheet('PO ML IU KJ NH YT GB VF RE DC')

#Machine
machine_encrypt = EnigmaMachine([r1, r2, r3], reflector, pb)
machine_decrypt = EnigmaMachine([r1, r2, r3], reflector, pb)

def encrypter():

    global message
    global ciphertext_encrypt
    # Set the initial position of the Enigma rotors
    machine_encrypt.set_display('AFP')
    print("AFP")

    # Encrypt the text 'BFR' and sotre it as msg_key
    msg_key = machine_encrypt.process_text('OMH')
    print(msg_key)

    machine_encrypt.set_display("OMH")
    plaintext = message
    ciphertext_encrypt = machine_encrypt.process_text(plaintext)
    print(ciphertext_encrypt)

    position = machine_encrypt.get_display()
    print(position)

def decrypter():

    global ciphertext_encrypt
    global message
    # Set the initial position of the Enigma rotors
    machine_decrypt.set_display('FNZ')

    # Decrypt the text 'PWE' and store it as msg_key
    msg_key = machine_decrypt.process_text('AYR')
    print(msg_key)

    # Set the new start position of the Enigma rotors
    machine_decrypt.set_display(msg_key)

    ciphertext_decrypt = ciphertext_encrypt
    plaintext = machine_decrypt.process_text(ciphertext_decrypt)
    print(plaintext)

    position = machine_decrypt.get_display()
    print(position)


print()
message = input("Saisir message : ")

encrypter()
print()
decrypter()

input()



# from enigma.rotors.rotor import Rotor
# from enigma.plugboard import Plugboard
# from enigma.machine import EnigmaMachine
# r1 = Rotor('my rotor1', 'EKMFLGDQVZNTOWYHXUSPAIBRCJ', ring_setting=0, stepping='Q')
# r2 = Rotor('my rotor2', 'AJDKSIRUXBLHWTMCQGZNPYFVOE', ring_setting=5, stepping='E')
# r3 = Rotor('my rotor3', 'BDFHJLCPRTXVZNYEIWGAKMUSQO', ring_setting=15, stepping='V')
# reflector = Rotor('my reflector', 'FVPJIAOYEDRZXWGCTKUQSBNMHL')
# pb = Plugboard.from_key_sheet('PO ML IU KJ NH YT GB VF RE DC')
# machine = EnigmaMachine([r1, r2, r3], reflector, pb)
