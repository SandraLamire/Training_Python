# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

def arithmetic_arranger(problems, show_answers=False):
    # vérifier le nb d'opérations
    # renvoyer une erreur si > 5 opérations
    if len(problems) > 5:
        return "Error: Too many problems."
      
    # initialiser les lignes
    arranged_problems = ""
    line1 = line2 = line3 = line4 = ""

    # itérer sur les opérations
    for problem in problems:
        # séparer nb1 et nb2
        nb1, op, nb2 = problem.split()
        # vérifier si opération + ou -
        if op != "+" and op != "-":
            return "Error: Operator must be '+' or '-'."
        # vérifier si nb1 et nb2 sont des nombres
        if not nb1.isdigit() or not nb2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(nb1)>4 or len(nb2)>4:
            return "Error: Numbers cannot be more than four digits."

        # calculer la largeur en tenant compte du signe
        width = max(len(nb1), len(nb2)) + 2

        # Construire les lignes
        line1 += nb1.rjust(width) + "    "
        line2 += op + nb2.rjust(width - 1) + "    "
        line3 += "-" * width + "    "

        # construire le résultat final
        if show_answers:
            if op == "+":
                answer = str(int(nb1) + int(nb2))
            else:
                answer = str(int(nb1) - int(nb2))
            line4 += answer.rjust(width) + "    "
        else:
            line4 = ""

    # affichage du résultat
    arranged_problems += line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip() + "\n" + line4.rstrip() + "\n"

    return arranged_problems

# N'affiche pas les réponses
print("Opérations sans les réponses :")
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=False))

print("####################################")

# Affiche les réponses
print("Opérations avec les réponses :")
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))

print("############## TESTS ######################")
print(arithmetic_arranger(["3801 - 2", "123 + 49"], show_answers=True))
# Error: Operator must be '+' or '-'.
print(arithmetic_arranger(["1 + 2", "1 * 9380"], show_answers=True))
# Error: Too many problems.
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380', '18 + 2'], show_answers=True))
# Error: Numbers cannot be more than four digits.
print(arithmetic_arranger(['24 + 852150', '3801 - 2', '45 + 43', '123 + 49'], show_answers=True))
# Error: Numbers must only contain digits.
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'], show_answers=True))

