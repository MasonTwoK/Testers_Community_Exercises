# Задача 1
d = {'name': 'John Doe', 'age': 30,
     'city': 'New York',
     'email': 'johndoe@example.com'}
# Попросіть користувача ввести ключ, який він бажає видалити, і видаліть цей елемент зі словника.
# Та виведіть на екран змінений словник.
app_switch = True
while app_switch:
    key = input("Enter the key of pair you want to delete: ")

    if key in d.keys():
        d.pop(key)
        print(d)
        app_switch = False
    else:
        print("Wrong key was entered! Try again..")


# Задача 2
d = {'name': 'Alice Smith',
     'age': 25, 'city': 'Los Angeles',
     'email': 'alice.smith@example.com',
     'favorite_subjects': ['Mathematics', 'History', 'Literature']}
# Виведіть з цього словника значення 'favorite_subjects' використовуючи цикл.
for values in d['favorite_subjects']:
    print(values)


# Задача 3
favorites = {
    'movies': ['Interstellar', 'Fast & Furious', 'Pirates of the Caribbean'],
    'music': ['Queen', 'The Beatles', 'Coldplay'],
    'sports': ['football', 'basketball', 'tennis']}
# Видаліть з цього списку sports та додайте новий ключ 'serials' де значенням будуть ваші улюблені серіали.
favorites.pop('sports')
favorites.update({'serials': ['Invincible', 'Netrunner', 'Berserk', 'Blue Eyed Samurai']})
