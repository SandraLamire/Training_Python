import random
import copy

class Hat:
    def __init__(self, **balls):
        self.contents = [color for color, quantity in balls.items() for _ in range(quantity)]

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            # Si on demande toutes les balles ou plus, retourner toutes les balles
            drawn_balls = list(self.contents)
            self.contents = []
        else:
            # Sinon, tirer num_balls balles au hasard
            drawn_balls = random.sample(self.contents, num_balls)
            self.contents = [ball for ball in self.contents if ball not in drawn_balls or drawn_balls.count(ball) > self.contents.count(ball)]

        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn = hat_copy.draw(num_balls_drawn)

        # Compter le nombre total de chaque balle tirée
        drawn_count = {color: drawn.count(color) for color in set(drawn)}
        #print("drawn_count:", drawn_count)

        # Vérifier si les balles tirées correspondent aux attentes
        if all(drawn_count.get(color, 0) >= count for color, count in expected_balls.items()):
            successful_experiments += 1
            #print("Success!")

    return successful_experiments / num_experiments



# Test hat draw method
hat = Hat(red=5, blue=2)
# retirer 2 balles
actual_draw = hat.draw(2)
# Vérifier si le contenu du chapeau est correct après le tirage de 2 balles sur 7
expected_contents_after_draw = len(hat.contents) == 5
print("hat_draw_contents après tirage de 2 boules sur 7 :", expected_contents_after_draw)
# Résultat attendu : True

# Résultat attendu : True => retourne False

# Test hat class contents
hat = Hat(red=3, blue=2)
actual = hat.contents
expected = ["red", "red", "red", "blue", "blue"]
print("hat_class_contents:", set(actual) == set(expected))
# Résultat attendu : True => OK

# Test hat draw method
hat = Hat(red=5, blue=2)
# retirer 2 balles
actual_draw = hat.draw(2)
# Vérifier si les boules tirées sont rouges ou bleues
expected_draw = all(ball in ["red", "blue"] for ball in actual_draw)
print("hat_draw:", expected_draw)
# Résultat attendu : True => OK

# Test probability experiment
hat = Hat(red=3, blue=4)
probability = experiment(hat=hat, expected_balls={"red": 2, "blue": 1}, num_balls_drawn=3, num_experiments=100)
print("prob_experiment1:", round(probability, 3) == 1.0)
# Résultat attendu : True => retourne False

hat = Hat(yellow=5, red=1, green=3, blue=9, test=1)
probability = experiment(hat=hat, expected_balls={"yellow": 2, "blue": 3, "test": 1}, num_balls_drawn=20, num_experiments=100)
print("prob_experiment2:", round(probability, 3) == 1.0)  
# Résultat attendu : True => OK