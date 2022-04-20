from Letter_frequency_a_and_c import polish, english, german
from math import fabs


def creating_relative_letter_frequency(text):
    text = text.lower()
    text.strip()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    tails = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z', 'ä': 'a', 'ö': 'o',
             'ß': 's', 'ü': 'u'}
    relative_letter_frequency = {}

    for letter_index in range(len(text)):
        for key, value in tails.items():
            if text[letter_index] == key:
                text = text[:letter_index] + value + text[letter_index + 1:]

    for let in alphabet:
        relative_letter_frequency[let] = 0

    for letter in text:
        if letter in relative_letter_frequency.keys():
            relative_letter_frequency[letter] += 1

    amount_of_letters = 0
    for value in relative_letter_frequency.values():
        amount_of_letters += value

    for k, v in relative_letter_frequency.items():
        relative_letter_frequency[k] = v / amount_of_letters

    return relative_letter_frequency


def comparison(table):

    languages = [polish, english, german]
    languages_names = ['polish', 'english', 'german']
    language_index = 0
    results = {}
    values = []

    for language in languages:
        distance = 0
        for key in table.keys():
            distance += fabs(table[key] - language[key])

        results[languages_names[language_index]] = distance
        values.append(distance)

        language_index += 1

    print(results)

    the_most_similar_language_value = min(values)
    for k, v in results.items():
        if v == the_most_similar_language_value:
            print(f'The most similar language is {str(k)}.')


