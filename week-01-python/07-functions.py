# 함수 functions : 코드를 간략하고 쉽게 짜기 위한 툴
# 입력값 parameters, 반환값 return <반환값이 있어야 변수에 담을 수 있다

# def > 데피니션

def hello_friends(nam):
    print("hello, {}".format(nam))

name1 = "강윤"
name2 = "은혜"
name3 = "맥스"
name4 = "크림"

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)

# 입력값 있고, 반환값 있고
def sum(a, b):
    return a + b
# 입력값 있고, 반환값 없고
def hello_friends(nam):
    print("hello, {}".format(nam))
# 입력값 없고, 반환값 있고
def return_1():
    return 1
# 입력값 없고, 반환값 없고
def hello_world():
    print("hello world")

num_1 = return_1()
print(num_1)

# "반환값이 있다는 건 리턴을 한다는 이야기고,
# 리턴을 한다는 것은 변수에 담을 수 있다"
