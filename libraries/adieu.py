
import inflect

name_list = []

def farewell(name_list):
    p = inflect.engine()
    p = p.join(name_list)
    print(f"Adieu, adieu, to {p}")
    

while True:
    try:
        name_list.append(input("Name: "))
    
    except KeyboardInterrupt:
        farewell(name_list)
        break




