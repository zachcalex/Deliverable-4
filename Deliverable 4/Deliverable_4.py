
import random

def method1(length):
    array = []
    for _ in range(length):
        array.append(random.randint(10, 51))
    return array

def method2(array):
    return sum(array)

try:
    user_input = int(input("Enter an integer number between 5 and 15: "))

    if 5 <= user_input <= 15:
        array = method1(user_input)
        print("\nThe elements of the array are:", " ".join(map(str, array)))

        sum_result = method2(array)
        print("The sum is:", sum_result)
    else:
        print("Invalid input. Please enter an integer between 5 and 15.")
except ValueError:
    print("Invalid input. Please enter an integer number.")
except OverflowError:
    print("Invalid input. The number is too large or too small.")

input()
