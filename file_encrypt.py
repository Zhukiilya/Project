from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
# 0 публичные и приватные ключи RSA для цифровой подписи, их обмен
from cryptography.hazmat.primitives.asymmetric import rsa, padding
private_rsa_key_a = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4096,  # Длина модуля n = 4096 бит
    backend=default_backend()
)
public_rsa_key_a = private_key.public_key()
n_ae = public_rsa_key_a.public_numbers().n

n_ae_bytes = n_ae.to_bytes((n.bit_length() + 7) // 8, byteorder="big")
S_a = private_rsa_key_a.sign(n_ae_bytes, padding=padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=32), algorithm=hashes.SHA256())
#
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives import serialization

# 1. Генерация приватного ключа отправителя d_a ключей (d_a и d_b)
d_a = X25519PrivateKey.generate()
d_b = X25519PrivateKey.generate()

# 2.1 и 2.2 Получение публичных ключей (P_ax и P_bx)
P_ax = d_a.public_key()
P_bx = d_b.public_key()

#Сериализация ключей в стандартный формат (32-байтные x-координаты)
public_key_a_bytes = public_key_a.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)

public_key_b_bytes = public_key_b.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)

# 3. Вычисление общего секрета (с обеих сторон)
shared_secret_a = private_key_a.exchange(public_key_b)
shared_secret_b = private_key_b.exchange(public_key_a)

# Проверка совпадения секретов
assert shared_secret_a == shared_secret_b

print("Общий секрет:", shared_secret_a.hex())
