import random

def get_numbers_ticket(min_num, max_num, quantity):
    if not (1 <= min_num <= max_num <= 1000):
        return []
    if quantity > (max_num - min_num + 1) or quantity <= 0:
        return []

    numbers = random.sample(range(min_num, max_num + 1), quantity)
    return sorted(numbers)

if __name__ == "__main__":
    print(get_numbers_ticket(1, 49, 6))
