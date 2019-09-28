import simplecrypt

encrypted = open("encrypted.bin", "rb").read()
psw = open("passwords.txt").read().split('\n')
print('start')

for ps in psw:
    try:
        decr = simplecrypt.decrypt(ps, encrypted)
        print(f'\ngood pass: {ps}\n\n {decr}\n')
        break
    except simplecrypt.DecryptionException:
        print(f'bad pass : {ps}')
