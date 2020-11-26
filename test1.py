# user_date = input('Введите дату: ')
# user_task = input('Введите задачу: ')
#
# print(user_date, user_task)

i = 0
mass = {}
while i < 3:
    user_date = input('Введите дату: ')
    user_task = input('Введите задачу: ')
    i += 1
    mass[user_date] = user_task
for key, data in mass.items():
    print(key, data)
