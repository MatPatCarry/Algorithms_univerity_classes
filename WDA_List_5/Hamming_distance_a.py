def hamming_distance(first, second):
    counter = 0
    for letter_index in range(len(first)):
        if first[letter_index] != second[letter_index]:
            counter += 1
        else:
            continue

    return counter


while True:
    first_string = input("Please, pass first string: ")
    second_string = input("Please, pass second string: ")
    if len(first_string) != len(second_string):
        print("Strings' length should be the same!")
        continue
    else:
        result = hamming_distance(first_string, second_string)
        print(result)
        once_again = input("One more time?: \n[1] Yes\n[2] No\n ")
        if once_again == 1:
            continue
        else:
            break

