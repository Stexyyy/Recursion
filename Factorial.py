#calculates factoral of a positive integer
def factorial(n):
    #print(n) without this commented it will go from 6 to 0 to 720
    if n == 0:
        return 1
    return n*factorial(n-1)

#function call
print(factorial(6))
