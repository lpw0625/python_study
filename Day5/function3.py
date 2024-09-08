# # 표준 입력 
# print("python", "Java",  sep=",", end="?")

# #end="?" : 문장의 끝을 "?"으로 바꿔 달라
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) # 표준 출력으로 문장이 찍힘 
# print("Python", "Java", file=sys.stderr) # 표준 에러로 찍힘.

#출력 포맷

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")


    # ljust(8) : 8칸의 공간을 확보한 상태에서 왼쪽으로 정렬. 
    # rjust(4) : 4칸의 공간을 확보한 상태에서 오른쪽으로 정렬


    # 은행 대기순번표 
    # 001, 002, 003, .... 

    # for num in range(1,21):
    #     print("대기번호 : " + str(num).zfill(3))

        #zfill(3) # 3크기 만큼 공간을 확보 하고 값이 없는 빈공간은 0으로 채울것.

# answer = input("아무 값이나 입력하세요 :")
# # answer = 10 : 변수에 정수 값이 선언을 했기 문에 출력 했을때 자료형은 int로 뜬다.
# print(type(answer))
# # print("입력하신 값은 " + answer + "입니다: ")