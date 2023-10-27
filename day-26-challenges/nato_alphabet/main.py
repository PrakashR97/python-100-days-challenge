import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}
print(phonetic_dict)

name = "Prakash"
# phonetic_word = []
# for i in name.upper():
#     # phonetic_word.append([j for k, j in new_dict.items() if i == k])
#     for k, j in phonetic_dict.items():
#         if i == k:
#             phonetic_word.append(j)
# print(phonetic_word)

phonetic_word = [phonetic_dict[i] for i in name.upper()]
print(phonetic_word)
