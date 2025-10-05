from bank_account import BankAccount

account = BankAccount(100)   # start with $100
account.deposit(50)          # add $50
account.withdraw(30)         # take out $30
account.display_balance()    # should print $120
