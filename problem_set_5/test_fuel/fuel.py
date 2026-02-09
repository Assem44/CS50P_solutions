def main():
    while True:
        fraction = input("Fraction: ").strip()
        try:
            percentage = convert(fraction)
            state = gauge(percentage)
            print(state)
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
    if "/" not in fraction:
        raise ValueError

    x, y = fraction.split("/")
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError
    elif x>y or x<0 or y<0:
        raise ValueError

    return round((x / y) * 100)
def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
