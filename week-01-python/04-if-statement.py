# 참과 거짓 boolean
# if
# True, False < 반드시 대문자
# and, or, not

# a= True
# b = False
# # A가 참이고 그리고 B가 참이라면
# print(a and b)
# # A가 참이거나 혹은 B가 참이라면
# print(a or b)

# = < 할당한다
# == < 동일하다
# a = True
# print(a == True)
# print(a is True)

d = 12
if d > 10 :
    print("숫자는 10보다 크다")
elif d > 5 or d <= 10 :
    print("숫자는 10보다 작거나 같고, 5보다 크다")
else :
    print("숫자는 5보다 작거나 같다")
