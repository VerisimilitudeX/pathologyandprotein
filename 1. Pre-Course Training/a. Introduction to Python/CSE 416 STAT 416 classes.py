"""
This starter code is written by Pemi Nguyen. Permission is
hereby granted to students registered for University of Washington
CSE 312 for use solely during Fall Quarter 2020 for purposes of
the course.  No other use, copying, distribution, or modification
is permitted without prior written consent.
"""

from typing import Set, Dict
"""
Task 1:
Check if element n exists in set s of integers.
If yes, remove it. Otherwise, add n^2 to s.
"""
def modify_set(s:Set[int], n:int):
    if (n in s):
        s.remove(n)
    else:
        s.add(n**2)

"""
Task 2
We create a class called ModifiedDict which stores a dictionary d
that maps each string to a float. For example:

/"abc" -> 1.2
"se" -> 4.21/

This class has a function add() which adds n to every value in the class dictionary
For example, if n = 3.0, then the class dictionary becomes:

/"abc" -> 4.2
"se" -> 7.21/
"""

class ModifiedDict:
    def __init__(self, d:Dict[str, float]):
        self.d = d

    def add(self, n:float):
        for key in self.d:
            self.d[key] += n

if __name__ == "__main__":
    print("Task 1")
    s = {4, 6, 8}
    print("Set s before test_set(): {}".format(s))
    modify_set(s=s, n=4)
    print("Set s after test_set(): {}".format(s))

    print("Task 2")
    d = {"warm": 4.7, "sun": 5.9}
    md = ModifiedDict(d=d)
    print("md before add(): {}".format(md.d))
    md.add(n=3.4)
    print("md after add(): {}".format(md.d))
