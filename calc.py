def convert_length(value, from_unit, to_unit):
    units = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1.0,
        "km": 1000.0,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }

    if from_unit in units and to_unit in units:
        return value * units[from_unit] / units[to_unit]
    else:
        return "Invalid units"


def calculate(value1, operator, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        if value2 != 0:
            return value1 / value2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"


def fraction_to_decimal(fraction):
    parts = fraction.split('/')
    if len(parts) == 2:
        numerator, denominator = int(parts[0]), int(parts[1])
        gcd = 1
        for i in range(1, min(abs(numerator), abs(denominator)) + 1):
            if numerator % i == 0 and denominator % i == 0:
                gcd = i
        numerator //= gcd
        denominator //= gcd
        return numerator / denominator
    else:
        return "Invalid fraction format"


def decimal_to_fraction(decimal):
    fraction = round(decimal * 16)
    gcd = 1
    for i in range(1, min(abs(fraction), 16) + 1):
        if fraction % i == 0 and 16 % i == 0:
            gcd = i
    fraction //= gcd
    denominator = 16 // gcd
    return f"{fraction}/{denominator}"


# Example usage:
print(fraction_to_decimal("3/12"))  # Output: 0.25
print(decimal_to_fraction(0.375))    # Output: 6/16



def main():
    print("Welcome to the Unit Converter and Measurement Calculator!")

    while True:
        print("\nChoose an option:")
        print("1. Convert Length")
        print("2. Perform Calculation")
        print("3. Convert Fraction to Decimal and Vice Versa")
        print("4. Close the program")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            value = float(input("Enter the value: "))
            from_unit = input("Enter the source unit (mm, cm, m, km, in, ft, yd, mi): ")
            to_unit = input("Enter the target unit (mm, cm, m, km, in, ft, yd, mi): ")
            result = convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} is equal to {result} {to_unit}")
        elif choice == "2":
            value1 = float(input("Enter the first value: "))
            operator = input("Enter the operator (+, -, *, /): ")
            value2 = float(input("Enter the second value: "))
            result = calculate(value1, operator, value2)
            print(f"The result of {value1} {operator} {value2} is {result}")
        elif choice == "3":
            conversion_choice = input("Choose conversion direction (1. Fraction to Decimal, 2. Decimal to Fraction): ")
            if conversion_choice == "1":
                fraction = input("Enter the fraction in the format of 1/16: ")
                decimal = fraction_to_decimal(fraction)
                print(f"{fraction} is equal to {decimal}")
            elif conversion_choice == "2":
                decimal = float(input("Enter the decimal: "))
                fraction = decimal_to_fraction(decimal)
                print(f"{decimal} is equal to {fraction}")
            else:
                print("Invalid choice")
        elif choice == "4":
            print("Closing the program...")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
