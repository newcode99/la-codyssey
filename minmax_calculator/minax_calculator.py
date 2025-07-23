#입력 → 분리 → 숫자 변환/검증 → 최소/최대값 찾기 → 출력

def main():

    user_input = input("숫자들을 공백으로 구분해서 입력하세요: ")

    input_list = user_input.split() #유저가 입력한 수를 구분자(공백 기준)를 지어 input_list에 삽입

    numbers = [] #리스트로 만듬

    for value in input_list: #input_list에 삽입된 값을(value)가져온 value값 / true 지속 검증 (아래서 호출)
    
        try: 
            num = float(value) #value 값을 실수로 지정 후 num에 삽입
            numbers.append(num) # []에 num 값을 뒤로 추가

        except ValueError:
            print("Invalid input.") #값이 숫자가 아닐 경우 에러 발생 / 반환
            return

    min_value = numbers[0] #min 
    max_value = numbers[0] # 값 비교의 기준 설정 / []의 첫째 값을 기준값으로 설정

    for num in numbers [1:]: #리스트 2번째 값부터 ~ 끝까지
    
        if num < min_value: #최소값 지정: num 값과 []첫째값과 비교 
            min_value = num

        if num > max_value: #최대값 지정: num 값과 []첫째값과 비교 
            max_value = num

    print(f"Min: {min_value}, Max: {max_value}") #f-str / Min은 {min_value} 함수, Max는 {max_value}에서 불러옴.
    #유저가 입력한 숫자들 내에 서 최소값인 것과 최대값인 것을 1개씩 잡아서 출력함?

if __name__ == "__main__":
    main()

#공백 예외처리 추가 진행
