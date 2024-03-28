def gronsfeld_encode(text, sequence):
    alphabet_eng = [chr(ord('a') + i) for i in range(26)]
    alphabet_rus = [chr(ord('а') + i) for i in range(32)]
    encrypted_text = ""
    sequence_length = len(sequence)
    
    for i, char in enumerate(text):
        if char.isalpha() and char in alphabet_eng:
            char_index = alphabet_eng.index(char.lower())  
            shift = int(sequence[i % sequence_length])  
            encrypted_char_index = (char_index + shift) % len(alphabet_eng)  
            encrypted_char = alphabet_eng[encrypted_char_index]
            if char.isupper():
                encrypted_text += encrypted_char.upper()
            else:
                encrypted_text += encrypted_char
        elif char.isalpha() and char in alphabet_rus:
            char_index = alphabet_rus.index(char.lower())  
            shift = int(sequence[i % sequence_length])  
            encrypted_char_index = (char_index + shift) % len(alphabet_rus)  
            encrypted_char = alphabet_rus[encrypted_char_index]
            if char.isupper():
                encrypted_text += encrypted_char.upper()
            else:
                encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    return encrypted_text

def gronsfeld_decode(encrypted_text, sequence):
    alphabet_eng = [chr(ord('a') + i) for i in range(26)]
    alphabet_rus = [chr(ord('а') + i) for i in range(32)]
    decrypted_text = ""
    sequence_length = len(sequence)
    
    for i, char in enumerate(encrypted_text):
        if char.isalpha() and char in alphabet_eng:
            char_index = alphabet_eng.index(char.lower())  
            shift = int(sequence[i % sequence_length])  
            decrypted_char_index = (char_index - shift) % len(alphabet_eng)  
            decrypted_char = alphabet_eng[decrypted_char_index]
            if char.isupper():
                decrypted_text += decrypted_char.upper()
            else:
                decrypted_text += decrypted_char
        elif char.isalpha() and char in alphabet_rus:
            char_index = alphabet_rus.index(char.lower())  
            shift = int(sequence[i % sequence_length])  
            decrypted_char_index = (char_index - shift) % len(alphabet_rus)  
            decrypted_char = alphabet_rus[decrypted_char_index]
            if char.isupper():
                decrypted_text += decrypted_char.upper()
            else:
                decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    return decrypted_text

def is_valid_gronsfeld_key(key):
    digits = "".join([chr(ord('0') + i) for i in range(10)])
    
    if not key:
        return False
    
    for char in key:
        if char not in digits:
            return False
    
    return True
