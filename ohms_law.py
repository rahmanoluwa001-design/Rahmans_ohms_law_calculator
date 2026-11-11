# OHM'S LAW AND POWER CALCULATOR

# ND1 Mechatronics Engineering Mini Project

# This program calculates voltage, current, resistance

# and electrical power using Ohm's Law.

# Calculation history is also stored as an extra feature.

# Function to calculate voltage

def calculate_voltage():

    current = float(input("Enter current in Amperes (A): "))

    resistance = float(input("Enter resistance in Ohms (Ω): "))

    voltage = current * resistance

    print(f"Voltage = {voltage:.2f} V")

    return f"Voltage = {voltage:.2f} V"

# Function to calculate current

def calculate_current():

    voltage = float(input("Enter voltage in Volts (V): "))

    resistance = float(input("Enter resistance in Ohms (Ω): "))

    if resistance == 0:

        print("Error: Resistance cannot be zero.")

        return None

    current = voltage / resistance

    print(f"Current = {current:.2f} A")

    return f"Current = {current:.2f} A"

# Function to calculate resistance

def calculate_resistance():

    voltage = float(input("Enter voltage in Volts (V): "))

    current = float(input("Enter current in Amperes (A): "))

    if current == 0:

        print("Error: Current cannot be zero.")

        return None

    resistance = voltage / current

    print(f"Resistance = {resistance:.2f} Ω")

    return f"Resistance = {resistance:.2f} Ω"

# Function to calculate electrical power

def calculate_power():

    voltage = float(input("Enter voltage in Volts (V): "))

    current = float(input("Enter current in Amperes (A): "))

    power = voltage * current

    print(f"Power = {power:.2f} W")

    return f"Power = {power:.2f} W"

# Main program

def main():

    # Stores previous calculations

    history = []

    print("===================================")

    print("   OHM'S LAW AND POWER CALCULATOR")

    print("===================================")

    while True:

        print("\nChoose what you want to calculate:")

        print("1. Voltage")

        print("2. Current")

        print("3. Resistance")

        print("4. Power")

        print("5. View Calculation History")

        print("6. Exit")

        try:

            choice = int(input("\nEnter your choice (1-6): "))

            if choice == 1:

                result = calculate_voltage()

            elif choice == 2:

                result = calculate_current()

            elif choice == 3:

                result = calculate_resistance()

            elif choice == 4:

                result = calculate_power()

            elif choice == 5:

                print("\n===== CALCULATION HISTORY =====")

                if len(history) == 0:

                    print("No calculations have been performed yet.")

                else:

                    for item in history:

                        print(item)

                continue

            elif choice == 6:

                print("Thank you for using the calculator!")

                break

            else:

                print("Invalid choice. Please select between 1 and 6.")

                continue

            # Save successful calculations

            if result is not None:

                history.append(result)

        except ValueError:

            print("Invalid input! Please enter numbers only.")

        print("\n-----------------------------------")

# Run the program

main()
