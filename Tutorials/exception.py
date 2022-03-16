def division(first , second):
    div = first / second 
    return div


try:
    first=int(input("first number: "))
    second=int(input("second number: "))
    print(division(first, second))
except ValueError:
    print("type only numbers")
except ZeroDivisionError:
    print("0 gives infinity")

