# The exceptions that can occur in this function are 
# 1. Value error - user enters data other than int
# 2. EOF error - user enters ctrl-d & does not provide input
def add():
    while True:
        a = int(input())
        b = int(input())
        c = a + b
        print("Addition =",c)
        print("Add Again")

# Here is another version of add() function that handles exceptions & displays
# appropriate message
def add_with_exception_handling():
    while True:
        try:
            a = int(input())
            b = int(input())
            c = a + b
            print("Addition =",c)
        except ValueError:
            print("Enter an integer")
        except EOFError:
            print("Give 2 numbers as input")
        finally:
            print("Add Again")

add_with_exception_handling()
