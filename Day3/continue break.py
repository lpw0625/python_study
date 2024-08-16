absent = [2, 5] # 결석
no_book = [7] #책을 깜빡한 학생
for student in range(1,11): # 1부터 10번까지 출석번호
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 반복문을 종료하고 끝내기.
    print("{0},책을 읽어봐".format(student))