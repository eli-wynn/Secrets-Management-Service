from app.services.crypto import encrypt, decrypt

def test_encrypt_decrypt():
    value = "supersecret"
    encrypted = encrypt(value)
    assert decrypt(encrypted) == value
