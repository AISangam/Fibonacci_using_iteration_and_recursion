import time


def fibonacci_using_recursion(i):
 
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci_using_recursion(i - 1) + fibonacci_using_recursion(i - 2)



def fibonacci_using_iteration(i):

    # fixed conditions
    previous = 0
    current = 1

    # apply the loop
    for j in range(1, i):
        previous_previous =  previous
        previous = current
        current = previous_previous + previous

    return current



n = int(input("Enter the nth fibonacci number to find: "))
start_time = time.time()
print("Result from recursive method is: {}".format(fibonacci_using_recursion(i=n)))
print("Result from iterative method is: {}".format(fibonacci_using_iteration(i=n)))
end_time = time.time() - start_time

# one can also calculate the time taken by recursion and iterative call. From the time taken it is 
# proven that iterative method for fibonacci series is better then recursive method