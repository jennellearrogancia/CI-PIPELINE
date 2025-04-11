def is_adult(age):
    if not isinstance(age, int):
        raise ValueError("Age must be an integer.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age >= 18
