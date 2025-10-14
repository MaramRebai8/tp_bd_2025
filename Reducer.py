#!/usr/bin/env python3
import sys

current_country = None
current_sum = 0.0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue  # ignorer les lignes vides

    # Essayer de séparer par tabulation
    parts = line.split('\t')

    # Si pas de tabulation, séparer par espace
    if len(parts) < 2:
        parts = line.split()
        if len(parts) < 2:
            continue  # ignorer les lignes mal formées

    country = parts[0].strip()
    value_str = parts[1].strip()

    # Nettoyer et convertir la valeur
    try:
        value = float(value_str)
    except ValueError:
        continue  # ignorer si ce n’est pas un nombre

    # Accumuler les valeurs
    if current_country == country:
        current_sum += value
    else:
        if current_country is not None:
            print("{}\t{}".format(current_country, current_sum))
        current_country = country
        current_sum = value

# afficher le dernier pays
if current_country is not None:
    print("{}\t{}".format(current_country, current_sum))
