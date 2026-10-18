import sys

def open_file(file_path):
    try:
        with open(file_path, "r") as file:
            count=0
            for line in file:
                if line.startswith('#'):
                    pass
                elif line == '\n':
                    pass
                else:
                    count +=1
            return(print(count))
                        
    except FileNotFoundError:
        print ("File does not exist")

def verify():
    
    file_path = sys.argv[1]
    if file_path.endswith('py'):
        return file_path
    else:
        print("Not a Python file")
        sys.exit()
       
    
     
def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
    elif len(sys.argv) >2:
        print("Too many command-line arguments")
    else:
        open_file(verify())

    
if __name__ == "__main__":
    main()


