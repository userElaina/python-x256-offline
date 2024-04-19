import os
import zlib

DIRNAME = os.path.dirname(__file__)

RGB_X256 = dict()

with open(os.path.join(DIRNAME, 'x256.bin'), 'rb') as f:
    data =  f.read()

d2 = zlib.compress(data, level=9)
d3 = zlib.decompress(d2)

print(len(data), len(d2))

assert len(d3) == len(data)

for i in range(len(d3)):
    assert data[i] == d3[i]

DST = os.path.join(os.path.dirname(DIRNAME), 'src', 'x256offline', 'x256.bin')
open(DST, 'wb').write(d2)
print('OK')
