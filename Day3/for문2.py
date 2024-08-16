# 한 줄 for문 

# #출석번호가 1,2,3,4 앞에 100을 붙이기로 함 => 101,102,103,104
# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

#학생 이름을 길이로 변환

# students =["iron man", "thor", "i am groot"]
# students= [len(i) for i in students] #lenth는 문자열의 길이를 의미한다. student라는 변수의 문자열 값을 세서 반복한다. 
# print(students)


students = ["iron man", "thor", "i am groot"]
students =[i.upper() for i in students]
print(students)

# 문자열이 전부 대문자로 바뀐다.

