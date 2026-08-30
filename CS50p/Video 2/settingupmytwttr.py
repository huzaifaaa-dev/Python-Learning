texts = input("What would you like to tweet/text: ")
for text in texts:
    match text:
        case "A" | "a":
            texts = texts.replace("A", "").replace("a", "")
        case "E" | "e":
            texts = texts.replace("E", "").replace("e", "")
        case "I" | "i":
            texts = texts.replace("I", "").replace("i", "")
        case "O" | "o":
            texts = texts.replace("O", "").replace("o", "")
        case "U" | "u":
            texts = texts.replace("U", "").replace("u", "")

print(texts)