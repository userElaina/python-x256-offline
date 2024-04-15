## python-x256-offline

Quickly find the nearest xterm 256 color index of an RGB.

##### Installation

```sh
python -m pip install x256offline
```

##### Simple Example

```py
import x256offline as x256

c0 = 0x23307b
x0e = x256.from_rgb(c0)
x0w = x256.from_rgb(c0, weighted=True)

print(hex(c0))
print(x0e, hex(x256.to_rgb(x0e)))
print(x0w, hex(x256.to_rgb(x0w)))

# 0x23307b
# 4 0x80
# 24 0x5f87
```
