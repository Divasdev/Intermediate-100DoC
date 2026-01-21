#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as file:
    letter_template = file.read()

with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

for name in names:
    clean_name = name.strip()
    personalized_letter = letter_template.replace("[name]", clean_name)

    with open(f"Output/ReadyToSend/letter_for_{clean_name}.txt", "w") as file:
        file.write(personalized_letter)
