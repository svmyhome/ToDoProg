import datetime


HELP = '''
Список доступных команд:
* print  - напечать все задачи на заданную дату
* todo - добавить задачу
* help - Напечатать help
* random - Добавить на сегодня случайную задачу
'''
RANDOM = 'Изучить питон'
todos = {}
start = True
def add_todo(date_task, new_task):
    if date_task in todos:
        todos[date_task].append(new_task)
        todos[date_task].append('test')
        print(f'Задача {new_task} добавлена в дату {date_task}')
    elif date_task not in todos:
        todos[date_task] = [new_task]
        todos[date_task].append('test')
        print(f'Задача {new_task} добавлена в дату {date_task}')
while start:
    new_command = input('Введите команду: ').lower()
    if new_command == 'help':
        print(HELP)
    elif new_command == 'add':
        date_task = input('Введите дату в формате ddmmyyyy: ').lower()
        new_task = input('Введите название задачи: ')
        add_todo(date_task,new_task)
    elif new_command == 'random':
        add_todo('today', RANDOM)
    elif new_command == 'print':
        print('Текущий список задач: ')
        screen_task = input('Введите дату за которрую необходимо вывести сообщения ')
        if screen_task in todos:
            print(todos[screen_task])
        else:
            print('Такой даты не существует')
    elif new_command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else: #new_command == 'exit' or new_command != ['add', 'help', 'print']:
        print('Команда не распознана введите одну из следующих команд:', HELP)

 #   start = bool(input('Вы хотите ввести еще задачу(True/False)? ').title())