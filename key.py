import os
import secrets

def generate_complex_key():
    # AES-256 için 256 bit (32 bayt) anahtar oluşturur.
    return secrets.token_bytes(32)

def generate_complex_iv():
    # 128 bit (16 bayt) IV (Başlangıç Vektörü) oluşturur.
    return secrets.token_bytes(16)
