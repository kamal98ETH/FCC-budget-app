class Category:
    # Constractor:
    def __init__(self, category):
        self.category = category
        self.ledger = list()

    # Deposite method:
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": float(amount), "description": description})

    # Withdraw method:
    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            self.ledger.append(
                {"amount": float(amount) * -1, "description": description}
            )
            return True
        else:
            return False

    # Get balance method:
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total = total + item["amount"]
        return total

    # Transfer method:
    def transfer(self, amount, budget_category):
        self.budget_category = budget_category
        if self.check_funds(amount) == True:
            self.withdraw(
                amount, "Transfer to " + budget_category.category.capitalize()
            )
            budget_category.deposit(
                amount, "Transfer from " + self.category.capitalize()
            )
            return True
        else:
            return False

    # Checking funds method:
    def check_funds(self, amount):
        total = 0
        for item in self.ledger:
            total = total + item["amount"]
        if total < amount:
            return False
        else:
            return True

    # Printing object
    def __repr__(self):
        half = (30 - len(self.category)) / 2
        stars = int(half) * "*"
        if len(self.category) % 2 == 0:
            title = stars + self.category.capitalize() + stars + "\n"
        else:
            title = stars + "*" + self.category.capitalize() + stars + "\n"
        items = ""
        for line in self.ledger:
            descrip = line["description"][:23]
            amount = "{:.2f}".format(line["amount"])
            spaces = (30 - len(descrip) - len(amount)) * " "
            item = descrip + spaces + amount + "\n"
            items = items + item
        total = "Total: " + "{:.2f}".format(self.get_balance())
        output = title + items + total
        return output


def create_spend_chart(categories):
    # Calculating
    longest = 0
    nameList = list()
    withdrawsList = list()
    persontages = list()
    total_withdraws = 0

    for category in categories:
        category_name = category.category
        nameList.append(category_name.capitalize())
        if len(category_name) > longest:
            longest = len(category_name)
        category_withdraws = 0

        for line in category.ledger:
            if line["amount"] < -1:
                category_withdraws = category_withdraws + (line["amount"] * -1)
                total_withdraws = total_withdraws + (line["amount"] * -1)
        withdrawsList.append(category_withdraws)

    for withdraw in withdrawsList:
        percentage = int((withdraw / total_withdraws) * 10)
        persontages.append(percentage)

    # Displating
    line1 = ""
    line2 = "    -"
    line3 = ""
    for i in reversed(range(11)):
        if i == 10:
            line = str(i * 10) + "| "
        elif i != 0:
            line = " " + str(i * 10) + "| "
        else:
            line = "  " + str(i * 10) + "| "
        for persontage in persontages:
            if persontage >= i:
                line = line + "o  "
            else:
                line = line + "   "
        line1 = line1 + line + "\n"
    for i in nameList:
        line2 = line2 + "---"
    line2 = line2 + "\n"
    for i in range(longest):
        line3 = line3 + "     "
        for name in nameList:
            try:
                line3 = line3 + name[i] + "  "
            except:
                line3 = line3 + "   "
        line3 = line3 + "\n"

    lines = line1 + line2 + line3
    lines = lines.rstrip() + "  "
    display = "Percentage spent by category\n" + lines
    return display
