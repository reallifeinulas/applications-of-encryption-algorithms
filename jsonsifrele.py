# Şifreleme ve Anahtar Oluşturma Kütüphanelerini Yükleme
from aesalg import encrypt
from key import generate_complex_key, generate_complex_iv
import json

# Adım 1: Anahtar ve IV Oluşturma
key = generate_complex_key()  # 256-bit AES anahtarı oluştur
iv = generate_complex_iv()  # 128-bit başlangıç vektörü oluştur

# Adım 2: JSON Dosyasını Okuma
# Mevcut dosya adını uygun şekilde değiştirin.
with open("data.json", "r") as f:
    json_data = json.load(f)  # JSON verisini yükle

# Adım 3: Veriyi Şifreleme
encoded_data = json.dumps(json_data).encode("utf-8")  # JSON'u UTF-8'e dönüştür
encrypted_data, mac_tag = encrypt(encoded_data, key, iv)  # Veriyi şifrele

# Adım 4: Şifrelenmiş Veriyi Kaydetme
# Şifrelenmiş veriyi ve doğrulama bilgisini farklı dosyalara kaydedin.
with open("encrypted_data.json", "wb") as f:
    f.write(encrypted_data)  # Şifrelenmiş veriyi kaydet
with open("mac_tag.bin", "wb") as f:
    f.write(mac_tag)  # HMAC doğrulama etiketini kaydet
with open("iv.bin", "wb") as f:
    f.write(iv)  # Başlangıç vektörünü kaydet

print("Veri şifrelendi ve kaydedildi.")
