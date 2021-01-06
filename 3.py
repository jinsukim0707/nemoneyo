
balance = 10000  

if balance >= withdrawl:  
    print(str(withdrawl)+"원을 출금합니다.")
    balance = balance - withdrawl 
print("잔고: " + str(balance))

def func(x,y):
return 2*x+y**2

print(type(func))
print(func(3,4), end='\n\n')

f=lambda x,y: x**2+2*y
print(type(f))
print(f(3,4))
