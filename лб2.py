# 1. Створення змінних різних типів
string_var = "Hello, Python!"
integer_var = 42
float_var = 3.14
bool_var = True
list_var = [1, 2, 3]
dict_var = {"name": "Roman", "age": 19}
tuple_var = (10, 20, 30)
none_var = None

print("Різні типи змінних:")
print(string_var, integer_var, float_var, bool_var, list_var, dict_var, tuple_var, none_var)
print()

# 2. Порівняння різних типів
print("Порівняння чисел:", 5 > 3)
print("Порівняння рядків:", "apple" == "apple")
print("Порівняння булевих значень:", True != False)
print("Порівняння списків:", [1, 2] == [1, 2])
print("Порівняння словників:", {"a": 1} == {"a": 1})
print("Порівняння кортежів:", (1, 2) < (2, 1))
print()

# --- РОБОТА З РЯДКАМИ ---
# 1
num_str = 125
num_str = str(num_str)
print("num_str:", num_str)

# 2
message = "Hi, my name is Python!"
message_replaced = message.replace("y", "0").replace("i", "1")
print("message після replace:", message_replaced)

# 3
split_test = "This is a split test"
split_result = split_test.split()
string_join = " ".join(split_result)
print("split_result:", split_result)
print("string_join:", string_join)

# 4
print("Довжина string_join:", len(string_join))
print()

# --- РОБОТА ЗІ СПИСКАМИ ---
# 1
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print("list_append:", list_append)

# 2
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print("list_extend:", list_extend)

# 3
print("Індекс елемента 6:", list_extend.index(6))

# 4
print("Довжина list_append:", len(list_append))
print()

# --- РОБОТА ЗІ СЛОВНИКАМИ ---
dict_test = {"car": "Toyota", "price": 4900, "where": "EU"}
print("car:", dict_test["car"])
print("where:", dict_test["where"])

print("Ключі:", dict_test.keys())
print("Значення:", dict_test.values())
print("Пари ключ-значення:", dict_test.items())
