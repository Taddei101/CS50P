import emooji

texto = input("Input: ")

EMO = emoji.emojize(texto, language="alias")

print("Output: ", EMO)
