import csv
import sys

def main():
    if len(sys.argv) < 3 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) >3 :
        sys.exit("Too many command-line arguments")

    raw_data = extract(sys.argv[1])
    #print (raw_data)
    transformed_data = transform(raw_data)
    print(transformed_data)
    load(sys.argv[2], transformed_data)


def extract(input_file):
    try:
        with open(input_file, "r") as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

def transform(raw_data):
    transformed = []
    for row in raw_data:
        last, first = row["name"].split(", ")

        transformed.append({
            "first_name":first,
            "last_name":last,
            "house": row["house"],
        })
    return transformed

def load(output_file, data):
    with open(output_file, "w", newline="") as file:
        fieldnames = ["first_name", "last_name", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)


if __name__=="__main__":
    main()