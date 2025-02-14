def add_integers(num1, num2):
    return num1 + num2
def subtract_integers(num1, num2):
    return num1 - num2
def multiply_integers(num1, num2):
    return num1 * num2
result =add_integers(5,3)
print(result)
result =add_integers(4,6)
print(result)
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        return True
    number=29
    if is_prime(number):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

def greet (name):
    return f"Hello {name}!"
person_name = "John"
greet(person_name)
print(greet(person_name))

