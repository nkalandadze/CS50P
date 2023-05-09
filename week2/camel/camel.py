# დავალება #13 - camelCase
camelCase = input("camelCase: ").strip()
snakeCase = ""

for i in range(len(camelCase)):
    if camelCase[i].isupper():
        snakeCase = snakeCase + "_" + camelCase[i].lower()
    else:
        snakeCase = snakeCase + camelCase[i]

print(f"snakeCase: {snakeCase}")