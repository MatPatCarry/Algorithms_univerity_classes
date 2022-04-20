from Letter_frequency_a_and_c import polish_tables_to_import, english_tables_to_import, german_tables_to_import
from math import fabs


def getting_frequencies(table):

    sum_of_letters = 0

    for value in table.values():
        sum_of_letters += value

    for k, v in table.items():
        if sum_of_letters != 0:
            table[k] = v / sum_of_letters

    return table


def creating_relative_letter_frequencies2(text):
    text = text.lower()
    text.strip()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels = 'aeiouy'
    tails = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z', 'ä': 'a', 'ö': 'o',
             'ß': 's', 'ü': 'u'}
    relative_vowel_frequency = {}
    relative_consonant_frequency = {}

    for letter_index in range(len(text)):
        for key, value in tails.items():
            if text[letter_index] == key:
                text = text[:letter_index] + value + text[letter_index + 1:]

    for let in alphabet:
        if let in vowels:
            relative_vowel_frequency[let] = 0
        else:
            relative_consonant_frequency[let] = 0

    for letter in text:
        if letter in relative_vowel_frequency:
            relative_vowel_frequency[letter] += 1
        elif letter in relative_consonant_frequency:
            relative_consonant_frequency[letter] += 1
        else:
            continue

    getting_frequencies(relative_vowel_frequency)
    getting_frequencies(relative_consonant_frequency)
    tables = [relative_vowel_frequency, relative_consonant_frequency]

    return tables


def specified_comparison(tables):

    languages_names = ['polish', 'english', 'german']
    languages = [polish_tables_to_import, english_tables_to_import, german_tables_to_import]
    language_index_v = 0
    language_index_c = 0
    vowels_results = {}
    consonants_results = {}
    vowels_values = []
    consonants_values = []

    for language in languages:

        distance_v = 0
        distance_c = 0

        for key in (tables[0]).keys():
            distance_v += fabs(tables[0][key] - language[0][key])

        vowels_results[languages_names[language_index_v]] = distance_v
        vowels_values.append(distance_v)
        language_index_v += 1

        for key in (tables[1]).keys():
            distance_c += fabs(tables[1][key] - language[1][key])

        consonants_results[languages_names[language_index_c]] = distance_c
        consonants_values.append(distance_c)
        language_index_c += 1

    print(f'Vowels:\n{vowels_results}\nConsonants:\n{consonants_results}')

    the_most_similar_language_vowels_value = min(vowels_values)
    the_most_similar_language_consonants_value = min(consonants_values)

    for k, v in vowels_results.items():
        if v == the_most_similar_language_vowels_value:
            print(f'The most similar language when we look only at vowels is {str(k)}.')

    for k, v in consonants_results.items():
        if v == the_most_similar_language_consonants_value:
            print(f'The most similar language when we look only at consonants is {str(k)}.')

