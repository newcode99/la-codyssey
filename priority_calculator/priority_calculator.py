# 함수 기능 정의 - 연산 시 호출

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero." #zero division ( 0/ 처리문 )
    return a / b

#입력 처리
def main():
    user_input = input("숫자들을 공백으로 구분해서 입력하세요:")
    tokens = user_input.split() # 구분자를 통해 나눔 (공백) -> []변형

#입력 검증: 수의 연산 성립 
    if len(tokens) < 3 or len(tokens) % 2 == 0: #숫자, 연산자, 숫자를 필수적으로 입력해야 수식이 완성됨으로 invalid 처리 (짝수 불가)
        print("invalid input.")                     # 나머지 연산자(%) / 어의 개수가 3개보다 작거나(or) 단어의 개수가 짝수
        return                                                    # ㄴ 3<3도 flase이기에, <3이 true가 되면 그냥 바로 종료하고 옆으로 3이 넘어가도 0이 아님으로 flase 즉, 오류 아님(성립)
     
    numbers = []
    operators = []
    try:  #연산자 분리 및 검증
        for i, token in enumerate(tokens): #작동 / tokens를 번호 매겨서 나온 것을, i와 token에 각각 담아 반복

            if i % 2 == 0: #수와 연산의 순서(숫자, 연산 ---)식으로 원활한 연산식이 되는지 검증
                numbers.append(float(token)) # 여기선 i가 enumerate로 인해 번호표 역할을 함.
            else:
                if token not in ['+', '-', '*', '/']:  # 분리된 리스트(numbers & operators)로 안전하게 재분배
                    print("Invalid input.")                 #ㄴtoken에 할당된 연산자 값이 -연산 리스트와 비교했을 때 포함되었지않은가.
                    return
                operators.append(token) #연산자 값이 연산 리스트와 비교했을 때 존재하지 않는다면, op(연산통)에 삽입.


    except ValueError:
        print("Invalid input.")
        return

    # 곱셈/나눗셈 먼저 처리 (사칙연산)
    i = 0
    while i < len(operators):
        if operators[i] == '*' or operators[i] == '/': #perators 리스트 안에서 i번째 위차한 값을 가져옴,
            a = numbers[i]                                #ㄴ 근데 이는 "연산수"가 들어옴으로 연산수 끼리 비교하는 것임
            b = numbers[i+1]   #위 op, numbers는 구조적 관계를 갖음으로 / i번째에서 왼쪽, 오른쪽 값을 차출
            if operators[i] == '*':     #만얀 연산수가 *와 같다면 아래문(*)실행
                result = multiply(a, b)
            else:                         
                result = divide(a, b)           # 아니라면 / 실행
                if result == "Error: Division by zero.": #반환
                    print(result)
                    return
            # 결과를 numbers[i]에 넣고, numbers[i+1] 삭제
            numbers[i] = result  #numbers 리스트의 i번째(1번째) 칸의 값을 변수 result의 값으로 할당
            del numbers[i+1] #Sequence / 계산에 사용된 숫자 삭제
            del operators[i]               #ㄴ 계산에 사용된 연산 수식 삭제 
        else:
            i += 1 #operators[i] == '*' or operators[i]가 flase일 때 실행 / i = i + 1

    # 덧셈/뺄셈 처리
    i = 0
    while i < len(operators):
        a = numbers[i] #number 리스트에서 i번째 수를 가져와서 저장
        b = numbers[i+1] # []에서 i번째 수에서 한 칸 뒤 값을 가져와 저장
        if operators[i] == '+': #연산 리스트에서 0번 문자열이 +와 같은가 비교
            result = add(a, b)
        else:
            result = subtract(a, b) #add(a, b)가 False임으로 해당 문에선 true가 됨.
        numbers[i] = result #numbers 리스트의 i번째(0번째) 칸의 값을 result 변수에 저장된 값으로 할당
        del numbers[i+1] #연산 데이터 순서로 간 값은 삭제
        del operators[i] #숫자 데이터 순서로 간 값은 삭제

    # 결과 출력
    print("Result:", float(numbers[0]))

if __name__ == "__main__":
    main()

#리스트에서 *, /을 먼저 처리 -> 결과 산출로 리스트 줄여야 함.
