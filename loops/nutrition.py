import csv

dicionario = {}

with open('food.csv', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        dicionario[linha['Category'].lower()] = {k : v for k, v in linha.items() if k != 'Category'}


# def busca():
#     food = input("Food: ").lower()
#     if food in dicionario:
#         print(dicionario[food]['Data.Fat.Saturated Fat'])
#     else:
#         print(f"{food} not in database.\n") 


def busca2(dicionario):
    food = input("Food: ").lower()
    try:
        print(f"""
            ============ REPORT ===========
            Food: {dicionario[food].get("Description","Unknown")}
            Saturated Fat: {dicionario[food].get("Data.Fat.Saturated Fat", "Unknown")}
            ===============================
        """)
    except KeyError:
        print(f"Error: '{food}' is not listed in database")

busca2(dicionario)
