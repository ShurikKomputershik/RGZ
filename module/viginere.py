def vigenere_encode(text, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(text)):
        key_char = key[i % key_length]
        shift = ord(key_char)
        encrypted_char = chr((ord(text[i]) + shift) % 65536)  # 65536 для UTF-8
        encrypted_text += encrypted_char
    return encrypted_text

def vigenere_decode(text, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(text)):
        key_char = key[i % key_length]
        shift = ord(key_char)
        decrypted_char = chr((ord(text[i]) - shift) % 65536)  # 65536 для UTF-8
        decrypted_text += decrypted_char
    return decrypted_text


def is_valid_vigenere_key(key):
    alphabet = "abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрстуфхцчшщъыьэюя"
    key = key.lower()
    
    if not key:
        return False
    
    for letter in key:
        if letter not in alphabet:
            return False
    
    return True