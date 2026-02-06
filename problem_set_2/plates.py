def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    elif not (s[:2].isalpha()):
        return False

    found_number = False
    for ltr in s:
        if not (ltr.isalnum()):
            return False
        elif ltr.isdigit():

            if ltr == "0" and  not found_number:
                return False

            found_number = True
        elif found_number and ltr.isalpha():
            return False

    return True

main()
