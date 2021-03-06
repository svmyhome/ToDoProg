import telebot
import random
token = '1448944959:AAFaQKKp7pXRlYmRZcuXVCgtjWXYRlY8Hs8'

bot = telebot.TeleBot(token)

todos = {}
HELP = '''
Список доступных команд:
* /print  - напечать все задачи на заданную дату
* /add ДАТА ЗАДАЧА - добавить задачу Формат ввода ДАТЫ: 01-01-2020, сегодня
* /help - Напечатать help
* /random - Добавить на сегодня случайную задачу
'''
COMMANDS_BOT = ['add', 'print','help', 'random']
RANDOM_TASKS = [
    'Изучить питон',
    'Выполнить ТО',
    'Пройти 2 курс по питону',
    'Изучить стратоплан'
]

def add_todo(date_task, new_task):
    if date_task in todos:
        todos[date_task].append(new_task)
        print(f'Задача {new_task} добавлена в дату {date_task}')
    elif date_task not in todos:
        todos[date_task] = [new_task]
        print(f'Задача {new_task} добавлена в дату {date_task}')

@bot.message_handler(commands=["help"])
def help_task(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["random"])
def random_task(message):
    task = random.choice(RANDOM_TASKS)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task} записанна сегодня')

@bot.message_handler(commands=["print"])
def print_task(message):
    split_task = message.text.split()
    if len(split_task) == 1:
        bot.send_message(message.chat.id, f'Вы ввели неправильный формат команды print.\n Формат /print Дата')
    else:
        if split_task[1] == 'all':
            for date in todos:
                text = ''
                if date in todos:
                    for task in todos[date]:
                        text = text + f'[] {task}\n'
                else:
                    text = 'Такой даты нет'
                bot.send_message(message.chat.id, f'На {date} у вас следующие задачи:\n {text}')
        else:
            for date in split_task[1:]:
                text = ''
                if date in todos:
                    for task in todos[date]:
                        text = text + f'[] {task}\n'
                else:
                    text = 'Такой даты нет'
                bot.send_message(message.chat.id, f'На {date} у вас следующие задачи:\n {text}')

@bot.message_handler(commands=["add"])
def add_task(message):
    split_task = message.text.split(maxsplit = 2)
    date = split_task[1].lower()
    task = split_task[2]
    if len(task) < 3:
        bot.send_message(message.chat.id, f'Вы ввели задачц {task} менее 4-х символов. ввведите задачу не менее 4-х символов')
    else:
        add_todo(date, task)
        bot.send_message(message.chat.id, f'Задача {task} записанна в {date}')

@bot.message_handler( content_types = ["text"])
def unknow_command(message):
    split_task = message.text.split()
    task = split_task[0].lower()
    if task not in COMMANDS_BOT:
        bot.send_message(message.chat.id, f'Неизвестная команда {task}. Наберите /help и посмотрите команды')

bot.polling(none_stop=True)
