# 1) 한식, 중식, 일식 중 한 가지를 고르라
# 2) 그 중에서 한 가지를 고르면
# 식당 이름을 하나 임의로 추천
import random

kor = ["된장", "김치찌개", "비빔밥", "불고기"]
jpn = ["초밥", "라멘", "타코야끼", "우동"]
chn = ["자장면", "짬뽕", "탕수육", "양꼬치"]

#
print("=" * 50)
country =input("한국, 중국, 일본, 오늘 점심 국적은 어디?")
print("오케이, 오늘은 " + country + "으로 갑시다!")
#
#

if country == "한국" :
    print(random.choice(kor) +" 식당으로 가시죠" )
if country == "일본" :
    print (random.choice(jpn)+ " 식당으로 가시죠" )
if country == "중국" :
    print (random.choice(chn)+" 식당으로 가시죠" )
