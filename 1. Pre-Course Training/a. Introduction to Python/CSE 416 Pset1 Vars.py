"""
Task 1:
Fix the errors in the if-else statement below
"""
def boolean(x:bool, y:bool) -> str:
    # TODO
    if (x and y):
        result = "cats"
    elif (x or y):
        result = "dogs"
    else:
        result = "fish"
    return result

"""
Task 2:
Let f(x) = 2x^2 + 1. 
The function f below takes an integer x and returns the above result.
Assign 2x^2 + 1 to variable result using arithmetic operations.
"""
def f(x:int) -> int:
    result = 2*(x**2)+1
    return result

if __name__ == "__main__":
    print("Task 1:")
    print(boolean(x=True, y=False))

    print("Task 2:")
    print(f(5))
