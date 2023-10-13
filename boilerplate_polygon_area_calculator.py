
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width
  
  def set_height(self, height):
    self.height = height
  
  def get_area(self):
    return self.width * self.height
  
  def get_perimeter(self):
    return 2 * (self.width + self.height)
  
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  # renvoyer une chaîne représentant la forme avec des étoiles ("*")
  # gérer si largeur ou hauteur > 50
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    return ("*" * self.width + "\n") * self.height

  # calculer combien de fois la forme passée en argument peut s'insérer dans la forme actuelle
  def get_amount_inside(self, shape):
    return (self.width // shape.width) * (self.height // shape.height)

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  
# Square doit être une sous-classe de Rectangle
class Square(Rectangle):
  # Appeler le constructeur de la classe mère avec side pour les paramètres width et height
  def __init__(self, side):
      super().__init__(side, side)
      self.side = side

  # Redéfinir la méthode set_width(self, width)
  def set_width(self, width):
      self.width = width
      self.height = width
      self.side = width

  # Redéfinir la méthode set_height(self, height)
  def set_height(self, height):
      self.width = height
      self.height = height
      self.side = height

  # Ajouter la méthode set_side(self, side) pour mettre à jour à la fois la largeur et la hauteur
  def set_side(self, side):
      super().set_width(side)
      super().set_height(side)
      self.side = side
    
  # Redéfinir la méthode __str__
  def __str__(self):
    return f"Square(side={self.side})"
      

print("*************** TESTS ***************")     
# Test subclass relationship
print("subclass:", issubclass(Square, Rectangle))
# Expected: True => OK

# Test distinct classes
print("distinct_classes:", Square is not Rectangle)
# Expected: True => OK

# Test square is instance of both Square and Rectangle
sq = Square(5)
print("square_is_square_and_rectangle:", isinstance(sq, Square) and isinstance(sq, Rectangle))
# Expected: True => OK

# Test string representation of Rectangle
rect = Rectangle(3, 6)
print("rectangle_string:", str(rect) == "Rectangle(width=3, height=6)")
# Expected: True => OK

# Test string representation of Square
sq = Square(5)
expected = "Square(side=5)"
print("square_string:", str(sq) == expected)
# Expected: True => OK

# Test area of Rectangle and Square
print("area_rectangle:", rect.get_area() == 18)
# Expected: True => OK
print("area_square:", sq.get_area() == 25)
# Expected: True => OK

# Test perimeter of Rectangle and Square
print("perimeter_rectangle:", rect.get_perimeter() == 18)
# Expected: True => OK
print("perimeter_square:", sq.get_perimeter() == 20)
# Expected: True => OK

# Test diagonal of Rectangle and Square
print("diagonal_rectangle:", rect.get_diagonal() == 6.708203932499369)
# Expected: True => OK
print("diagonal_square:", sq.get_diagonal() == 7.0710678118654755)
# Expected: True => OK

# Test setting attributes of Rectangle and Square
rect.set_width(7)
rect.set_height(8)
sq.set_side(2)
print("set_attributes:", str(rect) == "Rectangle(width=7, height=8)" and str(sq) == "Square(side=2)")
# Expected: True => OK

# Test picture representation of Rectangle
rect.set_width(7)
rect.set_height(3)
print("rectangle_picture:", rect.get_picture() == "*******\n*******\n*******\n")
# Expected: True => OK

# Test picture representation of Square
sq.set_side(2)
print("square_picture:", sq.get_picture() == "**\n**\n")
# Expected: True => OK

# Test picture representation of Rectangle with width > 50
rect.set_width(51)
rect.set_height(3)
print("big_picture:", rect.get_picture() == "Too big for picture.")
# Expected: True => OK

# Test get_amount_inside method
rect.set_height(10)
rect.set_width(15)
print("get_amount_inside:", rect.get_amount_inside(sq) == 6)
# Expected: True

# Test get_amount_inside method with two rectangles
rect2 = Rectangle(4, 8)
print("get_amount_inside_two_rectangles:", rect2.get_amount_inside(rect) == 1)
# Expected: True

# Test get_amount_inside method with none
rect2 = Rectangle(2, 3)
print("get_amount_inside_none:", rect2.get_amount_inside(rect) == 0)
# Expected: True => OK

print()
print("*************** EXEMPLES ***************") 

# Exemple d'utilisation avec Rectangle
print("Exemples d'utilisation avec Rectangle:")
rect = Rectangle(10, 5)
print(rect.get_area())
# 50
rect.set_height(3)
print(rect.get_perimeter())
# 26
print(rect)
# Rectangle(width=10, height=3)
print(rect.get_picture())
#  **********
#  **********
#  **********

# Exemple d'utilisation avec Square
print("Exemples d'utilisation avec Square:")
sq = Square(9)
print(sq.get_area())
# 81
sq.set_side(4)
print(sq.get_diagonal())
# 5.656854249492381
print(sq)
#Square(side=4)
Rectangle(width=10, height=3)
print(sq.get_picture())
# ****
# ****
# ****
# ****

# Exemple d'utilisation de get_amount_inside
print("Exemples d'utilisation avec get_amount_inside:")
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
# 8