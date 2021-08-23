import socketserver
import socket, os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from binascii import unhexlify

FLAG = 'HTB{FAK}'

wlcm_msg = '########################################################################\n' + \
           '#                  Welcome to the Bank of the World                    #\n' + \
           '#             All connections are monitored and recorded               #\n' + \
           '#      Disconnect IMMEDIATELY if you are not an authorized user!       #\n' + \
           '########################################################################\n'

key = get_random_bytes(16)
iv = get_random_bytes(16)
print(key)
print(key.hex())
print(iv)
print(iv.hex())

def encrypt_data(data):
    padded = pad(data.encode(), 16, style='pkcs7')
    cipher = AES.new(key, AES.MODE_CBC, iv)
    enc = cipher.encrypt(padded)
    return enc.hex()


def decrypt_data(encryptedParams, index =0):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    paddedParams = cipher.decrypt(unhexlify(encryptedParams))
    # print(paddedParams)
    print('herere', unpad(paddedParams, 16, style='pkcs7'), index)
    if b'admin&password=g0ld3n_b0y' in unpad(paddedParams, 16, style='pkcs7'):

        return 1
    else:
        return 0


def send_msg(s, msg):
    enc = msg.encode()
    s.send(enc)

def shift(cipher, b=16, xor=None):
    # xor = ord('w') ^ ord('r')
    # cipher_chunks = [cipher[i:i + 16] for i in range(0, len(cipher), 16)]
    # cipher_chunks[2] = hex(int(cipher_chunks[2][:2], 16) ^ xor)[2:] + cipher_chunks[2][2:]
    if not xor:
        xor = ord('b') ^ ord('a')
    cipher = cipher[:b] + hex(int(cipher[b:b+2], 32) ^ xor)[2:] + cipher[b+2:]
    return cipher

def main(s):
    send_msg(s, 'username: ')
    user = 'XXdmin'#s.recv(4096).decode().strip()

    send_msg(s, user + "'s password: ")
    passwd = 'g0ld3n_b0y'#s.recv(4096).decode().strip()

    send_msg(s, wlcm_msg)

    msg = 'logged_username=' + user + '&password=' + passwd

    # try:
    #     assert ('admin&parsword=g0ld3n_b0y' not in msg)
    # except AssertionError:
    #     send_msg(s, 'You cannot login as an admin from an external IP.\nYour activity has been logged. Goodbye!\n')
    #     raise

    msg = 'logged_username=' + user + '&password=' + passwd
    send_msg(s, "Leaked ciphertext:  " + encrypt_data(msg) + '\n')
    for i in range(1000):
        try:
            shifted = shift(encrypt_data(msg), 16, i)
            if decrypt_data(shifted, index=i):
                print('ok', i)
        except:
            pass
    send_msg(s, "Shifted ciphertext: " + shifted + '\n')
    send_msg(s, "enter ciphertext: ")

    enc_msg = s.recv(4096).decode().strip()

    try:
        check = decrypt_data(enc_msg)
    except Exception as e:
        send_msg(s, str(e) + '\n')
        s.close()

    if check:
        send_msg(s, 'Logged in successfully!\nYour flag is: ' + FLAG)
        s.close()
    else:
        send_msg(s, 'Please try again.')
        s.close()


class TaskHandler(socketserver.BaseRequestHandler):
    def handle(self):
        main(self.request)


if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 1337), TaskHandler)
    server.serve_forever()