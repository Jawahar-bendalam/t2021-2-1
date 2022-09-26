a = int(input())
b = int(input())
operator = input()

if operator == "+":
    print("{} + {} = {}".format(a, b, a+b))
elif operator == "-":
    print("{} - {} = {}".format(a, b, a-b))
elif operator == "*":
    print("{} * {} = {}".format(a, b, a*b))
elif operator == "/":
    print("{} / {} = {}".format(a, b, a/b))
else:
    print("Invalid Operator")