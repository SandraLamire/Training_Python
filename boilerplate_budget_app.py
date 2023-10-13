# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app


class Category:
    # Initialiser les propriétés category et ledger (= registre) avec les valeurs passées en argument
    # ledger = None évite les  listes partagées entre les instances
    def __init__(self, category, ledger=None):
        self.category = category
        self.ledger = ledger if ledger is not None else []

    # Ajouter un nouvel objet à la liste ledger au format {"amount": amount, "description": description}
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    #  Stocker le montant comme un nombre négatif dans le ledger
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    # Transfèrer un montant à une autre catégorie de budget
    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": -amount, "description": "Transfer to " + other.category}
            )
            other.ledger.append(
                {"amount": amount, "description": "Transfer from " + self.category}
            )
            return True
        return False

    # Renvoyer le solde actuel du budget basé sur les dépôts et retraits
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return balance

    # Vérifier si le montant peut être retiré du budget sans dépasser le solde actuel
    def check_funds(self, amount):
        return self.get_balance() >= amount

    # retourne une chaîne représentant le budget
    def __str__(self):
        # Calculer la largeur maximale pour la colonne des descriptions
        max_description_length = max(
            len(transaction["description"]) for transaction in self.ledger
        )
        # Ajouter une marge pour améliorer la lisibilité
        column_width = max(max_description_length + 1, len("Total:") + 1)

        # Inclure le titre de la catégorie centré de 30 caractères
        output = self.category.center(column_width + 7, "*") + "\n"
        for transaction in self.ledger:
            # Ajouter les éléments du ledger
            description = transaction["description"][:column_width].ljust(column_width)

            # Ajouter des espaces entre description et montant
            amount = f"{transaction['amount']:+.2f}" if transaction['amount'] >= 0 else f"{transaction['amount']:.2f}"
            amount = amount.rjust(column_width - len(description) + 8)

            output += f"{description}{amount}\n"

        # Ajouter des espaces entre Total: et montant
        total_amount = f"{self.get_balance():.2f}".rjust(column_width + 2)
        output += f"Total:{total_amount}\n"
        return output

    def create_spend_chart(categories):
        # Calcul des pourcentages dépensés par catégorie
        total = 0
        for category in categories:
            total += category.get_balance()
        percentages = []
        for category in categories:
            percentages.append(category.get_balance() / total * 100)

        # Création de la chaîne de caractères représentant le budget
        output = ""
        for i in range(max(percentages)):
            for category in categories:
                if percentages[categories.index(category)] >= i:
                    output += "o  "
                else:
                    output += "   "
            output += "\n"
        output += "    "
        for i in range(len(categories)):
            output += f"{categories[i].category[:3]:3}  "
        output += "\n"
        return output


print("*************** TESTS ***************")
# Créer une instance de la classe Category pour tester les méthodes
food = Category("Food")


# Test de la méthode deposit
food.deposit(900, "deposit")
print("food.ledger after deposit:", food.ledger)
# [{'amount': 900, 'description': 'deposit'}]


# Test de la méthode deposit sans description
food.deposit(45.56)
print("food.ledger after deposit:", food.ledger)
# [{'amount': 900, 'description': 'deposit'}, {'amount': 45.56, 'description': ''}]


# Test de la méthode withdraw
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
print("food.ledger after withdraw:", food.ledger)
# [{'amount': 900, 'description': 'deposit'}, {'amount': -45.67, 'description': 'milk, cereal, eggs, bacon, bread'}]


# Test de la méthode withdraw sans description
good_withdraw = food.withdraw(45.67)
print("food.ledger after withdraw:", food.ledger)
# [{'amount': 900, 'description': 'deposit'}, {'amount': -45.67, 'description': 'milk, cereal, eggs, bacon, bread'}, {'amount': -45.67, 'description': ''}]
print("food.ledger after withdraw:", good_withdraw)
# True


# Test de la méthode get_balance
print("food.get_balance:", food.get_balance())
# 854.22


# Test de la méthode transfer
entertainment = Category("Entertainment")
transfer_amount = 20
food_balance_before = food.get_balance()
entertainment_balance_before = entertainment.get_balance()
good_transfer = food.transfer(transfer_amount, entertainment)
food_balance_after = food.get_balance()
entertainment_balance_after = entertainment.get_balance()
print(food.ledger)
# [{'amount': 900, 'description': 'deposit'}, {'amount': -45.67, 'description': 'milk, cereal, eggs, bacon, bread'}, {'amount': -45.67, 'description': ''}, {'amount': -20, 'description': 'Transfer to Entertainment'}] => OK
print("transfer:", good_transfer)
# True
print("transfer:", food_balance_before - food_balance_after)
# Doit afficher : 20 => affiche 20.0
print("transfer:", entertainment_balance_after - entertainment_balance_before)
# 20
print("transfer:", entertainment.ledger)
# [{'amount': 20, 'description': 'Transfer from Food'}]


# Test de la méthode check_funds
print("check_funds - 20 :", food.check_funds(20))
# True
print("check_funds - 10 :", food.check_funds(10))
# True


# Test de la méthode withdraw_no_funds
good_withdraw = food.withdraw(100.10)
print("withdraw_no_funds :", good_withdraw)
# True


# Test de la méthode transfer_no_funds
entertainment.deposit(100, "deposit")
good_transfer = food.transfer(200, entertainment)
print("transfer_no_funds", good_transfer)
# True


# Test de la méthode to_string
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)
print("méthode to_string : \n", str(food))

#  ******************Food******************
# deposit                           +900.00
#                                    +45.56
# milk, cereal, eggs, bacon, bread   -45.67
#                                    -45.67
# Transfer to Entertainment          -20.00
#                                   -100.10
# Transfer to Entertainment         -200.00
# deposit                           +900.00
# milk, cereal, eggs, bacon, bread   -45.67
# Transfer to Entertainment          -20.00
# Total:                            1368.45
