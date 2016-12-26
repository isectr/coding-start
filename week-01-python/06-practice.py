# 1) 사용자로부터 단을 입력받는다
# 2) for 문으로 9단까지 만들어서 표기한다
# 3) format 형식으로

dan = int(input("몇단을 해볼까?"))
for num in range(1, 10) :
    print("{} * {} = {}".format(dan, num, dan * num))
