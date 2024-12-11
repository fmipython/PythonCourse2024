def f1():
    x = input("Type 1: ")
    y = input("Type 2: ")
    op = input("Choose +, -, *, /: ")

    if op == '+':
        try:
            r = int(x) + int(y)
        except:
            try:
                r = float(x) + float(y)
            except:
                r = x + y
    elif op == '-':
        try:
            r = int(x) - int(y)
        except:
            try:
                r = float(x) - float(y)
            except:
                print("Invalid!")
                return
    elif op == '*':
        try:
            r = int(x) * int(y)
        except:
            try:
                r = float(x) * float(y)
            except:
                print("Invalid!")
                return
    elif op == '/':
        try:
            r = int(x) / int(y)
        except:
            try:
                r = float(x) / float(y)
            except:
                print("Invalid!")
                return
    else:
        print("Bad operator!")
        return
    
    print("Result: ", r)

f1()
