from envsync.crypto import generate_key, encrypt_data, decrypt_data


def test_encrypt_decrypt():
    key = generate_key()

    original = "API_KEY=123"

    encrypted = encrypt_data(original, key)
    decrypted = decrypt_data(encrypted, key)

    assert decrypted == original