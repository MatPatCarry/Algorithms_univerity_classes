def the_longest_common_substring(first, second):

    results = []
    strings = []

    for letter_index_1 in range(len(first)):
        for letter_index_2 in range(len(second)):
            if second[letter_index_2] == first[letter_index_1]:
                new_first_string = first[letter_index_1:]
                new_second_string = second[letter_index_2:]
                counter = 0
                substring = ''
                possible_iterations = min(len(new_first_string), len(new_second_string))
                for letter_index in range(possible_iterations):
                    if new_first_string[letter_index] == new_second_string[letter_index]:
                        counter += 1
                        substring += new_first_string[letter_index]
                        if letter_index == possible_iterations - 1:
                            results.append(counter)
                            strings.append(substring)

                        else:
                            continue
                    else:
                        results.append(counter)
                        strings.append(substring)
                        break

    current = 0
    the_longest = ''

    for element in strings:
        if len(element) > current:
            the_longest = element
            current = len(element)

    return max(results), the_longest


'złożoność obliczeniowa to n^3 w najgorszym przypadku'


while True:
    result = the_longest_common_substring(input("Please, pass first string: "), input("Please, pass second string: "))
    print(f"Substring's length: {result[0]}, substring: '{result[1]}'")
    once_again = input("One more time?: \n[1] Yes\n[2] No\n ")
    if once_again == 1:
        continue
    else:
        break
