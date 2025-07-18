def add(a, b):
    return a + b  # 두 수를 더함

def subtract(a, b):
    return a - b  # 두 수를 뺌

def multiply(a, b):
    return a * b  # 두 수를 곱함

def divide(a, b):
    if b == 0:
        return "Error: Division by zero."  # 0으로 나누면 에러 메시지
    return a / b  # 두 수를 나눔

if __name__ == "__main__":
    try:
        a = int(float(input("첫 번째 숫자를 입력하세요: ")))  # 실수 입력(정수도 가능)
        b = int(float(input("두 번째 숫자를 입력하세요: ")))  # 실수 입력(정수도 가능)
        op = input("연산자(+, -, *, /)를 입력하세요: ")  # strip()을 붙이면 공백 자동 제거

        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = subtract(a, b)
        elif op == "*":
            result = multiply(a, b)
        elif op == "/":
            result = divide(a, b)
        else:
            result = "Invalid operator."  # 잘못된 연산자

        print("Result:", float(result))

    except ValueError:
        print("Invalid input. Please enter valid numbers.")  # 숫자가 아닌 값 입력 시 안내