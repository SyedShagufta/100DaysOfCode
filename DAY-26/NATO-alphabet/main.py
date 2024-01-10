import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
# df = pandas.read_csv("nato_phonetic_alphabet.csv")
# alpha_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(alpha_dict)
# # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# name = input("Enter a word:").upper()
# result = [alpha_dict[letter] for letter in name]
# print(result)


df = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter: row.code for (index, row) in df.iterrows()}
is_true = True

while is_true:
    try:
        name = input("Enter a word: ").upper()
        result = [alpha_dict[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        is_true = False
        print(result)
