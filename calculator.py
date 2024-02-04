class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b

num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))

calc = Calculator(a=num1, b=num2)

print(f"""Addition: {calc.add()}
Substraction: {calc.sub()}
Multiplication: {calc.mul()}
Division: {calc.div()}""")
