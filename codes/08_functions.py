# temp1 = 77
# celsius1 = (temp1 - 32) * 5 / 9
# print(celsius1)
# temp2 = 95
# celsius2 = (temp2 - 32) * 5 / 9
# print(celsius2)
# temp3 = 50
# celsius3 = (temp3 - 32) * 5 / 9
# print(celsius3)

# def function_name(param_first, ...) :
    # excute code (변수 + 약속어)
    # return result

# def function_name(param_first, ..., param_last) :
#     # 실행할 코드
#     return return_value

def to_celsius(temp) :
    # 실행할 코드
    celsius = (temp - 3) * 5 / 9
    return celsius

pass
to_celsius(120)
temp1 = to_celsius(77)
print(temp1)

temp2 = 100
result2 = to_celsius(temp2)
print(result2)
pass


# def fahrenheit_to_celsius(fahrenheit):
#     return (fahrenheit - 32) * 5 / 9

# 온도 리스트
# temps = [77, 95, 50]

# 반복문을 통해 처리
# for t in temps:
#     print(f"화씨 {t}도는 섭씨 {fahrenheit_to_celsius(t):.1f}도 입니다.")



# 1. { ... } (f-string 표현식)
# Python의 문자열 앞에 f를 붙이면(예: f"..."), 문자열 안에서 중괄호 {}를 사용해 변수나 계산식, 함수를 직접 넣을 수 있습니다.

# 이 중괄호 안의 내용은 실행되어 그 결과 값으로 대체됩니다.

# 2. fahrenheit_to_celsius(t) (값 계산)
# 가장 먼저 이 함수가 실행됩니다.

# t: 변수에 들어있는 화씨 온도 (예: 77)

# 함수 실행 결과: 섭씨 온도 계산값 (예: 25.0 또는 10.000000)

# 여기까지의 결과: 컴퓨터가 계산한 날것 그대로의 실수(float)입니다.

# 3. :.1f (서식 지정, Formatting)
# 계산된 숫자를 어떻게 보여줄지 결정하는 옵션입니다. 콜론(:) 뒤에 적습니다.

# :: "이제부터 이 값을 꾸며주는 옵션을 적겠다"는 구분선입니다.

# .1: **"소수점 아래 1자리까지 표현하라"**는 뜻입니다.

# 만약 소수점 자리가 더 길다면 반올림하여 자릅니다.

# 만약 소수점 자리가 없다면 .0을 붙여서 자릿수를 맞춥니다.

# f: 실수(float, fixed-point) 형태로 표현하라는 뜻입니다.