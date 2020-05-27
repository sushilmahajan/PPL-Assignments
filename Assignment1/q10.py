a = float(input("Enter first term in the GM: "))
r = float(input("Enter common ratio of the GM: "))

for i in range (0, 10):
    term = a * (r ** i)
    print(term)
