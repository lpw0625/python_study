# 파이썬 언어 함수
# 시작과 끝에는 선언된 함수로 시작하여 끝을 낸다.
def open_account():
    print("새로운 계좌가 생성되었습니다.")

open_account()


#전달값과 반환값

def deposit(balance, money): #현재 금액과 입금 하는 금액
    print("입금이 완료 되었습니다. 잔액은 {0} 원입니다." .format(balance + money)) #입금하는 함수를 호출하여 현재 금액과 입금 금액을 합치고
    return balance + money 
#합친 값을 되돌려 받는다.

def withdraw(balance, money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance
    
def withdraw_night(balance,money): #저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission #수수료가 얼마 나왔고 현재 잔액에서 출금 금액과 수수료를 뺀 값을 튜플 형식으로 보낸다.

    
balance = 0  # 잔액
balance = deposit(balance, 1000)  # 현재 금액과 1000원 입금액이 둘 다 있는 상태.
# balacne = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance,500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다." .format(commission, balance))
print(balance) # 입금 금액이 합쳐진 현재 금액으로 출력이 된다 .

