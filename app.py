def add(a, b):
    return a + b

def sub(a, b):
    return a - b

if __name__ == "__main__":
    print("Simple Calculator")
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    
    print("Addition:", add(x, y))
    print("Subtraction:", sub(x, y))
