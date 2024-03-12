class cardholder():
    transaction_history=()
    def __init__(self,cardnumber, pin, firstname, lastname, balance):
        self.cardnumber=cardnumber
        self.pin=pin
        self.firstname=firstname
        self.lastname=lastname
        self.balance=balance

#getter methods
    def get_cardnumber(self):
        return self.cardnumber
    def get_pin(self):
        return self.pin
    def get_firstname(self):
        return self.firstname
    def get_lastname(self):
        return self.lastname
    def get_balance(self):
        return self.balance
#setter methods
    def set_cardnumber(self,newvalue):
        self.cardnumber=newvalue
    def set_pin(self,newvalue):
        self.pin=newvalue
    def set_firstname(self,newvalue):
        self.firstname=newvalue 
    def set_lastname(self,newvalue):
        self.lastname=newvalue
    def set_balance(self,newvalue):
        self.balance=newvalue

    def print_out(self):
        print(f'''Card{self.cardnumber}
              Pin{self.pin}
              First Name{self.firstname}
              Last Name{self.lastname}
              Balance{self.balance}''')
              