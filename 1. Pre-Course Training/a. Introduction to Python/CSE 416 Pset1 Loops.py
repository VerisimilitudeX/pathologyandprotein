"""
This starter code is written by Pemi Nguyen. Permission is
hereby granted to students registered for University of Washington
CSE 312 for use solely during Fall Quarter 2020 for purposes of
the course.  No other use, copying, distribution, or modification
is permitted without prior written consent.
"""

"""
Task 1:
Use a for-loop to calculate 0 + 1 + 2 + ... + n (n >= 0)
and store the final result in variable result. No conditionals required
Hint: Initialize 'result' with 0 and use range() for the loop.
"""

def for_loop(n:int) -> int:
    result = 0
    for i in range(0, n + 1, 1):
        result += i
    return result

"""
Task 2:
Convert the following Java while loop into its Python
equivalent.

public void while_loop(int n) {
    int i = 2;
    while (i < n) {
        i++;
    }
    return i;
"""
def while_loop(n:int) -> int:
    i = 2
    while (i < n):
        i += 1
    return i

if __name__ == "__main__":
    print("Task 1:")
    print(for_loop(n=10))

    print("Task 2:")
    print(while_loop(n=8))
