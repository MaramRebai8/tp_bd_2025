#!/usr/bin/env python3
import sys

total_vaccinations = 0.0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue

    _, value_str = parts
    try:
        value = float(value_str)
    except ValueError:
        continue

    total_vaccinations += value

print(f"Total vaccinations (all countries):\t{total_vaccinations:.0f}")
