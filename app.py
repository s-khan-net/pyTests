def print_wassup():
    #numbers = [item * 2 for item in range(5)]
    # print(numbers)
    sentence = "This is a common interview question"
    char_frequency = {}
    for char in sentence:
        if char in char_frequency:
            char_frequency[char] += 1
        if char not in char_frequency:
            char_frequency[char] = 1
    print(type(char_frequency))
    return sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)[0]


print(print_wassup())
