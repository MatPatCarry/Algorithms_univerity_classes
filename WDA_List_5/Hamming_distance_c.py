from Hamming_distance_b import modified_hamming_distance
with open("100words.txt", 'r+', encoding="utf-8") as file:
    additional_list = file.readlines()

words = []
for word in additional_list:
    words.append((word[:len(word)-1]).lower())

while True:
    passed_word = input("Please, pass selected word: ")
    word_length = len(passed_word)
    if word_length < 3:
        print("Word is too short!")
        continue

    if passed_word in words:
        print("OK")
    else:
        available_words = []
        for element in words:
            if len(element) == word_length:
                available_words.append(element)
        results = {}
        values = []
        most_similar_words = []
        most_similar_words_values = []
        for w in available_words:
            distance = modified_hamming_distance(passed_word, w)
            results[w] = distance
            values.append(distance)

        minimum = min(values)

        for key, value in results.items():
            if value == minimum:
                most_similar_words.append(key)
                most_similar_words_values.append(value)

        for item in range(len(most_similar_words)):
            print(f'{most_similar_words[item]} - {most_similar_words_values[item]}')
            if item == 2:
                break
    once_again = input("One more time?: \n[1] Yes\n[2] No\n ")
    if once_again == '1':
        continue
    else:
        break
