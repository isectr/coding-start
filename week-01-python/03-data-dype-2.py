#목록 list, tuple
#사전 dict - dictionary
#집합 set


list []
print("list")
print ([1, 2, 3])
여기부터
list_a = [1,2,3]
print(list_a)
# print (type([1, 2, 3]))
## index는 0부터 시작합니다. 숫자가 어떻게 1부터 시작하냐. 0부터 시작한다!
print(list_a[0])
#
# 슬라이스
print(list_a[0:2])
list_a.append(4)
print(list_a)
list_a.remove(2)
print(list_a)
#클리어
list_a.clear()
print(list_a)

# # tuple (1, ) <<괄호만 넣으면 튜플 인지 못해
print("tuple")
print ((1, 2, 3))
print (type ((1, 2, 3)))

tuple_a = (1, 2, 3)
print(tuple_a)
print(type (tuple_a))
tuple_a.append(4)
print(tuple_a)

# dict (map) {}
# key & value
dict_a = {
"apple" : "a type of fruit",
"pen" : "a thing to write"
}
# dict_a = {"key" : "value"}
print(dict_a)
print(dict_a["apple"])
dict_a["pen"] = "someting to write"
print(dict_a)

# set set([]) > 집합, 중복이 없기 때문에 사용.
# 리스트는 그저 목록. 집합은 중복이 불가능하다.
# >> set은 중복이 자동으로 제거된다.
set_a = set([1, 2, 3])
set_b = set([2, 4, 6])
# 교집합, 합집합, 차집합
print(set_a & set_b)
print(set_a | set_b)
print(set_a - set_b)
