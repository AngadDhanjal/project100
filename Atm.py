class atm:
    def __init__(self, card_number, pin_number):
        self.card_number = card_number
        self.pin_number = pin_number

    def CashWithdrawal(self, amount):
        print("You have withdrawn $" + str(amount) + " from your account")

    def BalanceEnquiry(self):
        print("Your account balance is $1000")

    def ChangePin(self, new_pin):
        self.pin_number = new_pin
        print("Your PIN has been changed successfully")

    def Deposit(self, amount):
        print("You have deposited $" + str(amount) + " into your account")
        
card_number = "1234567890123456"
pin_number = "1234"
my_atm = atm(card_number, pin_number)

my_atm.CashWithdrawal(500)
my_atm.BalanceEnquiry()
my_atm.ChangePin("5678")
my_atm.Deposit(1000)
