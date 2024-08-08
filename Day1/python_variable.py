# 파이썬 언어 변수 

# 애완동물을 소개해 주세요~

# 변수 : 값을 저장하는 공간.
animal= "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3


print("우리집" + animal +"의 이름은 " + name + "입니다.")
hobby = "공놀이"
# print(name + "는" + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(name,"는" , age, "살이며, " , hobby , "을 아주 좋아해요")
print(name,"는 어른일까요?", is_adult)


# 문자 자료형에 변수를 함께 적을 수 있다.
# 단 변수 중에서 정수 자료형이나 boolean 자료형일 경우 str을 붙이고 적어야 한다. 
# 문자 자료형과 변수를 같이 적을때 "," 를 붙일 수 있다. 그리고, ","붙일 경우 앞에 str을 빼고 변수 그대로 넣어도 된다.