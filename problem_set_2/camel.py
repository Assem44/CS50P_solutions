camel_case = input("camelCase: ").strip()
snake_case = ''
for ltr in camel_case:
    if ltr.isupper():
        snake_case += f"_{ltr.lower()}"
    else:
        snake_case += ltr
print(snake_case)
