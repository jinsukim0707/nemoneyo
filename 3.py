balance = 10000  # 잔고 10000원
#withdrawl = input("출금액을 입력하세요:") 를 사용한다면 에러가 발생합니다.
#input()함수를 다시 int()함수로 감싸서 형변환 해줘야 합니다.
withdrawl = int(input("출금액을 입력하세요:")) # 출금액 2000원 입력

if balance >= withdrawl:  #조건 1
    print(str(withdrawl)+"원을 출금합니다.")
    balance = balance - withdrawl #출금액만큼 잔고에서 빼주기
    #들여쓰기가 끝났습니다. 이 이후부터는 if문 밖입니다.

print("잔고: " + str(balance))
