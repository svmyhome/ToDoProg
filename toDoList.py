import datetime


HELP = '''
    help  - вывести подсказки по командам
    add - добавить задачу
    print - распечатать списо задач
'''
TODAY = []
TOMORROW = []
OTHER = []

start = True
while start:
    now_date = datetime.datetime.today().strftime("%d%m%Y")
    tomorrow_date = (datetime.datetime.today() + datetime.timedelta(1)).strftime("%d%m%Y")
    new_command = input('Введите команду: ').lower()
    if new_command == 'help':
        print(HELP)
    elif new_command == 'add':
        date_task = input('Введите дату в формате ddmmyyyy: ')
        new_task = input('Введите название задачи: ').lower()
        if date_task == now_date:
                TODAY.append(new_task)
                print('Задача добавлена в список')
                print('Текущий список задач', TODAY)
        elif date_task == tomorrow_date:
                TOMORROW.append(new_task)
                print('Задача добавлена в список')
                print('Текущий список задач', TOMORROW)
        elif date_task != [tomorrow_date, now_date]:
            OTHER.append(new_task)
            print('Задача добавлена в список')
            print('Текущий список задач', OTHER)
    elif new_command == 'print':
        print('Текущий список задач: ')
        for task in TODAY:
            print('Список задачь текущего дня', task)
        for task in TOMORROW:
            print('Список задачь завтрашнего дня', task)
        for task in OTHER:
            print('Список задать прочие', task)
    elif new_command == 'exit' or new_command != ['add','help', 'print']:
        print('Команда не распознана введите одну из следующих команд:', HELP)
        print('Спасибо за использование! До свидания!')
        break

 #   start = bool(input('Вы хотите ввести еще задачу(True/False)? ').title())