import numpy as np
import json

# 3D koordinatları stringe dönüştüren fonksiyon
def coords_to_string(coords, key):
    chars = []
    for coord in coords:
        x, y, z = coord
        ascii_val = (x * pow(key[0], -1, 256)) % 256
        ascii_val = (ascii_val + (y * pow(key[1], -1, 256)) % 256) // 2
        ascii_val = (ascii_val + (z * pow(key[2], -1, 256)) % 256) // 2
        chars.append(chr(ascii_val))
    return ''.join(chars)

# data.json dosyasından verileri oku
with open('data.json', 'r') as f:
    data = json.load(f)

key = data['key']
coords = np.array(data['coords'])

# 3D koordinatları stringe dönüştür
decoded_string = coords_to_string(coords, key)
print("Çözümlenen String:", decoded_string)
