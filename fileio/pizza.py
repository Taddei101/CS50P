from tabulate import tabulate
import csv
import sys


def main():
    table = validate()
    print(tabulate(table,headers="firstrow",tablefmt="pretty"))

def validate():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit
    elif len(sys.argv) >2:
        print("too many command-line arguments")
    else:
        try:
            with open(sys.argv[1]) as file:
                table = list(csv.reader(file))
                return table
        
        except FileNotFoundError:
            sys.exit("File does not exist")

if __name__ =="__main__":
    main()