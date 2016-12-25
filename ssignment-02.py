#1) 사람 클래스를 하나 만듭니다.
#2) 기본 요소는 이름, 나이, 성별
#3) 직장 동료 클래스를 사람 클래스를 이용해서 만듭시다.
#4) 사람 기본 요소 외 별도의 추가 사항은 직급

class Human :
    name = "화강윤"
    age = "29"
    sex = "남"


class Coworker(Human) :
    position
