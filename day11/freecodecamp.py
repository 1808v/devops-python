#writing ceaser cipher 
#text = 'Hello World' #this is string
#shift = 3            #shift in cipher is 3 , it could be any value according to alphabets
#alphabet = 'abcdefghijklmnopqrstuvwxyz' #
#index = alphabet.find(text[0].lower()) # finding the value 1st index of "Hello World" in alphabet string
#print(index)                        # got value 7
#shifted = alphabet[index]           # getting the index value in alphabet 
#print(shifted)                      # got the value h
#shifted=alphabet[index+shift]       # adding the value of index and shift in shifted string
#print(shifted)                      # which will be (7+3=10)th value k
#Will be more typical to find and shift for every charachter so using for loop
#  
#text = 'Hello World'
#shift = 3
#alphabet = 'abcdefghijklmnopqrstuvwxyz'

#for char in text.lower():
#    index = alphabet.find(char)
#    print(char, index)
#    new_index = index + shift
#    new_char = alphabet[new_index]
#    print(new_char)

#text = 'Hello World'
#shift = 3
#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
#for char in text.lower():
#    index = alphabet.find(char)
#    new_index = index + shift
#    new_char = alphabet[new_index]
#    print('char:', char, 'new char:', new_char)
#
#text = 'Hello World'
#shift = 3
#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#encrypted_text = ''
#
#for char in text.lower():
#    if char == ' ':
#        print('space!')
#        #print(char == ' ') # removed 
#    index = alphabet.find(char)
#    new_index = index + shift
#    encrypted_text += alphabet[new_index]
#    print('char:', char, 'encrypted text:', encrypted_text)
#
#text = 'Hello Zaira'
#shift = 3
#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#encrypted_text = ''
#
#for char in text.lower():
#    if char == ' ':
#        encrypted_text += char
#    else:
#        index = alphabet.find(char)
#        new_index = (index + shift) % len(alphabet)
#        encrypted_text += alphabet[new_index]
#    print('char:', char, 'encrypted text:', encrypted_text)
#
#text = 'Hello Zaira'
#shift = 3
#alphabet = 'abcdefghijklmnopqrstuvwxyz'
#encrypted_text = ''
#
#for char in text.lower():
#    if char == ' ':
#        encrypted_text += char
#    else:
#        index = alphabet.find(char)
#        new_index = (index + shift) % len(alphabet)
#        encrypted_text += alphabet[new_index]
#print('encrypted text:', encrypted_text)
#
#
text = 'Hello Zaira'
shift = 3

def caesar():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in text.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + shift) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', text)
    print('encrypted text:', encrypted_text)