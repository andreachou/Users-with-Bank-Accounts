# Users with Bank Accounts

## Coding Dojo Core Assignement 06.14.2022

<br/>

Continue with "Bank Account" assignment: https://github.com/andreachou/BankAccount

Update your existing ```User``` class to have an association with the ```BankAccount``` class. You should not have to change anything in the ```BankAccount``` class. 

For example, from the User class we should be able to deposit money into the user's account:

```py
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    # other methods
    
    def make_deposit(self, amount):
    	# your code here
```


But our ```User``` class does not have a ```self.account_balance``` attribute. What it does have is an instance of a ```BankAccount``` by the name of self.account. That means that we'll be mirroring the methods created in the ```BankAccount``` class like make_deposit (and other methods referencing ```self.account_balance```). But we'll be calling on the ```BankAccount``` class to do most of the work! That's the goal of this assignment, and you may find that you do not have to add much logic if any. 

Remember in our ```User``` methods, we can now access the ```BankAccount``` class through our self.account attribute, like so:

```py

class User:
    def example_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
    	print(self.account.balance)		# or access its attributes

```

<br/>

Steps:

* Update the User class``` __init__``` method
* Add a make_deposit method to the User class that calls on it's bank account's instance methods.
* Add a make_withdrawal method to the User class that calls on it's bank account's instance methods.
* Add a display_user_balance method to the User class that displays user's account balance
* SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
* SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.