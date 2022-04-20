def modified_hamming_distance(first, second):
    neighbors = {'a': 'qwsz', 'b': 'nhgv', 'c': 'vfdx', 'd': 'resxcf', 'e': 'wsdfr', 'f': 'trdcvg', 'g': 'ytfvbh',
                 'h': 'juygbn', 'i': 'ujko', 'j': 'iuhnmk', 'k': 'mjiol', 'l': 'pok', 'm': 'njk', 'n': 'mjhb',
                 'o': 'plki', 'p': 'ol', 'q': 'wa', 'r': 'edfgt', 's': 'dewazx', 't': 'rfghy', 'u': 'yhjki',
                 'v': 'bgfc', 'w': 'qasde', 'x': 'zsdc', 'y': 'tghju', 'z': 'asx'}

    tails = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}

    first = first.lower()
    second = second.lower()
    counter = 0

    for letter_index in range(len(first)):
        for key, value in tails.items():
            if first[letter_index] == key:
                first = first[:letter_index] + value + first[letter_index + 1:]
            if second[letter_index] == key:
                second = second[:letter_index] + value + second[letter_index + 1:]

    for l_index in range(len(first)):
        if first[l_index] == second[l_index]:
            continue
        else:
            if second[l_index] in neighbors[first[l_index]]:
                counter += 1
            else:
                counter += 2

    return counter


while True:
    first_string = input("Please, pass first string: ")
    second_string = input("Please, pass second string: ")
    if len(first_string) != len(second_string):
        print("Strings' length should be the same!")
        continue
    else:
        result = modified_hamming_distance(first_string, second_string)
        print(result)
        once_again = input("One more time?: \n[1] Yes\n[2] No\n ")
        if once_again == '1':
            continue
        else:
            break
