

def medias (file_name):
    extensions = {'gif':'image','jpg':'image','jpeg':'image','png':'image','pdf':'application','txt':'text','zip':'application'}
    sufix = file_name.split('.')[-1].lower()

    if sufix in extensions:
        tipo = extensions[sufix]
        print(f"{tipo}/{sufix}")
        
    else:
        print("application/octet-stream")

file_name = input("File name: ")

medias(file_name)