def main():
    print(shorten(input("Word: ")))


def shorten(word):
    return ''.join([l for l in word if l.lower() not in 'aeiou'])

if __name__ =="__main__":
    main()
