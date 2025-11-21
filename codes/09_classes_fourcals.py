
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return "0으로 나눌 수 없습니다."
    return a / b

print(f"3 + 5 = {add(3, 5)}")
print(f"10 - 4 = {sub(10, 4)}")
print(f"2 * 6 = {mul(2, 6)}")
print(f"8 / 0 = {div(8, 0)}")
