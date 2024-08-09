# 슬라이싱
# 필요한 부분만 가져 오는 것을 슬라이싱 이라고 한다. 

juminumber = "950625-1234567"

print("성별: " + juminumber[7]) # 주민등록 번호 성별 기준 숫자 위치
print("년도:" + juminumber[0:2]) # 0부터 2 직전까지 (0,1)값만 가지고 온다.
print("월:" + juminumber[2:4])
print("일:" + juminumber[4:6])

print("생년월일:" + juminumber[:6]) # 처음부터 6직전까지 값을 가지고 온다.
print("뒤 7자리 :" + juminumber[7:]) # 7번째 부터 끝까지 가지고 온다.
print("뒤 7자리 (뒤에서부터) :" + juminumber[-7:]) # 맨 뒤에서 7번쨰부터 끝까지
