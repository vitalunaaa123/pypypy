class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def get_salary_info(self):
        return f"Заробітна плата {self.name}: {self.salary}"

# Приклад створення об'єкта та виклику методу
employee = Employee("Іван Петренко", "Розробник", 50000)
print(employee.get_salary_info())  # Виведе: "Заробітна плата Іван Петренко: 50000"