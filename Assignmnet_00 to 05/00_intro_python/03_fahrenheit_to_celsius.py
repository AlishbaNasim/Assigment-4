def main():
    print(" Covert temperature in Fahrenheit!! ")

    degrees_fahrenheit = float(input("Enter temperature here to convert in fahrenheit:"))

    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

    print(f"Temperature: {degrees_fahrenheit} = {degrees_celsius}C")

if __name__ == '__main__':
    main()