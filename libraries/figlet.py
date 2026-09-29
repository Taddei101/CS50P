from pyfiglet import Figlet, FontNotFound
import sys
import random

figlet = Figlet()
font_list = figlet.getFonts()

def figo():
    try:
        
        if len(sys.argv) == 2 or len(sys.argv) > 3:
            sys.exit("Invalid usage")

        elif len(sys.argv) < 2:
            
            text = input("Input: ")
            figlet.setFont(font=random.choice(font_list))

        else:
            
            if sys.argv[1] != "-f":
                sys.exit("Invalid usage")
                
            text = input("Input: ")
            figlet.setFont(font=sys.argv[2])

        print(figlet.renderText(text))

    except FontNotFound:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    figo()
