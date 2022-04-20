import json

polish_relative_frequency = {}
english_relative_frequency = {}
german_relative_frequency = {}
languages = [polish_relative_frequency, german_relative_frequency, english_relative_frequency]

with open("frequency.json") as file:
    data = json.load(file)

i = 0
for language in languages:
    for letter in data.keys():
        language[letter] = data[letter][i]
    i += 1

polish = polish_relative_frequency.copy()
english = english_relative_frequency.copy()
german = german_relative_frequency.copy()

"c"
polish_relative_vowels_frequency = {}
english_relative_vowels_frequency = {}
german_relative_vowels_frequency = {}
polish_relative_consonants_frequency = {}
english_relative_consonants_frequency = {}
german_relative_consonants_frequency = {}

polish_tables = [polish_relative_vowels_frequency, polish_relative_consonants_frequency]
english_tables = [english_relative_vowels_frequency, english_relative_consonants_frequency]
german_tables = [german_relative_vowels_frequency, german_relative_consonants_frequency]


def creating_specified_tables(tables, index):

    vowels = 'aeiouy'
    consonants = 'bcdfghjklmnpqrstvwxz'
    additional_v = []
    additional_c = []

    for let in data.keys():
        if let in vowels:
            additional_v.append(data[let][index])
        elif let in consonants:
            additional_c.append(data[let][index])
        else:
            continue

    sum_of_vowels = sum(additional_v)
    sum_of_consonants = sum(additional_c)

    vowels_values = map(lambda x: x / sum_of_vowels, additional_v)
    consonants_values = map(lambda y: y / sum_of_consonants, additional_c)
    vowels_values = list(vowels_values)
    consonants_values = list(consonants_values)

    v_index = 0
    c_index = 0

    for v in vowels:
        tables[0][v] = vowels_values[v_index]
        v_index += 1

    for c in consonants:
        tables[1][c] = consonants_values[c_index]
        c_index += 1

    return tables


polish_tables_to_import = creating_specified_tables(polish_tables, 0)
german_tables_to_import = creating_specified_tables(german_tables, 1)
english_tables_to_import = creating_specified_tables(english_tables, 2)


