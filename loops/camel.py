
def change(camel):
    snake = ""
    for l in camel:
        if l.isupper():
            snake += "_" +l.lower()
        else:
            snake += l 
    return snake 

camel = input ("camelCase: ")

snake = change(camel)
print("snake_case: ", snake)
i=3
print(snake[i+3])
