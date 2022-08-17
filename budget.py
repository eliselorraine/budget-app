class Category:
    def __init__(self, budget_category):
        self.budget_category = budget_category
        self.ledger = list()
        self.funds = 0
    
    def __repr__(self):
        print_ledger = ""
        title = self.budget_category.center(30, "*")
        print_ledger = print_ledger + title + "\n"
        for x in range(len(self.ledger)):
            desc = self.ledger[x]['description']
            desc = desc[0:23]
            amount = str(self.ledger[x]['amount'])
            cents = ".00"
            if amount.find('.') == -1:
                amount = amount + cents 
            amount = amount[0:7]
            line = "{:<23}{:>7}\n".format(desc, amount)
            print_ledger = print_ledger + line
        return print_ledger

    def deposit(self, amount, description=""):
        self.funds = self.funds + amount
        self.ledger.append({"amount": amount, "description": description})
        print(self.ledger[0]['description'])

    def check_funds(self, amount):
        if amount > self.funds:
            return False
        else:
            return True   
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount) != True:
            return False
        self.funds = self.funds - amount
        amount = amount - (amount*2)
        self.ledger.append({"amount": amount, "description": description})
        return True
      
    def get_balance(self):
        return self.funds

    def transfer(self, amount, new_category):
        if self.check_funds(amount) != True:
            return False
        new_category.deposit(amount, f"Transfer from {self.budget_category}")
        self.withdraw(amount, f"Transfer to {new_category.budget_category}")
        return True

    

food = Category('Groceries')
print(food)

def create_spend_chart(categories):
    print('last method')

