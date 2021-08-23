# The code is modified from
# https://gist.github.com/lopes/168c9d74b988391e702aac5f4aa69e41
#
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        iv = b'o'*16
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'),
                                                      16)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:16])
        return unpad(self.cipher.decrypt(raw[16:]), 16)


def bitFlip( pos, bit, data):
    raw = b64decode(data)
    list1 = list(raw)
    list1[pos] = ord(chr(ord(data[pos])^bit))
    return b64encode(bytes(list1))

if __name__ == '__main__':
    key = b'Sixteen byte key'
    msg = "logged_username=pdmin&password=g0ld3n_b0y"

    # print('Original Message:', msg)

    ctx = AESCipher(key).encrypt(msg)
    print(ctx)
    # print('Ciphertext      :', ctx)

    ctx = bitFlip(16, 67, '478c5754e92156bb6cf15dfd4c9b58a17d8470244ec6f8bf47f63abe631f642ef958c34d99aaba26b9309c10f44d397a')
    print(ctx)
    # print('Message...      :', AESCipher(key).decrypt(ctx).decode('utf-8'))

    # if msg != AESCipher(key).decrypt(ctx).decode('utf-8'):
