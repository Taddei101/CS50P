

def insert():
    amount = int(0)
    while True:
        amount += int(input("Insert Coin: "))

        if amount <50:
            print(f"Amount Due: {50-amount}")

        else:
            print(f"Charge Owed: {amount-50}")

            break


insert()
