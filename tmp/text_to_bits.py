import bitarray
ba = bitarray.bitarray()

data = '4d013d2cc89b64d0a7382221dcd0f7c4081abdf629e4a907ce02d84d8ea7a11fc91a46a9c5dd9bfef8f90870583de7e4'
ba.frombytes(data.encode('utf-8'))
print(ba)

ba = bitarray.bitarray()
data = '4d013d2cc89b64d0a7382221dcd0f7c4081abdf629e4a907ce02d84d8ea7a11fcf836bd9ac2ed6f63b1791de6bb3ff36'
ba.frombytes(data.encode('utf-8'))
print(ba)