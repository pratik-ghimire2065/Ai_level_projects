print("Learning  ai concepts ")
print("Just adding one commit to learnm git for practice ")
print("Part 2 git diff ")
print("Something happens ")
def add(a,b):
    return a +b
try: 
    a=int(input("Enter a number : ")) 
    b=int(input(f"Enter a another number to add with {a}: "))
except ValueError: 
    print("Wrong input given ")
print(f"The sum of {a} and {b} is ",add(a,b))
def subtract(a,b):
    if a<b:
        return "First number is less than second number try again........"
    else:
        return f"The subtraction of {a} and {b} is : {a-b}"
print(subtract(a,b))
def divide(a,b):
    if b==0:
        return("Zero division error ")
        raise ZeroDivisionError
    else :
        return f"Division of {a} and {b} is {a/b}"
print(divide(a,b))