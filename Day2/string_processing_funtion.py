python = "Python is Amazing"
print(python.lower()) # 모든 문자가 소문자로 출력이 됨.
print(python.upper()) # 모든 문자가 대문자로 출력
print(python[0].isupper()) # 해당 순서의 문자가 대문자인지 확인.
print(len(python)) # 문자열 전체 길이를 드러냄.
print(python.replace("Python", "Java")) # 해당 문자를 선택하여 다른 문자로 바꾸는 것.


index = python.index("n")
print(index) # 해당 문자열에 "n"이 몇번쨰에 위치 하는지 출력.
index = python.index("n", index + 1)
print(index) # 앞에서 찾은 위치 그 다음번째 "n"의 위치를 출력한다.

print(python.find("Java")) # find 에서는 원하는 값이 없으면 -1을 출력
# print(python.index("Java")) # index 에서는 원하는 값이 없으면 오류가 난다.
# 오류가 난 그 다음 문장부터는 출력이 되지 않는다.

print(python.count("n")) # 해당 문자열에서 "n"이 총 몇 개 들어있는지를 출력.