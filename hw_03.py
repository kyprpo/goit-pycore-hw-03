# Домашня робота: Тема 4. Робота з датою, часом та рядками

from datetime import datetime, timedelta
import random
import re


# Завдання 1
def get_days_from_today(date_str):
    """
    Повертає кількість днів між заданою датою і поточною.
    Якщо дата у майбутньому — результат буде від’ємним.
    """
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - target_date
        return delta.days
    except ValueError:
        print("X Неправильний формат дати. Використовуйте 'YYYY-MM-DD'.")
        return None


# Завдання 2
def get_numbers_ticket(min_num, max_num, quantity):
    """
    Генерує відсортований список унікальних випадкових чисел у межах [min_num, max_num].
    """
    if not (1 <= min_num <= max_num <= 1000):
        return []
    if quantity > (max_num - min_num + 1) or quantity <= 0:
        return []

    numbers = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(numbers)


# Завдання 3
def normalize_phone(phone_number):
    """
    Нормалізує телефонний номер до формату +380XXXXXXXXX.
    """
    cleaned = re.sub(r"[^\d+]", "", phone_number.strip())

    if cleaned.startswith("+"):
        if not cleaned.startswith("+38"):
            return cleaned
        return cleaned

    if cleaned.startswith("380"):
        return f"+{cleaned}"

    if cleaned.startswith("0"):
        return f"+38{cleaned}"

    return f"+38{cleaned}"


# Завдання 4
def get_upcoming_birthdays(users):
    """
    Повертає список колег, яких потрібно привітати протягом наступних 7 днів.
    Якщо день народження припадає на вихідний — переносимо привітання на понеділок.
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days
        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


# Тестові приклади (можеш залишити для перевірки)
if __name__ == "__main__":
    print("Завдання 1:", get_days_from_today("2023-10-10"))
    print("Завдання 2:", get_numbers_ticket(1, 49, 6))
    
    raw_numbers = [
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    sanitized = [normalize_phone(num) for num in raw_numbers]
    print("Завдання 3:", sanitized)

    users = [
        {"name": "John Doe", "birthday": "1985.10.15"},
        {"name": "Jane Smith", "birthday": "1990.10.18"},
    ]
    print("Завдання 4:", get_upcoming_birthdays(users))
