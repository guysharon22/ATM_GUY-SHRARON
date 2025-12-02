# ATM_GUY-SHRARON

###################
Eran's comments:
In general, good job.
Key Strengths (Excellent Implementation)
Data Structure: Using a list of dictionaries for customers is the ideal way to manage user data .
Modularity: Breaking down the logic into functions (find_customer, deposit, withdraw, etc.) is excellent for organization and readability.
Robustness: The use of try-except blocks in deposit and withdraw (option 5) is great for handling invalid (non-numeric) user input.
Continuous Operation: The while True: main() loop at the end correctly allows the ATM to serve multiple customers one after another, and the while True loop inside main() handles the continuous transaction menu.
Withdrawal (Option 5): The code correctly applies the insufficient balance check (amount > customer["balance"]) .
Bonus Features: The student correctly implemented the functions for Change PIN (change_pin) and Print Receipt (print_recipe). The PIN check for 4 digits is also present in change_pin.
Point for improvement:
Add some documentation and an explanation to the README file. What is the target of the script, how to run it,etc.
Updating the Menu Display: Adding the 'p' and 'r' options to the atm_menu() function.
Adjusting Output Text: Changing the success messages to "OK" and fixing the final "Quit" message.
