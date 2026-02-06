user_expression = input("Expression: ").strip()
x, y, z = user_expression.split(" ")
def user_math(x, y, z):
    x = int(x)
    z = int(z)
    result = None
    match y :
        case "/":
            if (z == 0):
                return "Cant devide by zero."
            else:
                result = x / z
        case "+":
            result = x + z
        case "-":
            result = x - z
        case "*":
            result = x * z
    return round(float(result), 1)
print(user_math(x,y,z))
