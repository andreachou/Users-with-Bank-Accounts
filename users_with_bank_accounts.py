class BankAccount:

    # for Ninja Bonus - Create a class variable
    accounts = []

    # constructor
    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance

        # for Ninja Bonus
        BankAccount.accounts.append(self)

    # increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self

    # decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        else:
            self.balance -= amount 
        return self
        

    # print to the console: eg. "Balance: $100"
    def display_account_info(self):
        return f"{self.balance}"

    # increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.interest_rate)
        return self

    # for Ninja Bonus
    @classmethod
    def display_all_account_info(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # original code for users only having one account:
        # self.account = BankAccount(interest_rate=0.02, balance=0)

        # Allow users to have multiple accounts
        self.account = {
            "checking" : BankAccount(0.02, 0),
            "savings" : BankAccount(0.05, 0)
        }

    def make_deposit(self, amount, account_type):
        self.account[account_type].deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        # Allow users to have multiple accounts
        print(f"{self.name}, Checking Account Balance: ${self.account['checking'].display_account_info()}")
        print(f"{self.name}, Savings Account Balance: ${self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self, account_type, amount, other_user, other_user_acct_type):
        if amount < self.account[account_type].balance:
            self.account[account_type].balance -= amount
            other_user.account[other_user_acct_type].balance += amount
        else:
            print("Insufficient funds")
        return self


user1 = User("Kevin", "kevin@gmail.com")
user2 = User("Andy", "andy@hotmail.com")

user1.make_deposit(200, "checking")     # can also use user1.account.deposit(200) so we dont need make_deposit() method in Uesr class. Same with make_withdrawal
user1.account["savings"].deposit(100000).deposit(2000)
user1.display_user_balance() # same with user1.account.display_account_info()

user1.transfer_money("savings", 3000, user2, "checking")

user1.display_user_balance()
user2.display_user_balance()
