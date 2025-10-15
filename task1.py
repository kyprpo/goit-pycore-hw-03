from datetime import datetime

def get_days_from_today(date_str):
    """
    Рахує кількість днів між заданою датою і сьогоднішньою.
    Якщо дата в майбутньому — повертає від’ємне число.
    """
    try:
        target_date = datetime.strptime(date_str, "%Y-%m-%d").date()  # переводимо рядок у дату
        today = datetime.today().date()  # сьогоднішня дата
        delta = today - target_date      # різниця між датами
        return delta.days
    except ValueError:
        print("Неправильний формат дати! Використовуйте YYYY-MM-DD.")
        return None


# це просто приклад, щоб перевірити роботу функції
if __name__ == "__main__":
    print(get_days_from_today("2023-10-10"))
