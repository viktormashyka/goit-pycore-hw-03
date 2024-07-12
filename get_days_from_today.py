from datetime import datetime

def get_days_from_today(date):
    today = datetime.today()
    date = datetime.strptime(date, "%Y-%m-%d")
    return (today - date).days

if __name__ == "__main__":
    print(get_days_from_today("2024-07-13"))