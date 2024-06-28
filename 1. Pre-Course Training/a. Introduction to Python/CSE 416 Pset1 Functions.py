"""
This starter code is written by Pemi Nguyen. Permission is
hereby granted to students registered for University of Washington
CSE 312 for use solely during Fall Quarter 2020 for purposes of
the course.  No other use, copying, distribution, or modification
is permitted without prior written consent.
"""

"""
Task 1:
Write the method find_max, which takes two integer parameters and returns the larger one.
If they are equal, return which ever.
"""
def find_max(num1: int, num2: int):
    if num1 >= num2:
        return num1
    else:
        return num2

"""
Task 2:
One of the differences between Python and other programming languages is that it can return
multiple values in a function (even with different types).
In this task, you will write a function called sum_and_prod(), which takes two integer parameters
and return the sum and product of the two.
(Remember, the return values are ordered, so you need to return the sum first and the product second).
"""
def sum_and_prod(num1, num2):
    return (num1 + num2), (num1*num2)

if __name__ == "__main__":
    print("Task 1:")
    print(find_max(3, 6))

    print("Task 2:")
    s, p = sum_and_prod(4, 7)
    print("Sum = {}".format(s))
    print("Product = {}".format(p))
