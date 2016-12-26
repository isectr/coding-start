# exceptions 예외처리
# try ~ except

# 1/0

def divide_by(first, second) :
    try :
        return first / second
    except ZeroDivisionError:
        return "멍충아"
print(divide_by(4,2))
print(divide_by(4, 0))

# 예외를 만들어 보자!
# Exception
class EvenNumberDevisionError(Exception):
    pass
# class의 경우 아래쪽에 뭐라도 하나 적어야하는 사오항
# >> pass로 빈자리 메우기

def divide_by_odd_number(first, second):
    if second % 2 == 0 :
        raise EvenNumberDevisionError
    else:
        return first / second

print(divide_by_odd_number(6,3))
print(divide_by_odd_number(6,2))


# raise. 에러를 일부러 일으켜야하는 상황
#>> 
