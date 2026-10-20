#Extract, Transform, Load [ETL]


import csv, sys

def main():
    transform()
    
    


def extract():

    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit()
    elif len(sys.argv) >3:
        print("too many command-line arguments")
        sys.exit()

    else:
        
        try:
            with open(sys.argv[1]) as file:
                table = csv.DictReader(file) 

                first_name = []
                last_name = []
                home = []

                for row in table:
                    names = row['name'].split(sep=', ')
                    houses = row['house']
                    
                    first_name.append(names[1])
                    last_name.append(names[0])
                    home.append(houses)

                #print(first_name, last_name,home)
                return first_name, last_name, home
                    
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")

def transform():
    first_name, last_name, home = extract()

    with open(sys.argv[2], "w", newline='') as file:
        fieldnames = ['first_name', 'last_name', 'house']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        
        for f, l, h in zip(first_name, last_name, home):
            writer.writerow({
                "first_name":f,
                "last_name":l,
                "house":h,
            })



if __name__ == "__main__":
    main()


