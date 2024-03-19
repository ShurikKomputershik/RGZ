# def vigenere_encode(plaintext, keyword):
#     ciphertext = ""
#     keyword = keyword.upper()
#     plaintext = plaintext.upper()
#     key_index = 0
#     for letter in plaintext:
#         if letter.isalpha():
#             offset = ord('A')
#             keyword_letter = keyword[key_index]
#             key_letter_index = ord(keyword_letter) - offset
#             letter_index = ord(letter) - offset
#             ciphertext += chr(((letter_index + key_letter_index) % 26) + offset)
#             # print(f"{chr(((letter_index + key_letter_index) % 26) + offset)} = ({letter_index} + {key_letter_index}) + {offset}")
#             key_index = (key_index + 1) % len(keyword)
#         else:
#             ciphertext += letter
#     return ciphertext

# def vigenere_decode(ciphertext, keyword):
#     plaintext = ""
#     keyword = keyword.upper()
#     ciphertext = ciphertext.upper()
#     key_index = 0
#     for letter in ciphertext:
#         if letter.isalpha():
#             offset = ord('A')
#             keyword_letter = keyword[key_index]
#             key_letter_index = ord(keyword_letter) - offset
#             letter_index = ord(letter) - offset
#             plaintext += chr(((letter_index - key_letter_index) % 26) + offset)
#             # print(f"{chr(((letter_index - key_letter_index) % 26) + offset)} = ({letter_index} - {key_letter_index}) % 26 + {offset}")
#             key_index = (key_index + 1) % len(keyword)
#         else:
#             plaintext += letter
#     return plaintext 

def vigenere_encode(plaintext, keyword):
    ciphertext = ""
    keyword = keyword.upper()
    key_index = 0
    for i, letter in enumerate(plaintext):
        if letter.isalpha():
            offset = ord('A') if letter.isupper() else ord('a')
            keyword_letter = keyword[key_index]
            key_letter_index = ord(keyword_letter) - ord('A')
            letter_index = ord(letter) - offset
            new_letter = chr(((letter_index + key_letter_index) % 26) + offset)
            print(f"{new_letter} = ({chr(letter_index + offset)} + {chr(key_letter_index + ord('A'))}) % 26 + {chr(offset)}")
            ciphertext += new_letter.upper() if letter.isupper() else new_letter.lower()
            key_index = (key_index + 1) % len(keyword)
        else:
            ciphertext += letter
    return ciphertext

def vigenere_decode(ciphertext, keyword):
    plaintext = ""
    keyword = keyword.upper()
    key_index = 0
    for i, letter in enumerate(ciphertext):
        if letter.isalpha():
            offset = ord('A') if letter.isupper() else ord('a')
            keyword_letter = keyword[key_index]
            key_letter_index = ord(keyword_letter) - ord('A')
            letter_index = ord(letter) - offset
            new_letter = chr(((letter_index - key_letter_index) % 26) + offset)
            print(f"{new_letter} = ({chr(letter_index + offset)} - {chr(key_letter_index + ord('A'))}) % 26 + {chr(offset)}")
            plaintext += new_letter.upper() if letter.isupper() else new_letter.lower()
            key_index = (key_index + 1) % len(keyword)
        else:
            plaintext += letter
    return plaintext


def is_valid_vigenere_key(key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key.lower()
    
    if not key:
        return False
    
    for char in key:
        if char not in alphabet:
            return False
    
    return True