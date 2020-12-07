CATEGORY_TASKS = []
s = '/add 10-12-2020 Taask1 example @Work'
print(s.split())
split_command = s.split(maxsplit=2)
split_task = split_command[2].split('@')
CATEGORY_TASKS.append(split_task[1])
print(CATEGORY_TASKS)
