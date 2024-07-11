"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    new_account=Account(balance, interest_rate)   
    # Calculate interest earned
    interest = balance * (apr/100 * months/12)
    #be sure to set interest earned to 0

    # ADD YOUR CODE HERE

    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    # new_balance= balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    #use the set_balance 
    self.balance = balance

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    #use the set_interest
    self.interest = interest

    # Return the updated balance and interest earned.
    return  # ADD YOUR CODE HERE
