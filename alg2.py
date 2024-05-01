import hashlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Metni al ve hash'e dönüştür
def text_to_hash(text):
    # SHA-256 hash fonksiyonunu kullan
    return hashlib.sha256(text.encode()).hexdigest()

# Hash'i 3 boyutlu koordinatlara dönüştür
def hash_to_3d_points(hash_str):
    # Hash'i 6 karakterlik bloklara ayırarak 3D koordinatlar oluştur
    points = []
    for i in range(0, len(hash_str), 6):
        num = int(hash_str[i:i+6], 16)  # 16'lık tabandan 10'luk tabana dönüştür
        x = (num % 100) / 10  # 0-10 arası ölçekle
        y = ((num // 100) % 100) / 10
        z = ((num // 10000) % 100) / 10
        points.append((x, y, z))
    return points

# 3 boyutlu noktaları grafik olarak göster ve aralarındaki bağlantıları çiz
def visualize_3d(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # X, Y, Z koordinatlarını al
    x_vals = [p[0] for p in points]
    y_vals = [p[1] for p in points]
    z_vals = [p[2] for p in points]

    # Noktaları scatter plot olarak ekle
    ax.scatter(x_vals, y_vals, z_vals)

    # Noktaları birbirine bağlayan çizgileri ekle
    # Her noktayı bir sonrakiyle bağla
    for i in range(len(points) - 1):
        ax.plot([x_vals[i], x_vals[i + 1]], 
                [y_vals[i], y_vals[i + 1]], 
                [z_vals[i], z_vals[i + 1]], 'k-')  # Siyah çizgiyle bağla

    ax.set_xlabel('X Eksen')
    ax.set_ylabel('Y Eksen')
    ax.set_zlabel('Z Eksen')

    plt.show()

# Terminalden girdi al
text = input("Bir metin girin: ")

# Metni hash'e dönüştür
hash_str = text_to_hash(text)

# Hash'i 3 boyutlu noktalara dönüştür
points = hash_to_3d_points(hash_str)

# 3 boyutlu grafiği aralarındaki bağlantılarla görselleştir
visualize_3d(points)
