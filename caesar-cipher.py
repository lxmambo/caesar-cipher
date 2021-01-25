alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

alphabet_length = len(alphabet)

def encrypt(text_str, shift):
  print("just starting")
  encrypted_text = []
  for letter in text_str:
    if letter != ' ':
      letter_idx = alphabet.index(letter)
      if letter_idx + shift <=25:
        encrypted_text.append(alphabet[letter_idx + shift])
      else:
        go_around_shift = letter_idx + shift - alphabet_length
        encrypted_text.append(alphabet[go_around_shift])
    else:
      encrypted_text.append(' ')

  #Join all the elements in the list and turn it into a String.
  print(f"the encoded text is {' '.join(encrypted_text)}\n")

def decrypt(text, shift):
  deciphered_text = ""
  for letter in text:
    if letter != ' ':
      position = alphabet.index(letter)
      if position - shift < 0:
        new_position = alphabet_length + position - shift
        deciphered_text += alphabet[new_position]
      else:
        new_position = position - shift
        deciphered_text += alphabet[new_position]
    else:
      deciphered_text += ' '
  print(f"the decoded text is {deciphered_text}")

if direction == 'encode':
  text_str = []
  for letter in text:
    text_str.append(letter)
  encrypt(text_str,shift)
elif direction == 'decode':
  decrypt(text, shift)

