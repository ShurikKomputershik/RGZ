def atbash_encode(text):
    ciphertext = ''
    for char in text:
        if ord('a') <= ord(char) <= ord('z'):
            encrypted_char = chr(ord('a') + ord('z') - ord(char))
        elif ord('A') <= ord(char) <= ord('Z'):
            encrypted_char = chr(ord('A') + ord('Z') - ord(char))
        elif ord('а') <= ord(char) <= ord('я'):
            encrypted_char = chr(ord('а') + ord('я') - ord(char))
        elif ord('А') <= ord(char) <= ord('Я'):
            encrypted_char = chr(ord('А') + ord('Я') - ord(char))
        else:
            encrypted_char = char
        ciphertext += encrypted_char
    return ciphertext

def atbash_decode(ciphertext):
    plaintext = atbash_encode(ciphertext)  
    return plaintext