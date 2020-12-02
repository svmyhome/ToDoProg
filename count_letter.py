word_list = ['python', 'c++', 'c', 'scala', 'java']
l_task = input('Введите букву: ')


def count_letter(letter, word_list):
    for word in word_list:
        if l_task in word:
            print(word)

count_letter(l_task, word_list)
