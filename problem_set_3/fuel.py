def main():
    fuel_state = handle_user_input("Fraction: ")
    print(fuel_state)
def handle_user_input(prompt):
    while True:
        try:
            fraction = input(prompt).strip()
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
            if 0 <= x <= y:
                return get_fuel_percent(x, y)
        except (ValueError, ZeroDivisionError):
            pass
def get_fuel_percent(x, y):
    percent = round((x/y) * 100)
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"

if __name__ == "__main__":
    main()
