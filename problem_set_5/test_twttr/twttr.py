def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    output = ''
    for ltr in word:
        if ltr.lower() in ["a", "e", "i", "o", "u"]:
            continue
        else:
            output += ltr

    return output

if __name__ == "__main__":
    main()
