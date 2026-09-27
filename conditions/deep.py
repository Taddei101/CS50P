
answer_raw = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))

answer = answer_raw.lower()

match answer:
    case "42":
        print("Yes")
    case "forty-two":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")


