#세트(집합)

# 중복 안됨, 순서 없음

my_set  = {1,2,3,3,5}
print(my_set) #중복된 숫자는 무시하고 출력된다.

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"])

#교집합 (java와 python을 모두 할 수 있는 개발자)

print(java & python)
print(java.intersection(python))

#합집합(Java를 할 수 있거난 python을 개발 할 수 있는 개발자)

print(java | python)
print(java.union(python))

#차집합(java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 을 할 줄 아는 사람이 늘어남

python.add("김태호")
print(python)

# java를 까먹었다

java.remove("김태호")
print(java)