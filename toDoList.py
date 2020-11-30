HELP = '''
    help  - вывести подсказки по командам
    add - добавить задачу
    print - распечатать списо задач
'''
TASKS = []
start = True
while start:
    new_command = input('Введите команду: ').lower()
    if new_command == 'help':
        print(HELP)
    elif new_command == 'add':
        new_task = input('Введите название задачи: ').lower()
        TASKS.append(new_task)
        print('Задача добавлена в список')
        print('Текущий список задач', TASKS)
    elif new_command == 'print':
        print('Текущий список задач: ')
        for task in TASKS:
            print(task)
    elif new_command == 'exit' or new_command != ['add','help', 'print']:
        print('Команда не распознана введите одну из следующих команд:', HELP)
        print('Спасибо за использование! До свидания!')
        break

 #   start = bool(input('Вы хотите ввести еще задачу(True/False)? ').title())