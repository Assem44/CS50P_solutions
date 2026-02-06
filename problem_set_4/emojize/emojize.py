import emoji
user_input = input("Input: ").strip()
output = emoji.emojize(user_input, language='alias')
print(f"Output: {output}")
