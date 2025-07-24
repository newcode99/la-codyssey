def main():
    user_input = input("숫자들을 공백으로 구분해서 입력하세요: ")
    input_list = user_input.split()  # 입력값을 공백 기준으로 나눔

    # 입력이 비어있는 경우 예외 처리
    if not input_list or user_input.strip() == "": #리스트가 비어있는 경우도 한 번 더 체크 (and / if not .split())
        print("Invalid input.")
        return

    numbers = []
    for value in input_list:
        try:
            num = float(value)  # 실수로 변환 
            numbers.append(num)
        except ValueError:
            print("Invalid input.")  # 숫자가 아닌 값이 있으면 에러
            return

    # 정렬 알고리즘: 버블 정렬 알고리즘 구현 (비교값이 높은 것을 우선 수로 설정)
    n = len(numbers) #객체의 길이 or 크기를 반환
    for i in range(n): # n나열 - > 첫 수 i 할당  
        for j in range(0, n - i - 1): #이중 루프 할당 / #IndexError 방지: 마지막 인덱스 접근 시 +1로 인해 에러 발생을 -1로 방지) /n - i - 1
            if numbers[j] > numbers[j + 1]: #앞 수가 클 경우 자리 swap # 앞에서부터 하나씩 옆이랑 비교 (0부터 시작) 
                # 두 값을 교환(스왑)                ㄴ []+[] 임으로 인덱싱 처리 numbers 리스트에서 j가 순서의 값을 탐색
                temp = numbers[j]  # 임시 변수 
                numbers[j] = numbers[j + 1] 
                numbers[j + 1] = temp

                # -i: 정렬이 끝나서 맨 뒤에 고정된 값들은 비교 대상에서 제외함.
                # -1: j+1 인덱싱을 할 때, 리스트 범위를 벗어나는 오류 방지

    # 결과 출력 (소수점 포함) : .join으로 공백을 이어붙힘(여러 값을 한줄로 하기 위함) 
    print("Sorted:", " ".join(str(float(num)) for num in numbers)) #numbers(리스트)의 각 num(숫자)을 float(num)로 실수 변환 후,str()로 문자열로 변경
                                                                        # ㄴ numbers 리스트에 있는 모든 값에 적용 
if __name__ == "__main__":
    main()
