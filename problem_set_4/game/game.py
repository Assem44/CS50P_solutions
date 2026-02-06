import random
def main():
    while True:
        try:
            level = int(input("Level: ").strip())
            if level > 0:
                break
        except ValueError:
            pass

    random_integer = random.randint(1, level)

    while True:
        try:
            user_guess = int(input("Guess: ").strip())
            if user_guess <= 0:
                continue
            if (user_guess < random_integer):
                print("Too small!")
            elif (user_guess > random_integer):
                print("Too large!")
            else:
                print("Just right!")
                break
        except (ValueError):
            continue
if __name__ == "__main__":
    main()


