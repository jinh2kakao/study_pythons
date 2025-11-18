first = 5

# while 문장구조
# while condition:
#    executable_statement(s)

while first > 0 :
    print("while 값 :"+str(first))
    if first == 3 :
        print("while 중단")
        break
    first = first - 1

print("while 종료")