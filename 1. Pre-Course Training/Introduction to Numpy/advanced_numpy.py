import numpy as np

# HINT: How can you use the zeros method to do this?
def task1():
    return np.zeros((3, 4), dtype=int) + 3
    

def task2():
    array2 = np.array([x for x in range(1, 13)])
    return array2.reshape(3, 4)

# HINT: Using a list might help you here.
def task3():
    array3 = np.array([7, 5, 3, 1])
    return np.tile(array3, (5, 1))

def main():
    print(task1())
    print(task2())
    print(task3())

if __name__ == "__main__":
    main()