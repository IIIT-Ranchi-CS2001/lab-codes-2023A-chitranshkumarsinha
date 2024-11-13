s=str(input("enter the string:"))

char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
result = char_count                   
for char, count in result.items():
    print((f"'{char}': {count}"))