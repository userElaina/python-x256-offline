import src.x256offline as x256

c0 = 0x297331
x0e = x256.from_rgb(c0)
x0w = x256.from_rgb(c0, weighted=True)
x1e = x256.from_rgb(c0, n_color=256)
x1w = x256.from_rgb(c0, weighted=True, n_color=256)

print(hex(c0))
print(x0e, hex(x256.to_rgb(x0e)))
print(x0w, hex(x256.to_rgb(x0w)))
print(x1e, hex(x256.to_rgb(x1e)))
print(x1w, hex(x256.to_rgb(x1w)))

# 0x297331
# 23 0x5f5f
# 2 0x8000
# 238 0x444444
# 239 0x4e4e4e
