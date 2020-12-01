todos = {'20202020': ''}
start = True
while start:
    date_task = input('Введите дату в формате ddmmyyyy: ')
    new_task = input('Введите название задачи: ')
    todos[date_task].append(new_task)
    print(todos[date_task])