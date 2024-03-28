def vigenere_encode(text, key):
    alphabet_eng = [chr(ord('a') + i) for i in range(26)]
    alphabet_rus = [chr(ord('а') + i) for i in range(32)]
    encrypted_text = ""
    key_length = len(key)

    for i, char in enumerate(text):
        if char.isalpha() and char in alphabet_eng:
            char_index = alphabet_eng.index(char.lower())
            key_char = key[i % key_length]
            if key_char in alphabet_eng:
                shift = alphabet_eng.index(key_char.lower())
            else:
                shift = alphabet_rus.index(key_char.lower())
            encrypted_char_index = (char_index + shift) % len(alphabet_eng)
            encrypted_char = alphabet_eng[encrypted_char_index]
            if char.isupper():
                encrypted_text += encrypted_char.upper()
            else:
                encrypted_text += encrypted_char
        elif char.isalpha() and char in alphabet_rus:
            char_index = alphabet_rus.index(char.lower())
            key_char = key[i % key_length]
            if key_char in alphabet_eng:
                shift = alphabet_eng.index(key_char.lower())
            else:
                shift = alphabet_rus.index(key_char.lower())
            encrypted_char_index = (char_index + shift) % len(alphabet_rus)
            encrypted_char = alphabet_rus[encrypted_char_index]
            if char.isupper():
                encrypted_text += encrypted_char.upper()
            else:
                encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def vigenere_decode(text, key):
    alphabet_eng = [chr(ord('a') + i) for i in range(26)]
    alphabet_rus = [chr(ord('а') + i) for i in range(32)]
    decrypted_text = ""
    key_length = len(key)
    
    for i, char in enumerate(text):
        if char.isalpha() and char in alphabet_eng:
            char_index = alphabet_eng.index(char.lower())
            key_char = key[i % key_length]
            if key_char in alphabet_eng:
                shift = alphabet_eng.index(key_char.lower())
            else:
                shift = alphabet_rus.index(key_char.lower())
            decrypted_char_index = (char_index - shift) % len(alphabet_eng)
            decrypted_char = alphabet_eng[decrypted_char_index]
            if char.isupper():
                decrypted_text += decrypted_char.upper()
            else:
                decrypted_text += decrypted_char
        elif char.isalpha() and char in alphabet_rus:
            char_index = alphabet_rus.index(char.lower())
            key_char = key[i % key_length]
            if key_char in alphabet_eng:
                shift = alphabet_eng.index(key_char.lower())
            else:
                shift = alphabet_rus.index(key_char.lower())
            decrypted_char_index = (char_index - shift) % len(alphabet_rus)
            decrypted_char = alphabet_rus[decrypted_char_index]
            if char.isupper():
                decrypted_text += decrypted_char.upper()
            else:
                decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

def is_valid_vigenere_key(key):
    alphabet = "".join([chr(ord('a') + i) for i in range(26)]) + "".join([chr(ord('а') + i) for i in range(32)])

    key = key.lower()
    
    if not key:
        return False
    
    for letter in key:
        if letter not in alphabet:
            return False
    
    return True