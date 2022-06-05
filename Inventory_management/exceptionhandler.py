try:
    a = int(input("Enter the value of a "))
    b = int(input("Enter the value of b "))

    c = z/b
    print(c)
except Exception as e:
    print(e)
finally:
    a = 1
    b = 2
    c = a + b
    print(c)
