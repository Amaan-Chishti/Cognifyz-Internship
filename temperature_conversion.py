def convert_temperature():
    """Converts temperature between Celsius and Fahrenheit."""

    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C or F): ").upper()

    if unit == 'C':
        converted_temp = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {converted_temp}°F")
    elif unit == 'F':
        converted_temp = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {converted_temp}°C")
    else:
        print("Invalid unit. Please enter 'C' or 'F'.")

convert_temperature()