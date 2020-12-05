import datetime
# user_date = input('Введите дату: ')
# user_task = input('Введите задачу: ')
#
# print(user_date, user_task)

# i = 0
# mass = {}
# while i < 3:
#     user_date = input('Введите дату: ')
#     user_task = input('Введите задачу: ')
#     i += 1
#     mass[user_date] = user_task
# for key, data in mass.items():
#     print(key, data)
d = datetime.date(2012, 12, 14)
print( datetime.date.today().strftime("%m/%d/%Y"))
a = datetime.datetime.today().strftime("%m%d%Y")
print(a) # '20170405'
print((datetime.datetime.now() + datetime.timedelta(1)).strftime("%m%d%Y"))