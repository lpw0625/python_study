# #반복문
# # print("대기번호 : 1")
# # print("대기번호 : 2")
# # print("대기번호 : 3")

# # for waiting_no in [0,1,2,3,4]:
# #     print("대기번호 : {0}".format(waiting_no))


# # 순차적으로 증가
# for waiting_no in range(1, 6) : # 0,1,2,3,4,
#     print("대기번호 : {0}".format(waiting_no))

starbucks = ["뜨거운 아아" , "망치대신 오함마 토르","슈트없는 아이언맨"]

for customer in starbucks:
    print("{0}, 커피가 준비되었어요.".format(customer))