from Letter_frequency_b_functions import creating_relative_letter_frequency, comparison

with open('Inwokacja', 'r+', encoding='utf-8') as inwokacja:
    polish_data = inwokacja.read()

with open('Romeo_and_juliet', 'r+') as romeo_and_juliet:
    english_data = romeo_and_juliet.read()

with open('Stille Nacht', 'r+', encoding='utf-8') as stille_nacht:
    german_data = stille_nacht.read()

print('1. Polish text')
test1 = comparison(creating_relative_letter_frequency(polish_data))
print('\n2. English text')
test2 = comparison(creating_relative_letter_frequency(english_data))
print('\n3. German text')
test3 = comparison(creating_relative_letter_frequency(german_data))