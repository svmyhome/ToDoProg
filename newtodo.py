todos = {} # todos: list -> dict

RANDOM_TASK = 'Выучить Python'

HELP = '''
Список доступных команд:
* print  - напечать все задачи на заданную дату
* todo - добавить задачу
* help - Напечатать help
* random - Добавить на сегодня случайную задачу
'''

# dict().keys() -> Список ключей
# dict().values() -> Список значений
# value in dict().values()


# 1. Привязка к датам
# Дата
# (в любом формате, 30-11-2020, Сегодня, завтра, когда-нибудь)
# Для каждой даты N задач (N >= 0)

# {"Дата"(string) : [Задачи](list)}

def add_todo(date, task):
  # Проверяем, есть ли такая дата в нашем словаре
  if date in todos:
  # Если дата есть - добавляем в список, который ей соответствует задачу
    # todos[d] -> ['task1', ...]
    # .append('input_task')
    todos[date].append(task)
  else:
    # Если нет - создаем в словаре пару ключ: значение -> Дата: [Задачу]
    todos[date] = [task]
    # todos[d] -> [1 одна задача]
  print(f'Задача {task} добавлена на дату {date}')


while True:
    command = input('Введите команду\n')
    command = command.lower()
    if command == 'help':
      print(HELP)
    elif command == 'todo': # (1)
      d = input('Введите дату: ')
      task = input('Введите задачу: ')
      d = d.lower()
      add_todo(d, task)
    elif command == 'print':
      d = input('Введите дату, для которой напечатать задачи: ')
      d = d.lower()
      if d in todos:
        task_list = todos[d]
        for task in task_list:
          print(f'[] {task}')
      else:
        print('Такой даты нет')
    elif command == 'random': # (2)
      add_todo('сегодня', RANDOM_TASK)
    elif command == 'exit':
      print('Спасибо за использование! До свидания!')
      break
    else:
      print('Неизвестная команда! Попробуйте еще раз')
