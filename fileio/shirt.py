import sys, os
from PIL import Image, ImageOps

def main():

    extensions = [".jpeg", ".jpg", ".png"]

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguents")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif os.path.splitext(sys.argv[1])[1].lower() not in extensions or os.path.splitext(sys.argv[2])[1].lower() not in extensions:
        sys.exit("Invalid input")


    person = extract(sys.argv[1])
    output = transform(person)
    output.save(sys.argv[2])



def extract(input_file):
    try:
        with Image.open(input_file) as img:
            img.load()        
            return img

    except FileNotFoundError:
        sys.exit("File not found")


def transform(photo):
    try:
        with Image.open("shirt.png") as shirt:
            shirt_size = shirt.size
            photo_fitted = ImageOps.fit(photo, shirt_size)
            photo_fitted.paste(shirt, (0, 0), mask=shirt)
            return photo_fitted
    except FileNotFoundError:
        sys.exit("shirt.png not found")
    
       

if __name__ == "__main__":
    main()