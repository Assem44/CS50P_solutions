grocery_list = {}
while True:
    try:
        item = input().strip().upper()
        if not item:
            continue
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        print()
        for key in sorted(grocery_list.keys()):
            print(f"{grocery_list[key]} {key}")
        break
