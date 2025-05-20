class Employee:
    def __init__(self, name: str, position: str, salary: float):
        self.name = name
        self.position = position
        self.salary = salary
    
    def get_salary_info(self) -> str:
        return f"Заробітна плата {self.name}: {self.salary}"


if __name__ == "__main__":
    # Приклад створення об'єкта та виклику методу
    employee = Employee("Іван Петренко", "Розробник", 50000)
    print(employee.get_salary_info())  # Виведе: "Заробітна плата Іван Петренко: 50000"