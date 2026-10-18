
def main():
    while True:
        try:
            fraction = input("Fraction: ")
        
            gauge(convert(fraction))
        except (ValueError, ZeroDivisionError, IndexError,TypeError):
            True



def convert (fraction):
    try:
        fraction = fraction.split("/")
        percentage = (int(fraction[0]) / int(fraction[1]))*100
        return percentage

    except (ValueError, ZeroDivisionError, IndexError,TypeError):
            True

def gauge(percentage):
    try:
        if percentage >= 99:
            print("F")
            return f"F"
            
        
        elif percentage <=1:
            print("E")
            return f"E"
        
        else:
            print(f"{percentage:.0f}%")

    except (TypeError):
        print("type error")
    
        

if __name__ == "__main__":
    main()




# while True:

#     fraction = input("Fraction: ")
#     try:
#         fraction = fraction.split("/")
#         percentage = (int(fraction[0]) / int(fraction[1]))*100

#         if percentage >= 99:
#             print("F")

#         elif percentage <=1:
#             print("E")

#         else:
#             print(f"{percentage:.0f}%")

#         break

#     except (ValueError, ZeroDivisionError, IndexError):
#         True
    
    

