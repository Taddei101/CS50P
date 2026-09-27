lista = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:

    date = input("Date: ")

    if "/" in date:
        try:
            date = date.split('/')
            month=date[0]
            day=date[1]
            year=date[2]
            print(f"{year}-{month:02}-{day:02}")
            break

        except (TypeError, IndexError,ValueError):
            pass

    else:
        try:
            date = date.split(' ')
            year = int(date[2])
            day = int(date[1].replace(",",""))
            month = int(lista.index(date[0])+1)
            print(f"{year}-{month:02}-{day:02}")
            break
        
        except (TypeError, IndexError,ValueError):
            pass

