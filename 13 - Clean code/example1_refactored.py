import sys

COMMON_OPERATIONS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
}

INT_OPERATIONS = {
    **COMMON_OPERATIONS,
    "/": lambda x, y: x // y,
}

FLOAT_OPERATIONS = {
    **COMMON_OPERATIONS,
    "/": lambda x, y: x / y,
}


def apply_operation_to_ints(x: int, y: int, operation: str):
    if operation not in INT_OPERATIONS:
        raise ValueError("Invalid operation")

    return INT_OPERATIONS[operation](x, y)


def apply_operation_to_float(x: float, y: float, operation: str):
    if operation not in FLOAT_OPERATIONS:
        raise ValueError("Invalid operation")

    return FLOAT_OPERATIONS[operation](x, y)


def parse_number(number: str) -> int | float:
    match number:
        case ".":
            return float(number)
        case _:
            return int(number)


if __name__ == "__main__":
    x = input("First number: ")
    try:
        x = parse_number(x)
    except ValueError:
        print("Invalid value", file=sys.stderr)
        sys.exit(1)

    try:
        y = parse_number(input("Second number: "))
    except ValueError:
        print("Invalid value", file=sys.stderr)
        sys.exit(1)

    operation = input("Choose +, -, *, /: ")

    try:
        result = apply_operation_to_ints(x, y, operation)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
    except ZeroDivisionError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)

    print(result)
