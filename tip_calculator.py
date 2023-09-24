# tip_calculator.py

# TODO: Create a function named calculate_tip
try:  #DO NOT MODIFY


    # TODO:
        # Get these user inputs
        # total_cost (float): The cost of the meal (without tax)
        # num_people (int): The number of people splitting the bill
        # tip_percentage (float): The tip percentage
    def tip_calculator():
        total_cost = float(input("how much was the meal before taxes? "))
        num_people = int(input("how many people are splitting the bill? "))
        tip_percentage = float(input("what percent is the tip? "))
        tip = total_cost * tip_percentage / 100
        tax = total_cost * 0.1
        total_bill = format(float(total_cost + tax + tip), ".2f")
        payment = format(float(float(total_bill) / num_people), ".2f")
        print(f"Total bill: ${total_bill}")
        print(f"Each person should pay: ${payment}")

    
    # TODO:
        # Calculate the total bill including tip and sales tax (10%).
        # Convert to float: The total bill (including tip and sales tax).

    # NOTE: Calculate the tip and tax separately. 
     
    # TODO: 
        # Calculate how much each person should pay.
        # Convert to float: The amount each person should pay.   
    
    # TODO:
        # Using an f-string, print two different statements 
        # Total bill: $0.00
        # Each person should pay: $0.00

    # NOTE: The amounts are displayed with 2 decimals only

except ValueError:
    print("Your input is invalid") # TODO: modify this except to include a Built-in Exception
        # TODO: Print an statement telling the user their input is invalid 
    
    
if __name__ == "__main__": # DO NOT MODIFY
    tip_calculator() # DO NOT MODIFY
