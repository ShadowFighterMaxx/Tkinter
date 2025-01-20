def multiply_one_iteration(a, b):
    return a * b

def multiply_n_iterations(a, b):
    if b < 0:
        a, b = -a, -b
    result = 0
    for _ in range(b):
        result += a
    return result

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

product1 = multiply_one_iteration(num1, num2)
product2 = multiply_n_iterations(num1, num2)

print(f"Product using one iteration: {product1}")
print(f"Product using N iterations: {product2}")