from pyfiglet import Figlet
import random
import sys
def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        user_font = random.choice(fonts)
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        user_font = sys.argv[2]
        if user_font not in fonts:
            sys.exit("Font not defined.")

    else:
        sys.exit("Invalid Input.")
    user_input = input("Input: ").strip()
    figlet.setFont(font = user_font)
    output = figlet.renderText(user_input)
    print(f"Output:\n{output}")


if __name__ == "__main__":
    main()




