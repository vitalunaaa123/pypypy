result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a має бути більше або дорівнювати b")
        if b > 100:
            raise IndexError("b має бути менше або дорівнювати 100")
        return a / b
    except ZeroDivisionError:
        print("Помилка: Ділення на нуль")
        return None
    except Exception as e:
        print(f"Виняток: {type(e).__name__} - {str(e)}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        num_key = float(key) if isinstance(key, str) and key.isdigit() else key
        
        if not isinstance(num_key, (int, float)) or not isinstance(data[key], (int, float)):
            raise TypeError("Ключ або значення не є числом")
            
        res = divider(num_key, data[key])
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"Виняток при обробці {key}:{data[key]} - {type(e).__name__}: {e}")

print("Результат:", result)
