def atbash_encode(text):
    ciphertext = ''
    alphabet_eng = [chr(ord('a') + i) for i in range(26)]
    alphabet_rus = [chr(ord('а') + i) for i in range(32)]
    for char in text:
        if char.islower():
            index = ord('z') - ord(char) + ord('a')
            encrypted_char = alphabet_eng[index - ord('a')]
        elif char.isupper():
            index = ord('Z') - ord(char) + ord('A')
            encrypted_char = alphabet_eng[index - ord('A')].upper()
        elif char >= 'а' and char <= 'я':
            index = ord('я') - ord(char) + ord('а')
            encrypted_char = alphabet_rus[index - ord('а')]
        elif char >= 'А' and char <= 'Я':
            index = ord('Я') - ord(char) + ord('А')
            encrypted_char = alphabet_rus[index - ord('А')].upper()
        else:
            encrypted_char = char
        ciphertext += encrypted_char
    return ciphertext


def atbash_decode(ciphertext):
    plaintext = atbash_encode(ciphertext)  
    return plaintext