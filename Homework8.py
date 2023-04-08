"""
Реалізувати функцію для виведення списку колег, яких потрібно привітати з днем народження на тижні.
У вас є список словників users, кожен словник у ньому обов'язково має ключі name (це рядок з
ім'ям користувача) та birthday (datetime об'єкт - день народження).
Завдання: написати функцію get_birthdays_per_week, яка отримує на вхід список users і виводить
у консоль (за допомогою print) список користувачів, яких потрібно привітати по днях.

Умови приймання:
- get_birthdays_per_week виводить іменинників у форматі:
    Monday: Bill, Jill
    Friday: Kim, Jan
- Користувачів, у яких день народження був на вихідних, потрібно привітати у понеділок.
- Для відладки зручно створити тестовий список users та заповнити його самостійно.
- Функція виводить користувачів з днями народження на тиждень вперед від поточного дня.
- Тиждень починається з понеділка.
"""

from datetime import datetime, timedelta

users = [{"name": "Alex", "birthday": datetime(1980, 4, 8)},
         {"name": "Egle", "birthday": datetime(1982, 4, 8)},
         {"name": "Hiba", "birthday": datetime(1986, 4, 9)},
         {"name": "Abdel", "birthday": datetime(1995, 4, 10)},
         {"name": "Akshay", "birthday": datetime(1990, 5, 11)},
         {"name": "Zayn", "birthday": datetime(1982, 4, 12)},
         {"name": "Casey", "birthday": datetime(1999, 4, 12)},
         {"name": "Johan", "birthday": datetime(1995, 4, 12)},
         {"name": "Adrien", "birthday": datetime(1993, 4, 13)},
         {"name": "Rilvan", "birthday": datetime(1995, 4, 14)},
         {"name": "Zineb", "birthday": datetime(1995, 4, 16)},
         {"name": "Ahmed", "birthday": datetime(1995, 4, 19)},
         {"name": "Mohamed", "birthday": datetime(1995, 4, 22)},
         {"name": "Jakub", "birthday": datetime(1995, 5, 3)},
         {"name": "Dan", "birthday": datetime(1995, 5, 5)},
         ]

DAYS = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday",
        4: "Friday", 5: "Saturday", 6: "Sunday"}

def get_birthdays_per_week(users):
    print("Let's select the date from which we will start to calculate.")
    year = int(input("Type number for year (YYYY): "))
    month = int(input("Type number for month (MM): "))
    day = int(input("Type number for day of month (DD): "))
    base = datetime(year, month, day)
    #base = datetime.today()
    print(f"The selected day is {DAYS[base.weekday()]}. ", end="")
    if base.weekday() == 0:  # Monday: take past weekend till future Friday included
        start = base - timedelta(days=2)
        period = [start + timedelta(days=_) for _ in range(7)]
    elif base.weekday() in range(1, 5):  # any weekday: take from today till future Friday included
        period = [base + timedelta(days=_) for _ in range(5-base.weekday())]
    else:  # weekend: take from today till future Friday included
        period = [base + timedelta(days=_) for _ in range(5+7-base.weekday())]
    print(f"The following {len(period)} dates will be checked:")
    print(*[i.date() for i in period], sep=", ")
    print("-" * 82)

    to_greet = {DAYS[i.weekday()]: [] for i in period}  # create dictionary: keys: days, values: lists for names
    people_with_birthdays = 0
    for user in users:
        for item in period:
            if (user['birthday'].month == item.month) and (user['birthday'].day == item.day):
                day_was = DAYS[user["birthday"].weekday()]
                day_index_will_be = item.weekday()
                day_name_will_be = DAYS[item.weekday()]
                #print(f'{user["name"]} was born on {user["birthday"].date()} ({day_was}), ', end="")
                #print(f'their coming birthday will be on {day_name_will_be} {item.date()}')
                if day_index_will_be not in (5, 6):  # if not weekend, the name is greeted on the "correct" day
                    to_greet[day_name_will_be].append(user["name"])
                else:  # if weekend, move the name to be greeted on Monday
                    to_greet["Monday"].append(user["name"])
                people_with_birthdays += 1
    print(f"In the target period there will be {people_with_birthdays} birthdays.")
    print("-" * 82)

    for key, value in to_greet.items():
        if len(value) > 0:
            print(key + ": ", end="")
            print(*value, sep=', ')
    
    return None


if __name__ == "__main__":
    get_birthdays_per_week(users)
