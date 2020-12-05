word_list = ['python', 'c++', 'c', 'scala', 'java']
l_task = input('Введите букву: ')


def count_letter(letter, word_list):
    result = 0
    for word in word_list:
        if l_task in word:
            print(word)
            result += 1
    return result
print(count_letter(l_task, word_list))
