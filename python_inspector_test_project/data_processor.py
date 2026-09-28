import os
import json

numbers = [10, 20, 30, 40, 50]

def calculate_average(values):
    total = sum(values)
    average = total / len(values)
    return average

result = calculate_average(numbers)
print("Average:", result)
