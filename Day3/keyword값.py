#키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)
# 함수에서 전달받은 매개변수 값을 키워드 = 값을 넣어주면 함수 호출을 할 수 있다.
profile(name="유재석", main_lang ="파이썬", age=20)
profile(main_lang="자바" ,age=25, name="김태호")