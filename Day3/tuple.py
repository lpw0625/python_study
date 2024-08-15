#튜플 
# 리스트와는 다르게 내용 변경이 불가능 하다.

menu = ("돈까스", "치킨까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 오류발생 tuple은 add기능이 지원하지 않는다.

name = "김종국"
age = 45
hobby = "헬스"
print(name,age,hobby)

(name,age,hobby) = ("김종국",45,"헬스")
print(name, age,hobby)


