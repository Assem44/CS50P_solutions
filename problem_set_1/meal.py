def main():
    user_time = input("What time is it? ").strip()

    result = convert(user_time)
    if (7.0 <= result <= 8.0):
        print("breakfast time")
    elif (12.0 <= result <= 13):
        print("lunch time")
    elif (18.0 <= result <= 19.0):
        print("dinner time")

def convert(time):
    if " " in time:
        parts = time.split(" ")
        user_hours, user_minutes = parts[0].split(":")
        state = parts[1].lower().replace(".", "")
        h = int(user_hours)
        if (state == "pm" and h != 12):
            h += 12
        elif (state == "am" and h == 12):
            h = 0
    else:
        user_hours, user_minutes = time.split(":")
        h = int(user_hours)

    m = int(user_minutes)

    return h + (m / 60)

if __name__ == "__main__":
    main()
