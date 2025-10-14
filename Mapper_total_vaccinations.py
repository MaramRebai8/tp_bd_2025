#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin, delimiter=',')
next(reader)

for line in reader:
    if len(line) == 8:
        daily_vac = line[3].strip()
        if daily_vac:
            try:
                value = float(daily_vac)
                print(f"Total\t{value}")
            except ValueError:
                continue
