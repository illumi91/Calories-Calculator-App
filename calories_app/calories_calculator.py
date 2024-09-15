class CaloriesCalculator:
    """
    Represents the amount of calories calculated:
    BMI = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """
    def __init__(self, weight, height, age, temperature):
        self.weight = float(weight)
        self.height = float(height)
        self.age = float(age)
        self.temperature = temperature
        
    def calculate(self):
        BMI = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5 - 10 * 10
        return BMI