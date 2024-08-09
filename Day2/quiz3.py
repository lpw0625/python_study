# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

#ex) http://naver.com

#규칙1 : http:// 부분을 제외 => naver.com
#규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver 
#규칙3 : 남은 글자 중 처음 세자리 + 글제 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
#                (nav)               (5)      (1)      (!)
# 예시) 생성된 비밀번호 : nav51!

#출제 답인

# # 사이트 :http://google.com

# passwordsite = "http://google.com"

# delete_str1 = passwordsite.replace("http://","")
# delete_str2 = passwordsite.replace(".com", "")

# password = passwordsite[0:2] + passwordsite.len("google") + passwordsite.count("g") + "!"


#정답

# passwordsite = "http://google.com"
passwordsite = "http://daum.net"

delete_str1 = passwordsite.replace("http://","") # 규칙 1
# print(delete_str1)
delete_str1 = delete_str1[:delete_str1.index(".")] # 규칙 2 
# print(delete_str1)
password = delete_str1[:3] + str(len(delete_str1)) + str(delete_str1.count("n")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(passwordsite,password))



