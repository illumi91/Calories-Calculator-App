from temperature import Temperature
from calories_calculator import CaloriesCalculator


temperature_instance = Temperature(country="Italy", city="Ancona")
temperature = temperature_instance.get()
calories_calculator = CaloriesCalculator(weight=80, height=188, age=33, temperature=temperature)

print(calories_calculator.calculate())