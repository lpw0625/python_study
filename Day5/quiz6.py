# 퀴즈6

# 당신의 회사에서는 매주 1회 작성해여 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간보고 -

# 부서 : 
# 이름 :
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성 하시오.

# 조건: 파일명은 "1주차.txt", "2주차.txt", ... 와 같이 만듭니다.




# 제출 답안 

# import sys


# reports = {"부서:인사부", "이름: 이평원", "업무 요약:1주차 보고 입니다."}


# report_file = open("x주차.txt", "w", encoding="utf8")
# print("부서:인사부",file=report_file)
# print("이름:이평원",file=report_file)
# print("업무 요약:xx입니다.",file=report_file)
# report_file.close()

# for num in range(1,51):
#     print("주간보고: " + str(num).zfill(3))

#========================================================================================


#정답

for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write(" - {0} 주차 주간보고 - ".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")




