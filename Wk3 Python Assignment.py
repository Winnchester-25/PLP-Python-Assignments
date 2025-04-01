def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Check if discount is 20% or more
        discount_amount = price * (discount_percent / 100)  # Calculate discount
        final_price = price - discount_amount  # Apply discount
        return final_price
    else:
        return price  # Return the original price if discount is less than 20%

# Prompt user for input

original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and print the result
final_price = calculate_discount(original_price, discount_percent)

print(f"The final price after applying the discount is: ${final_price:.2f}")