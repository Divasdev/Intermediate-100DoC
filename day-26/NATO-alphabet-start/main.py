import pandas


#TODO 1. Create a dictionary in this format:

alphabet_dataframe=pandas.read_csv("nato_phonetic_alphabet.csv")
print(alphabet_dataframe)

alphabet_dict={row.letter:row.code
               for (index,row) in alphabet_dataframe.iterrows()
               }

print(alphabet_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_word = input("Enter a word: ").upper()

phonetic_list = [alphabet_dict[letter] for letter in user_word]

print(phonetic_list)
