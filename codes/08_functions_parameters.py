# 함수 사용
# def function_name(param_first, ...) :
    # 실행할 코드
#     return result

# 점수 총합 함수 작성
kor = 60
eng = 70
math = 80

sum = kor + eng + math

def get_sum(korean, english, math=0) :
    # 실행할 코드
    summation = korean + english + math
    return summation

# sum = get_sum(kor, eng, math)
# print(f"총점: {sum}")

# sum = get_sum(kor, eng)
# print(f"총점: {sum}")

# for문 함수 작성
kor_scores = [70, 80, 90, 40, 50]
eng_scores = [90, 80, 70, 70, 60]
math_scores = [80, 70, 60, 90, 100]
# length = len(kor_scores)
# len_list = range(length)
# pass
# for i in range(len(eng_scores)) :
#     kor = kor_scores[i]
#     eng = eng_scores[i]
#     math = math_scores[i]
#     sum = get_sum(kor, eng, math)
#     print(f"{i+1}번 학생 총점: {sum}")

def get_for_sum(korean_scores, english_scores, mathmatics_scores) :
    for i in range(len(korean_scores)) :
        kor = korean_scores[i]
        eng = english_scores[i]
        math = mathmatics_scores[i]
        sum = get_sum(kor, eng, math)
        print(f"{i+1}번 학생 총점: {sum}")
    return 0

get_for_sum(kor_scores, eng_scores, math_scores)