#지역변수와 전역변수

#지역변수 : 함수 내에서 쓸 수 있는것.
#전역 변수 : 모든 공간에서 어디서든지 부를 수 있는 변수.

gun = 10

def checkpoint(soldiers): # 경계근무 
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))

