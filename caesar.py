# Caesar Cipher Encryption Script

key = int(input('Please enter a key: '))
message = input('Please enter a message to encrypt: ')

encrypted_message = ''
 
for letter in message:

  if letter.isalpha():
  
    ascii = ord(letter)
    ascii += (key % 26)


    if letter.isupper():

      if ascii > ord('Z'):

        ascii -= 26

      elif ascii < ord('A'):

        ascii += 26

    elif letter.islower():

      if ascii > ord('z'):

        ascii -= 26

      elif ascii < ord('a'):

        ascii += 26

    encrypted_message += chr(ascii)

  else:
    encrypted_message += letter

print('The encrypted message is ' + encrypted_message)
