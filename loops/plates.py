import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    
    pattern = r"^[A-Z]{2,6}$|^[A-Z]{2,4}[1-9][0-9]{0,3}$"
        
    if re.match(pattern, s, re.IGNORECASE):
        return True
    return False


main()


# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")

# def is_valid(s):
#     if not (2 <= len(s) <= 6 and s.isalnum()):
#         return False
        
#     if not s[0:2].isalpha():
#         return False
        
#     i = 0
#     while i < len(s):
#         if s[i].isdigit():
#             if s[i] == '0':
#                 return False
#             for j in range(i, len(s)):
#                 if not s[j].isdigit():
#                     return False
#             break
#         i += 1
        
#     return True

# main()