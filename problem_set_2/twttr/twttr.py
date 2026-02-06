user_text = input("Input: ")
output = ''
for ltr in user_text:
    if ltr.lower() in ["a", "e", "i", "o", "u"]:
        continue
    else:
        output += ltr
print(f"Output: {output}")
