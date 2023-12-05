import copy
import random
# Consider using the modules imported above.

class Hat:
    # Initialiser la classe avec le contenu du chapeau
    # **balls = nombre variable d'arguments représentant le nombre de boules de chaque couleur dans le chapeau

    def __init__(self, **balls):
        # Convertir les arguments en une liste de boules
        # Exemple: balls = {'red': 2, 'blue': 3...} 
        self.contents = []
        for key, value in balls.items():
            for i in range(value):
                self.contents.append(key)
        print(self.contents)
        
        
  # Méthode pour tirer des boules du chapeau
    def draw(self, num_balls):
        all_removed = []
        if(num_balls > len(self.contents)):
            return self.contents
        for i in range(num_balls):
            removed = self.contents.pop(int(random.random() * len(self.contents)))
            all_removed.append(removed)
        return all_removed        

    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_gotten = hat_copy.draw(num_balls_drawn)
        
        for color in colors_gotten:
            if(color in expected_copy):
                expected_copy[color] -=1
        
        if(all(x <= 0 for x in expected_copy.values())):
            count += 1
    return count / num_experiments



print("*************** TESTS ***************")

# Test
# hat = Hat(red=3, blue=4)
# actual_contents_before_draw = len(hat.contents)  
# print("contenu du chapeau avant tirage =", actual_contents_before_draw)

# drawn_balls, actual_contents_after_draw = hat.draw(2)
# print("boules tirées :", drawn_balls)
# print("contenu du chapeau après tirage =", len(actual_contents_after_draw))

# expected_contents_after_draw = max(0, actual_contents_before_draw - 2)
# print("hat_draw_contents après tirage de 2 boules sur 7 :", len(actual_contents_after_draw) == expected_contents_after_draw)


# Test hat class contents
hat = Hat(red=3, blue=2)
actual = hat.contents
expected = ["red", "red", "red", "blue", "blue"]
print("hat_class_contents:", actual == expected)  
# Résultat attendu : True => OK

# Test hat draw method
hat = Hat(red=5, blue=2)
# retirer 2 balles
actual_draw = hat.draw(2)
# Vérifier si les boules tirées sont rouges ou bleues
expected_draw = all(ball in ["red", "blue"] for ball in actual_draw)
print("hat_draw:", expected_draw)
# Résultat attendu : True


# Test probability experiment
hat = Hat(blue=3, red=2, green=6)
probability = experiment(hat=hat, expected_balls={"green": 1}, num_balls_drawn=1, num_experiments=1000)
print("prob_experiment1:", round(probability, 3) == round(6/11, 3))  
# Résultat attendu : True => false car problème d'arrondi connu!!!!!

hat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
probability = experiment(hat=hat, expected_balls={"yellow": 2, "blue": 3, "test": 1}, num_balls_drawn=20, num_experiments=100)
print("prob_experiment2:", round(probability, 3) == 1.0)  
# Résultat attendu : True

