# Deşifreleme için kütüphaneleri yükleme
from aesalg import decrypt
from key import generate_complex_key
import json

# Adım 1: IV ve Doğrulama Etiketini Yükleme
# Şifrelenmiş veriyi deşifrelemek için başlangıç vektörü ve HMAC doğrulama etiketi gereklidir.
with open("iv.bin", "rb") as f:
    iv = f.read()  # Başlangıç vektörünü oku
with open("mac_tag.bin", "rb") as f:
    mac_tag = f.read()  # HMAC doğrulama etiketini oku
key = generate_complex_key()  # Anahtar oluştur (güvenli değil, aynı anahtarı kullanmalısınız)

# Adım 2: Şifrelenmiş Veriyi Okuma
with open("encrypted_data.json", "rb") as f:
    encrypted_data = f.read()  # Şifrelenmiş veriyi oku

# Adım 3: Veriyi Deşifreleme
# Doğrulama etiketi ve anahtar ile birlikte şifrelenmiş veriyi deşifre eder.
decrypted_data = decrypt(encrypted_data, mac_tag, key, iv)

# Adım 4: Deşifrelenmiş Veriyi JSON'a Dönüştürme
if decrypted_data:
    json_data = json.loads(decrypted_data.decode("utf-8"))  # JSON'a dönüştür
    print("Deşifrelenmiş veri:", json.dumps(json_data, indent=2))
else:
    print("Deşifreleme başarısız oldu. HMAC doğrulaması geçersiz olabilir.")
