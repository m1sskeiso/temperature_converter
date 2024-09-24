# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Main program
def temperature_converter():
    print("Temperature Converter")
    
    # Ask the user to input a temperature
    temperature = float(input("Enter the temperature: "))
    
    # Ask the user to select the conversion type
    print("Choose the conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        # Convert Celsius to Fahrenheit
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {result:.2f}°F.")
        
    elif choice == '2':
        # Convert Fahrenheit to Celsius
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is equal to {result:.2f}°C.")
        
    else:
        print("Invalid choice. Please select 1 or 2.")

# Run the program
temperature_converter()
