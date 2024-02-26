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
    {"name": "Michael Scott", "birthday": datetime(1962,2,28)},
    {"name": "Dwight Schrute", "birthday": datetime(1968,2,29)},
    {"name": "Jim Halpert", "birthday": datetime(1980,2,29)},
    {"name": "Pam Beesly", "birthday": datetime(1974,3,1)},
    {"name": "Ryan Howard", "birthday": datetime(1979,3,2)},
    {"name": "Andy Bernard", "birthday": datetime(1974,3,3)},
    {"name": "Stanley Hudson", "birthday": datetime(1958,3,4)},
    {"name": "Kevin Malone", "birthday": datetime(1972,3,5)},
    {"name": "Angela Martin", "birthday": datetime(1971,3,5)},
    ]

get_birthdays_per_week(users)
