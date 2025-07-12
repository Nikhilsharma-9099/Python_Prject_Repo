from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
text = input("Type your message:\n").lower()

for character in text:
    if character not in alphabet:
        print(input("Enter a valid message: "))
          
        
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_message = ""
    
    for letter in original_text:
        pos = alphabet.index(letter) + shift_amount
        pos = pos%len(alphabet)
        encrypted_message+= alphabet[pos]
        
    return encrypted_message


def decrypt(original_text, shift_amount):
    encrypted_message = ""
    
    for letter in original_text:
        pos = alphabet.index(letter) - shift_amount
        pos = pos%len(alphabet)
        encrypted_message+= alphabet[pos]
        
    return encrypted_message

def caesar(dir, msg, sft):
    if dir=="encode":
        return encrypt(original_text=msg, shift_amount=sft)
    
    else:
        return decrypt(original_text=msg, shift_amount=sft)
    

print(caesar(dir=direction, msg=text, sft=shift))

choice = input("Do you want to play again ? Type 'yes' or 'no'").lower()

while choice=='yes':
    print(logo)
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    
    text = input("Type your message:\n").lower()

    for character in text:
        if character not in alphabet:
            print(input("Enter a valid message: "))
          
        
    shift = int(input("Type the shift number:\n"))
    
    print(caesar(dir=direction, msg=text, sft=shift))
    
    choice = input("Do you want to play again ? Type 'yes' or 'no'").lower()
    
    if choice=='no':
        break
    
print("GAME OVER!!")
    
    
    
