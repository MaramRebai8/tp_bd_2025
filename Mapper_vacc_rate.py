#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin, delimiter=',')
next(reader)  # ignorer l'en-tête

for line in reader:
    if len(line) == 8:
        country = line[0].strip()
        fully_vaccinated = line[4].strip()
        if fully_vaccinated:
            try:
                value = float(fully_vaccinated)
                print(f"{country}\t{value}")
            except ValueError:
                continue
