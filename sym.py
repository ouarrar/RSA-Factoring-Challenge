#!/usr/bin/env python3
import sympy

# Replace this with the semiprime you want to factor
n = 143

# Use sympy's factorint function to factor n
factors = sympy.factorint(n)

print(f"Factors of {n}: {factors}")
