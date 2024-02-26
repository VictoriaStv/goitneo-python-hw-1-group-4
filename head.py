from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    get_birthdays_per_week = defaultdict(list)

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date() 
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
           birthday_this_year = birthday_this_year.replace(year=today.year + 1)

    delta_days = (birthday_this_year - today).days    
    
    birthday_weekday = (today + timedelta(days = delta_days)).strftime("%A")
    if delta_days >= 0 and delta_days < 7:
        if birthday_weekday in ["Saturday", "Sunday"]:
            birthday_weekday = "Monday"

        get_birthdays_per_week[birthday_weekday].append(name)
    
    for day, names in get_birthdays_per_week.items():
        print(f"{day}: {', '.join(names)}")

users = [
    {"name": "Michael Scott", "birthday": datetime(1962,2,27)},
    {"name": "Dwight Schrute", "birthday": datetime(1966,2,28)},
    {"name": "Jim Halpert", "birthday": datetime(1979,2,28)},
    {"name": "Pam Beesly", "birthday": datetime(1974,1,1)},
    {"name": "Ryan Howard", "birthday": datetime(1979,1,2)},
    {"name": "Andy Bernard", "birthday": datetime(1974,1,3)},
    {"name": "Stanley Hudson", "birthday": datetime(1958,1,4)},
    {"name": "Kevin Malone", "birthday": datetime(1972,1,5)},
    {"name": "Angela Martin", "birthday": datetime(1971,1,5)},
    ]

get_birthdays_per_week(users)