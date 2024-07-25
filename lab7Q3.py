input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase_count = 0
lowercase_count = 0
special_char_count = 0
numeric_count = 0

for char in input_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        numeric_count += 1
    elif not char.isspace():
        special_char_count += 1

print("Uppercase characters:", uppercase_count)
print("Lowercase characters:", lowercase_count)
print("Special characters:", special_char_count)
print("Numeric characters:", numeric_count)
