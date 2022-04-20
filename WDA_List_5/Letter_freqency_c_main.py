from Letter_frequency_c_functions import creating_relative_letter_frequencies2, specified_comparison

with open('Inwokacja', 'r+', encoding='utf-8') as inwokacja:
    polish_data = inwokacja.read()

with open('Romeo_and_juliet', 'r+') as romeo_and_juliet:
    english_data = romeo_and_juliet.read()

with open('Stille Nacht', 'r+', encoding='utf-8') as stille_nacht:
    german_data = stille_nacht.read()

print('1. Polish text')
test1 = specified_comparison(creating_relative_letter_frequencies2(polish_data))
print('\n2. English text')
test2 = specified_comparison(creating_relative_letter_frequencies2(english_data))
print('\n3. German text')
test3 = specified_comparison(creating_relative_letter_frequencies2(german_data))
