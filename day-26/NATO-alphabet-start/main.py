import pandas
alphabet_dataframe=pandas.read_csv("nato_phonetic_alphabet.csv")


alphabet_dict={row.letter:row.code
               for (index,row) in alphabet_dataframe.iterrows()
               }
print(alphabet_dict)

def generate_phonetic():
    user_word = input("Enter a word: ").upper()
    try:
        phonetic_list = [alphabet_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry Only Alphabet letter")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()
