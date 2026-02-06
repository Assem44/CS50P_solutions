def main():
    user_text = input("Enter the text: ")
    converted_text = convert(user_text)
    print(converted_text)
def convert(txt):
    return txt.replace(":)", "🙂").replace(":(", "🙁")
if __name__ == "__main__":
    main()
