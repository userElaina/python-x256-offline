import src.x256offline as x256

c0 = 0x23307b
x0e = x256.from_rgb(c0)
x0w = x256.from_rgb(c0, weighted=True)

print(hex(c0))
print(x0e, hex(x256.to_rgb(x0e)))
print(x0w, hex(x256.to_rgb(x0w)))

# 0x23307b
# 4 0x80
# 24 0x5f87
