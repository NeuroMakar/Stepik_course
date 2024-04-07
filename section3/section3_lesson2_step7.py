# Форматирование строк с помощью конкатенации:
actual_result = "abrakadabra"
print("Wrong text, got " + actual_result + ", something wrong")
# Wrong text, got abrakadabra, something wrong

# Форматирование строк с помощью str.format:
print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))
# Let's count together: one, then goes two, and then three


# Форматирование строк с помощью f-strings:
# Пример №1:
str1 = "one"
str2 = "two"
str3 = "three"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")
# Let's count together: one, then goes two, and then three

# Пример №2:
actual_result = "abrakadabra"
print(f"Wrong text, got {actual_result}, something wrong")
# Wrong text, got abrakadabra, something wrong

# Пример №3:
print(f"{2+3}")  # 5
