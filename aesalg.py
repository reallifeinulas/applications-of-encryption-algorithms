from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.hmac import HMAC
from key import generate_complex_key, generate_complex_iv 
import os

# Rastgele bir anahtar ve başlangıç vektörü oluştur
key = generate_complex_key()  # Yeni anahtar oluştur
iv = generate_complex_iv()    # Yeni IV oluştur

# ANSIX923 Dolgusu
def pad_ansix923(data, block_size):
    pad_length = block_size - (len(data) % block_size)
    return data + bytes([0] * (pad_length - 1)) + bytes([pad_length])

# Dolguyu kaldırmak için
def unpad_ansix923(data):
    pad_length = data[-1]
    return data[:-pad_length]

# Şifreleme fonksiyonu
def encrypt(data, key, iv):
    # CBC modunda AES şifrelemesi
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    # Veriyi ANSIX923 ile dolgulama
    padded_data = pad_ansix923(data, 16)

    # Şifrele
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # HMAC ile doğrulama etiketi oluştur
    hmac = HMAC(key, hashes.SHA256())
    hmac.update(encrypted_data)
    mac_tag = hmac.finalize()

    return encrypted_data, mac_tag

# Deşifreleme fonksiyonu
def decrypt(encrypted_data, mac_tag, key, iv):
    # HMAC doğrulama
    hmac = HMAC(key, hashes.SHA256())
    hmac.update(encrypted_data)
    try:
        hmac.verify(mac_tag)  # Veri bütünlüğünü kontrol et
    except Exception as e:
        print("HMAC doğrulama başarısız oldu:", e)
        return None

    # CBC modunda AES deşifrelemesi
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    # Deşifrele ve dolgu byte'larını çıkar
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    
    # Dolguyu kaldırma
    data_without_padding = unpad_ansix923(decrypted_data)

    return data_without_padding

# UTF-8 ile veri dönüştürme
original_data = "Bu bir test mesajıdır. Şifreleme için kullanılıyor."
encoded_data = original_data.encode("utf-8")

# Şifreleme
encrypted_data, mac_tag = encrypt(encoded_data, key, iv)

# Deşifreleme
decrypted_data = decrypt(encrypted_data, mac_tag, key, iv)

# Deşifrelenmiş veriyi yeniden karakter dizisine dönüştür
decrypted_text = decrypted_data.decode("utf-8")

print("Şifrelenmiş veri:", encrypted_data)
print("Doğrulama etiketi:", mac_tag)
print("Deşifrelenmiş veri:", decrypted_text)
