#!/usr/bin/env python3
import sys

current_country = None
total = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    if len(parts) != 2:
        continue

    country, value_str = parts
    try:
        value = float(value_str)
    except ValueError:
        continue

    if current_country == country:
        total += value
        count += 1
    else:
        if current_country:
            avg = total / count if count > 0 else 0
            print(f"{current_country}\t{avg:.2f}")
        current_country = country
        total = value
        count = 1

# dernier pays
if current_country:
    avg = total / count if count > 0 else 0
    print(f"{current_country}\t{avg:.2f}")
