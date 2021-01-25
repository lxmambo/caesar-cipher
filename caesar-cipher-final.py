import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(plain_text,shift_amount,direction):
  text = ""

  if direction == 'decode':
    shift_amount *= -1

  if shift_amount > 26:
    shift_amount = shift_amount % 26
  
  for letter in plain_text:
      if letter in alphabet:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        text += alphabet[new_position]
      else:
        text += letter

  print(f"The {direction}d text is {text}")

lets_go = True
while(lets_go):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(plain_text=text,shift_amount=shift,direction=direction)
  do_it_again = input("type 'yes' if you want to repeat. Otherwise type 'no.\n").lower()
  if do_it_again == 'no':
    lets_go = False
    print("thank you and good bye!")