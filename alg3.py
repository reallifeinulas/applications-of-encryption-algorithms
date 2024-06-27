import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import json

######## String'i 3D koordinatlara dönüştüren fonksiyon ########
def string_to_3d_coords(input_string, key):
    coords = []
    for char in input_string:
        ascii_val = ord(char)
        x = (ascii_val * key[0]) % 256
        y = (ascii_val * key[1]) % 256
        z = (ascii_val * key[2]) % 256
        coords.append((x, y, z))
    return np.array(coords)

######## 3D poligonları oluşturan fonksiyon ########
def create_polygons(coords):
    polygons = []
    num_points = len(coords)
    for i in range(0, num_points - 2, 3):
        if i + 2 < num_points:
            polygon = [coords[i], coords[i + 1], coords[i + 2]]
            polygons.append(polygon)
    return polygons

########## anahtar
key = [7, 11, 13]

########## string
input_string = "ulas okayer bitirme odevim"

########## String'i 3D koordinatlara dönüştür
coords = string_to_3d_coords(input_string, key)
print("3D Koordinatlar:", coords)

########## 3D poligonları oluştur
polygons = create_polygons(coords)

########## 3D poligonları görselleştirme
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

########## Koordinatları ekleme
ax.scatter(coords[:, 0], coords[:, 1], coords[:, 2], c='r', marker='o')

########## Poligonları ekleme
poly3d = Poly3DCollection(polygons, alpha=0.7, linewidths=1, edgecolors='k', facecolors='cyan')
ax.add_collection3d(poly3d)

########## Grafik başlık ve etiketleri
ax.set_title('3D Polygons from String Coordinates')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

########## Gölge efektleri ekleme
ax.view_init(elev=20, azim=30)
ax.grid(True)

plt.show()

########## Verileri JSON formatında sakla
data = {
    'key': key,
    'coords': coords.tolist()
}

with open('data.json', 'w') as f:
    json.dump(data, f)

print("Veriler data.json dosyasına kaydedildi.")
