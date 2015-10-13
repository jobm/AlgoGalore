# Using the Python, have the function CaesarCipher(str,num) take the str parameter and perform a Caesar Cipher shift
# on it using the num parameter as the shifting number.
# A Caesar Cipher works by shifting each letter in the
# string N places down in the alphabet (in this case N will be num).
# Punctuation, spaces, and capitalization should remain intact.
# For example if the string is "Caesar Cipher" and num is 2 the output should be "Ecguct Ekrjgt".

# to read more about ceaser's cipher visit http://practicalcryptography.com/ciphers/caesar-cipher/ or google some more
# happy coding :-)

import string
def capitalizer(str_input):
    list_words = str_input.split( )
    list_split = []
    for word in list_words:
       list_split.append(word.replace(word[0],word[0].upper()))
    return ' '.join(list_split)


def cipher(sentence,step):
    cipher = []
    alphabets = string.ascii_lowercase
    alphabets_tuples = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    alpha_cipher = ''
    spaces_index = [pos for pos, char in enumerate(sentence) if char == ' ']
    for char in sentence.lower(): 
        if char in alphabets:
            alpha_cipher = alphabets.index(char) + step
            if alphabets.index(char) + step >= 25:
                alpha_cipher = alpha_cipher % 25
        cipher.append(alphabets_tuples[alpha_cipher])
    for i in spaces_index:
        cipher[i] = ' '
    return capitalizer(''.join(cipher))

print cipher("Caesar Cipher",2)


