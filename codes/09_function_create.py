# 공통 사항 : 제출 문제마다 function 실행은 최소 3회 호출

# 🔹 문제 1
# 섭씨 온도 3개를 받아 평균을 반환하는 함수 avg_celsius(t1, t2, t3) 를 작성하시오.

def avg_celsius(t1, t2, t3):
    return (t1 + t2 + t3) / 3

test_cases = [
    (20, 22, 24),
    (30, 30, 30),
    (10, 15, 25)
]

print("--- 문제 1 실행 결과 ---")
for t1, t2, t3 in test_cases:
    result = avg_celsius(t1, t2, t3)
    print(f"입력({t1}, {t2}, {t3}) -> 평균: {result:.2f}°C")

# 🔹 문제 2
# 이름과 좋아하는 언어 2개를 받아 아래 형식으로 출력하는 함수를 작성하시오.
# 홍길동님의 선호 언어는 Python, Java 입니다.

def print_fav_languages(name, lang1, lang2):
    print(f"{name}님의 선호 언어는 {lang1}, {lang2} 입니다.")

users = [
    ("홍길동", "Python", "Java"),
    ("이영희", "C++", "JavaScript"),
    ("김철수", "Swift", "Kotlin")
]

print("\n--- 문제 2 실행 결과 ---")
for name, l1, l2 in users:
    print_fav_languages(name, l1, l2)


# 🔹 문제 3
# 점수 리스트를 받아 60점 이상 점수만 누적한 합계를 반환하는 함수를 작성하시오.

def sum_over_60(scores):
    total = 0
    for score in scores:
        if score >= 60:
            total += score
    return total

score_lists = [
    [50, 70, 80, 40, 90],
    [100, 100, 59, 55],
    [20, 30, 40, 50]
]

print("\n--- 문제 3 실행 결과 ---")
for scores in score_lists:
    result = sum_over_60(scores)
    print(f"입력 {scores} -> 합계: {result}")


# 🔹 문제 4
# 문자열 두 개를 받아 하나의 문장으로 이어 붙이는 함수 combine(str1, str2) 작성.

def combine(str1, str2):
    return str1 + " " + str2

# 테스트 데이터
word_pairs = [
    ("Hello", "World"),
    ("Python", "Programming"),
    ("Good", "Morning")
]

print("\n--- 문제 4 실행 결과 ---")
for w1, w2 in word_pairs:
    print(f"결과: {combine(w1, w2)}")

# 🔹 문제 5
# 온도 리스트를 받아 모두 섭씨로 변환해 새로운 리스트로 반환하는 함수 작성.

def to_celsius_list(temps):
    celsius_list = []
    for t in temps:
        c = (t - 32) * 5 / 9
        celsius_list.append(round(c, 1))
    return celsius_list

# 테스트 데이터
temp_lists = [
    [32, 212],       # 0도, 100도
    [77, 95, 50],    # 랜덤 온도
    [100, 0, -40]    # 고온/저온
]

print("\n--- 문제 5 실행 결과 ---")
for temps in temp_lists:
    result = to_celsius_list(temps)
    print(f"화씨 {temps} -> 섭씨 {result}")

