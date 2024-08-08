#파이썬 연산자

# print(1+1)
# print(3-2)
# print(5*2)
# print(6/3)


# print(2**3) # 2^3 = 8
# print(5%3) # 나머지 구하기 2
# print(10%3) # 1
# print(5//3) # 몫 1
# print(10//3) # 몫 3

# print(10 > 3)
# print(4 >= 7)
# print(10 < 3)
# print(5 <= 5)

# print(3==3) # 앞과 뒤의 값이 똑같은지를 확인.
# print(1 != 3) # !부정의 의미. 앞뒤가 똑같지 않다.
# print(not(1 != 3))
# print((3 > 0) and (3 < 5)) 
# print((3 > 0) or (3 > 5))

# print(2 + 3 * 4) #14
# print((2 + 3) * 4) # 20
# number = 2 + 3 * 4  # 14
# print(number)
# number = number + 2 #16
# print(number)
# number += 2  #18
# print(number)
# number *= 2 # 36
# print(number)
# number /= 2 # 18
# print(number)
# number -= 2  # 16
# print(number)

#-------------------------------------------------------

#숫자처리 함수 
#abs(절대값)
#pow((제곱근))
#max((최대값))
#min((최소값))
#round(반올림)

print(abs(-5)) #5
print(pow(4,2)) # 4^2 = 4*4 = 16
print(max(5,12)) # 12 
print(min(5,12)) # 5
print(round(3.14)) # 3


from math import * # math 라이브러리 안에 있는 것들을 모두 이용하겠다.,
print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4

