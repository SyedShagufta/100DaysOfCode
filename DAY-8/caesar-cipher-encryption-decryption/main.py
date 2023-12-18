def caesar_cipher(text, shift, direction='encrypt'):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = alphabet.index(char.lower())

            if direction == 'encrypt':
                new_index = (char_index + shift) % 26
            elif direction == 'decrypt':
                new_index = (char_index - shift) % 26
            else:
                raise ValueError("Invalid direction. Use 'encrypt' or 'decrypt'.")

            new_char = alphabet[new_index]
            result += new_char.upper() if is_upper else new_char
        else:
            result += char

    return result

game_is_on = True

while game_is_on:
    direction = input("Type 'encrypt' to encrypt, 'decrypt' to decrypt:\n")
    text = input("Enter the message:\n")
    shift = int(input("Enter the shift number:\n"))

    if direction == 'encrypt' or direction == 'decrypt':
        result = caesar_cipher(text, shift, direction)
        print(f"Result: {result}")
    else:
        print("Invalid direction. Please use 'encrypt' or 'decrypt'.")

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        game_is_on = False
        print("Goodbye")
