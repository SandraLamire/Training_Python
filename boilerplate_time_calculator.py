# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator
from datetime import datetime, timedelta, time, date


def add_time(start, duration, start_day=None):
    # Analyser le temps de départ et la durée : convertir le temps en objet datetime
    start_time = datetime.strptime(start, "%I:%M %p")
    # gérer les durées au-delà de 24 heures
    # Extract heures et minutes de la durée
    hours, minutes = map(int, duration.split(":"))
    duration_time = timedelta(hours=hours, minutes=minutes)

    # Ajouter la durée au temps de départ
    end_time = start_time + duration_time

    # Calculer les jours passés
    #   if end_time.hour < start_time.hour or (end_time.hour == start_time.hour and end_time.minute < start_time.minute):
    #     days_passed = (end_time - start_time).days + 1
    #   else:
    #     days_passed = (end_time - start_time).days
    # OU :
    days_passed = end_time.day - start_time.day

    # Formater le résultat
    new_time = end_time.strftime("%I:%M %p")

    # Gérer le jour de la semaine
    # si le jour de la semaine de départ est fourni en paramètre, ajoutez-le au résultat
    if start_day:
        start_day = start_day.lower().capitalize()
        new_time += f", {start_day}"
    # Gérer les cas spéciaux
    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    # retourner le résultat
    return new_time


print(add_time("11:06 PM", "2:02"))
# 01:08 AM

print(add_time("3:00 PM", "3:10"))
# 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
