# with

# import pickle

# with open("profile.pickle", "rb") as profile_file: # 해당 파일을 열어서 profile_file로 저장을 하여
#     print(pickle.load(profile_file)) # 저장된 profile_file를 불러옴


# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있는 개발자 지망생입니다.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
