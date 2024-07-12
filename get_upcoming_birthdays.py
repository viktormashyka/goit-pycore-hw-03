from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    today = datetime.now().date()

    for user in users:
        normalized_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
       
        day_of_birth = normalized_date.day
        month_of_birth = normalized_date.month
        birthday_this_year = datetime(today.year, month_of_birth, day_of_birth).date()
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        days_until_birthday = (birthday_this_year - today).days
        if 0 <= days_until_birthday < 7:
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday_this_year})
        
    return upcoming_birthdays


if __name__ == "__main__":
    users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Joanna Dawson", "birthday": "1982.07.17"}
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)

# Передбачений результат:
# Якщо сьогодні 2024.07.12 результатом може бути:
# [
# {"name": "Joanna Dawson", "birthday": "1982.07.17"}
# ]