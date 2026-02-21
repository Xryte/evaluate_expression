def evaluate_expression(expr: str):
    allowed = set("0123456789+-*/(). ")
    for ch in expr:
        if ch not in allowed:
            return "Ошибка (недопустимый символ)"

    try:
        result = eval(expr, {"__builtins__": None}, {})
        if isinstance(result, (int, float)):
            return result
        else:
            return "Ошибка (неверный результат)"
    except ZeroDivisionError:
        return "Ошибка (деление на 0)"
    except Exception:
        return "Ошибка (неверное выражение)"


#Тесты
def run_tests():
    tests = {
        "2+2": 4,
        "2*3": 6,
        "2+2*3": 8,
    }
    for expr, expected in tests.items():
        out = evaluate_expression(expr)
        print(f"{expr} = {out} (Получилось: {expected})")

if __name__ == "__main__":
    run_tests()
