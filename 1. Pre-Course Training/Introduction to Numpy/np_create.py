import numpy as np

def task1():
    # Generate and return the following array: [3, 2, 5, 6]
    return np.array([3, 2, 5, 6])
    

def task2():
    # TODO: Generate and return an array of the cubes of every integer 
    # from 3 to 9 (inclusive).
    # HINT: remember we can easily generate lists using list comprehension
    return np.array([x**3 for x in range(3, 10)])
    
    

def task3():
    # TODO: Generate and return an array of every 3rd number 
    # from 10 to 20 (inclusive)
    return np.array([x for x in range(10, 20, 3)])
    

def main():
    print("Array: " + str(task1()) + ", Shape: " + str(task1().shape))
    print(task2())
    print(task3())

if __name__ == "__main__":
    main()
