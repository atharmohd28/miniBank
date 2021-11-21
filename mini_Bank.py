class Customer:
    '''customer class developed by Mohd Athar for bank operation'''
    Bank_name="Rights Bank"
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposite(self,Amount):
        self.balance=self.balance+Amount
        print("Balance After Deposite:",self.balance)
    def withdraw(self,Amount):
        if Amount>self.balance:
            print('Insuffiecient Balance...... cannot Perform this opration ')
        else:
            self.balance=self.balance-Amount
            print('Balance after Withdraw:',self.balance)
print('Welcome to',Customer.Bank_name)
name=input('Enter your Name:')
c=Customer(name)
while True:
    print('d-deposite\nw-withdrw\ne-exit')
    option=input('Enter your option:')
    if option.lower()=='d':
        Amount=float(input('Enter Amount to deposite:'))
        c.deposite(Amount)
    elif option.lower()=='w':
        Amount=float(input('Enter Amount to withdraw:'))
        c.withdraw(Amount)
    elif option.lower()=='e':
        print('Thanks For Banking:')
        break
    else:
        print('Invalid option Please Chose valid optin:')