# encryption by vigenere cipher
def encryption(text,key):
    cryp_text = ""
    key = key.upper()
    key_index = 0
    for ch in text :
        # to encrypt only charecters (numbers and punctuation marks remain unchanged during encryption)
        if ch.isalpha() :
            # to save the letter case
            # if the letter in upper case use ord('A') else use ord('a')
            # ord() -> return the value of the letter in ASCII code
            x= ord('A') if ch.isupper() else ord('a')
            c= ord(ch.upper())-ord('A')
            k = ord(key[key_index])-ord('A')
            vig_cip = (c+k)%26
            # exchange the number to a letter with saving the letter case
            cryp_chr = chr(vig_cip+x)
            cryp_text+=cryp_chr
            key_index = (key_index+1)%len(key)
            # if key_index<len(key)-1:
            #     key_index+=1
            # else :
            #     key_index=0
        else:
            cryp_text+=ch
    return cryp_text

# decryption by vigenere decrypt
def decryption(text,key):
    decryp_text = ""
    key = key.upper()
    key_index = 0
    for ch in text :
        if ch.isalpha() :
            # to save the latter case
            x= ord('A') if ch.isupper() else ord('a')
            c= ord(ch.upper())-ord('A')
            k = ord(key[key_index])-ord('A')
            # +26 to keep the value to be positive
            vig_decip = (c-k+26)%26
            decryp_chr = chr(vig_decip+x)
            decryp_text+=decryp_chr
            key_index = (key_index+1)%len(key)
            # if key_index<len(key)-1:
            #     key_index+=1
            # else :
            #     key_index=0
        else:
            decryp_text+=ch
    return decryp_text