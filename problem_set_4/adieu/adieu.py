import inflect
def main():
    s = inflect.engine()
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except EOFError:
            print()
            break
    output = s.join(names)
    print(f"Adieu, adieu, to {output}")
if __name__ == "__main__":
    main()
