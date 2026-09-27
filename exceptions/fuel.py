
while True:

    fraction = input("Fraction: ")
    try:
        fraction = fraction.split("/")
        percentage = (int(fraction[0]) / int(fraction[1]))*100

        if percentage >= 99:
            print("F")

        elif percentage <=1:
            print("E")

        else:
            print(f"{percentage:.0f}%")

        break

    except (ValueError, ZeroDivisionError, IndexError):
        True
    
    

