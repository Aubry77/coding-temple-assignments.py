def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return None

try:
    temperature = input("Please enter the temperature in Fahrenheit: ")
    celsius = fahrenheit_to_celsius(temperature)

    if celsius is not None:
        print(f"{temperature} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
finally:
    print("Thank you for using the weather forecast application!")

    