import re

def normalize_phone(phone_number):
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

if __name__ == "__main__":
    raw_numbers = [
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    print([normalize_phone(num) for num in raw_numbers])
