assert abs(-42) == 42

# assert abs(-42) == -42  # AssertionError

# Добавляем текст ошибки:
assert abs(-42) == -42, "Should be absolute value of a number"
# AssertionError: Should be absolute value of a number
