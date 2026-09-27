n=1
my_dict = {}

while True:
    try:
        item = input().upper()
        if item in my_dict:
            my_dict[item] += 1
        else:
            my_dict[item] = 1


    except (EOFError, KeyboardInterrupt):
        my_dict = dict(sorted(my_dict.items()))
        for item in my_dict:
            print(f"{my_dict[item]} : {item}")
        break