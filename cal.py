f = float(input("Enter first number: "))
o = input("Enter operator: ")
s = float(input("Enter second number: "))

if o == "+":
    print(f + s)
elif o == "-":
    print(f - s)
elif o == "/":
    print(f / s)
elif o == "*":
    print(f * s)
else:
    print("wrong operator")
