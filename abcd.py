def calculate(expression):
    return eval(expression)  # SAST issue: unsafe use of eval()

if __name__ == "__main__":
    user_input = input("Enter an expression: ")
    result = calculate(user_input)
    print(result)
