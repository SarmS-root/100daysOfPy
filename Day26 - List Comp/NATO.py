import pandas as pd

df = pd.read_table("nato_phonetic_alphabet.csv", delimiter=",")

#This for loop was turned into the following list comp above...
# for (index, row) in df.iterrows():
#     print(row.code)
dict = { row.letter:row.code for (index, row) in df.iterrows()}
 
print(dict)

word = input("Type the word...")


result = [dict[letter.upper()] for letter in word]
print(result)
