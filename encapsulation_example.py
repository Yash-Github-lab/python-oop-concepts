class BankAccount:
    """Example of encapsulation with private attributes"""
    
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.__balance = balance  # Private attribute (name mangling with __)
        self.__transaction_history = []
    
    # Getter method
    def get_balance(self):
        """Return the current balance"""
        return self.__balance
    
    # Setter method with validation
    def deposit(self, amount):
        """Add money to account"""
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposited: ${amount}")
            return f"Successfully deposited ${amount}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """Remove money from account"""
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrew: ${amount}")
            return f"Successfully withdrew ${amount}"
        return "Insufficient funds or invalid amount"
    
    def get_transaction_history(self):
        """Return transaction history"""
        return self.__transaction_history


# Usage
account = BankAccount("John", 1000)
print(account.deposit(500))  # Successfully deposited $500
print(account.withdraw(200))  # Successfully withdrew $200
print(account.get_balance())  # 1300
print(account.get_transaction_history())  # ['Deposited: $500', 'Withdrew: $200']

# Cannot directly access private attributes
# print(account.__balance)  # This will raise AttributeError