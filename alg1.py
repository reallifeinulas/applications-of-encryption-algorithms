import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

harf_koordinatlari = {
    "A": (0.25, 0.75, 0.5),
    "B": (0.75, 0.25, 0.5),
    "C": (0.5, 0.25, 0.25),
    "D": (0.25, 0.5, 0.25),
    "E": (0.75, 0.5, 0.25),
    "F": (0.5, 0.75, 0.25),
    "G": (0.25, 0.25, 0.75),
    "H": (0.75, 0.25, 0.75),
    "I": (0.5, 0.25, 0.75),
    "J": (0.25, 0.5, 0.75),
    "K": (0.75, 0.5, 0.75),
    "L": (0.5, 0.75, 0.75),
    "M": (0.25, 0.25, 0.5),
    "N": (0.75, 0.25, 0.5),
    "O": (0.5, 0.25, 0.5),
    "P": (0.25, 0.5, 0.5),
    "Q": (0.75, 0.5, 0.5),
    "R": (0.5, 0.75, 0.5),
    "S": (0.25, 0.75, 0.25),
    "T": (0.75, 0.75, 0.25),
    "U": (0.5, 0.75, 0.25),
    "V": (0.25, 0.5, 0.25),
    "W": (0.75, 0.5, 0.25),
    "X": (0.5, 0.25, 0.25),
    "Y": (0.25, 0.75, 0.75),
    "Z": (0.75, 0.75, 0.75),
    "0": (0.4, 0.4, 0),
    "1": (0.6, 0.4, 0),
    "2": (0.8, 0.4, 0),
    "3": (0.4, 0.6, 0),
    "4": (0.6, 0.6, 0),
    "5": (0.8, 0.6, 0),
    "6": (0.4, 0.8, 0),
    "7": (0.6, 0.8, 0),
    "8": (0.8, 0.8, 0),
    "9": (0.5, 0.5, 0.5)  # Nokta (.) için koordinat
}

def text_to_3d(text):
    # Metnin uzunluğunu al
    length = len(text)
    
    # 3D grafik oluşturma
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Küplerin boyutu
    cube_size = 0.1
    
    # Her bir harf için bir küp oluştur
    for i, char in enumerate(text):
        # Koordinatları sözlükten alma
        x, y, z = harf_koordinatlari[char]

        # Küpü çizme
        ax.bar3d(x, y, z, cube_size, cube_size, cube_size, color='gray')

    
    # Eksenleri gizle
    ax.set_axis_off()
    
    # Gösterme
    plt.show()

# Örnek Kullanım
text = input("Şifrelemek istediğiniz metni girin: ")
text_to_3d(text)
