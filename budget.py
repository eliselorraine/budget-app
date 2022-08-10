class Category:
    def __init__(self, budget_category):
        self.budget_category = budget_category
        self.ledger = list()
        self.funds = 0
    
    def __repr__(self):
        title_length = 30 - len(self.budget_category)
        # what happens if the length is an odd number, you cannot multiply with a float
        title_line = "*" * (title_length / 2)
        title = f'{title_line}{self.budget_category}{title_line}'
        print(title)
        for x in range(len(self.ledger)):
            return f"{self.ledger[x]['description']} {self.ledger[x]['amount']}"

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

    

food = Category('Food')
print(food)

def create_spend_chart(categories):
    print('last method')