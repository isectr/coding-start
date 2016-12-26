# 클래스 class

## Article variables
title1 = "개발"
author1 ="마르코"
content1= "개발은 쉬워요"
view_count1 = 0

title2 = "코칭"
author2 ="마르코"
content2= "코칭은 쉬워요"
view_count2 = 0

title3 = "창업"
author3 ="마르코"
content3= "창업은 쉬워요"
view_count3 = 0

# >>이 내용을 간단히 만들려면 'class'!!

# 클래스는 대문자로 많이 시작한다.
# class Article:
#     title = "개발"
#     author ="마르코"
#     content= "개발은 쉬워요"
#     view_count = 0
#
# article1 = Article()
# print(article1.title)
# article2 = Article()
# article2.title = "코칭"
# print(article1.title)
# print(article2.title)

### Article class with __init
class Article:
    author ="마르코"
    view_count = 0

#클래스 안에서 만드는 함수는 항상 self 를 넣어줘야
    def __init__(self, title, content):
        self.title = title
        self.content = content
    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("개발", "개발은 쉬워요")
article2 = Article("코칭", "코칭은 쉬워요")
article3 = Article("창업", "창업은 쉬워요")
#
# print(article1.view_count)
# article1.read()
# print(article1.view_count)

# 클래스가 중요한 이유!! inheritance 상속
class Brunch(Article):
    sounce = "브런치"
    def read(self):
        self.view_count = self.view_count + 2

# 인스턴트 활성화
abcd = Brunch("개발", "개발은 쉬워요")
print(abcd.title)
print(abcd.sounce)
print(abcd.view_count)
abcd.read()
print(abcd.view_count)

# 부모 클래스의 함수를 자식 클래스에서 덮어쓸 수 있다
# > 오버라이드. 이런 경우 새로 정의된 내용이 나온다

print(abcd.view_count)
abcd.read()
print(abcd.view_count)
