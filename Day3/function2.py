#지역변수와 전역변수

#지역변수 : 함수 내에서 쓸 수 있는것.
#전역 변수 : 모든 공간에서 어디서든지 부를 수 있는 변수.

gun = 10

def checkpoint(soldiers): # 경계근무 
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

    print("전체 총 :{0}".format(gun))
    checkpoint(2) # 2명이 경계 근무 나감
    print("남은 총 : {0}".format(gun))

    #checkpoint함수 내의 "gun"이 값이 초기화가 안됐는데 쓸 수가 없다고 에러가 뜬다. 
