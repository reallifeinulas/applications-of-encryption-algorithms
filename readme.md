aesalg.py dosyası, AES-256 algoritması kullanarak veri şifreleme ve deşifreleme işlemlerini gerçekleştirir:

generate_complex_key(), AES-256 için 256 bitlik (32 bayt) rastgele bir anahtar üretir.
generate_complex_iv(), 128 bitlik (16 bayt) rastgele bir başlangıç vektörü oluşturur.

- Veriyi ANSIX923 dolgusu ile pad eder.
- AES-256 CBC modunda şifreleme yapar.
- Şifrelenmiş veriye ek olarak HMAC kullanarak doğrulama etiketi oluşturur.


key.py dosyası, güvenli anahtarlar ve başlangıç vektörleri oluşturur:

generate_complex_key(), AES-256 için 256 bitlik (32 bayt) rastgele bir anahtar üretir.
generate_complex_iv(), 128 bitlik (16 bayt) rastgele bir başlangıç vektörü oluşturur.




https://github.com/reallifeinulas/applications-of-encryption-algorithms/assets/96961115/7ddb9160-77f3-4cb7-9cd2-bb9c7668b8fd

