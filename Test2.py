#기본은 리스트의 첫 글자를 딴 result를 변형시키는 것에서 부터 시작
result = s[0]
#카운트 숫자를 합쳐줘야할 것
count = 0

#스트링을 읽을동안,
for st in s:
    #첫번째 스트링이 result의 마지막 문자와 같다면
    if st == result[-1]:
        #카운트를 올려주는거임. 뭐 다른짓 하는건 아니고
        count += 1
      #그렇게 카운트 올리다가 만약에 다른 문자를 만난다면,  
    else:
        #그때야 result에 일단 이때까지 세알렸던 카운트 꼬라박고 다른문자까지 합쳐줌
        result += str(count) + st #여기 개념이 아예 없없음. 문자 카운트 + st라면 s중 그다음꺼
        #여기는 카운트 다시 초기화 해줄 작업이 필요함
        count = 1
        
result += str(count) # 마지막놈 카운트해서 넣어준다는 거네 하 ㅋ 세키
print(result)



        
