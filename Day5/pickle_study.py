#pickle
# 피클 : 프로그램 상에서 사용하고 있는 데이터를 파일 형식으로 저장을 하는 것. 
# 파일 형식의 데이터를 다시 불러와서 코드로 쓸 수 있다.

import pickle


# profile_file = open("profile.pickle", "wb") # 피클은 따로 인코딩을 할 필요가 x 
# profile = {"이름":"이평원", "나이":30, "취미":["게임", "헬스", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)# profile 에 있는 정보를 file 에 저장.
# profile_file.close()

# 파일에서 데이터를 가지고 오기. 
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()

# 에러 
# AttributeError: partially initialized module 'pickle' has no attribute 'dump' (most likely due to a circular import)
# 모듈 이름이 pickle 인 경우 python 파일 이름을 pickle.py로 설정했다면 
# python이 표준 라이브러리 pickle 모듈 대신 해당 파일을 참조하려고 하면서 문제가 발생 
# 파일 이름을 pickle.py로 하지 말고 pickle_study 이라는 다른 이름으로 해서 해결.