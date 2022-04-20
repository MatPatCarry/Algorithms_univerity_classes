def the_longest_common_substring_with_breaks(first, second):

    global result
    global substring

    for letter_index_1 in range(len(first)):
        for letter_index_2 in range(len(second)):
            if second[letter_index_2] == first[letter_index_1]:
                new_first_string = first[letter_index_1:]
                new_second_string = second[letter_index_2:]
                counter = 0
                current_substring = ''
                possible_iterations = min(len(new_first_string), len(new_second_string))
                for letter_index in range(possible_iterations):
                    if new_first_string[letter_index] == new_second_string[letter_index]:
                        counter += 1
                        current_substring += new_first_string[letter_index]
                        if letter_index == possible_iterations - 1:
                            result += counter
                            substring += current_substring

                            return result, substring

                        else:
                            continue
                    else:
                        result += counter
                        substring += current_substring
                        return the_longest_common_substring_with_breaks(new_first_string[letter_index:],
                                                                        new_second_string[letter_index:])


'złożoność obliczeniowa to n^3 w najgorszym przypadku'


while True:
    result = 0
    substring = ''
    to_show = the_longest_common_substring_with_breaks(input("Please, pass first string: "),
                                                       input("Please, pass second string: "))
    print(f"Substring's length: {to_show[0]}, substring: '{to_show[1]}'")
    once_again = input("One more time?: \n[1] Yes\n[2] No\n ")
    if once_again == 1:
        continue
    else:
        break

