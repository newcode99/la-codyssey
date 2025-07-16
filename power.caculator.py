num_input = input("enter number:")

try:
    number = float(num_input)
    # 입력값을 실수(float)로 변환

except ValueError:
    print("invalid number input.")
    exit()

exp_input = input("enter exponent:") 
#지수(제곱 수) 입력 받기

try:
    exponent = int(exp_input)
    #제곱 - 입력값 정수 변환 시도 
except ValueError: 
    print("invalid exponent input")
    exit()

# 거듭 제곱 계산 로직 (입력값 만큼 지수 반복문 설정)
result = 1
if exponent >= 0:
    for _ in range(exponent):
        result = result * number
else:  #>=0 제외 
    for _ in range(-exponent):
        result = result * number
    result = 1 / result #음수 처리 연산식 


print(f"Result: {int(result) if result.is_integer() else result}")
#수의 형태의 따라 노출되도록 설정 

if __name__ == "__main__":
    pass
