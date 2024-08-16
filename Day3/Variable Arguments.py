#가변 인자
#파이썬에서 위치, 키워드 인자의 개수가 많아지거나 인자의 수가 미정일 경우 가변인자를 사용합니다

# def profile(name, age, lang1 , lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4 ,lang5)

def profile(name, age,*language):
    print("이름 : {0}\t나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석" , 20, "Python", "java", "C", "C++", "C#","JavaScript")
profile("김태호", 23, "Kotiln","Swift","","","")